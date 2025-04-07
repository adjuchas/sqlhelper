from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.db.models import Q
from django.utils import timezone
from datetime import datetime

class CRUDView(APIView):
    model = None  # 子类应指定
    soft_delete_field = None  # 子类应指定软删除字段名
    vague_search_fields = []  # 子类应指定模糊搜索的字段
    exact_search_fields = []  # 子类应指定精确搜索的字段
    datetime_fields = []  # 子类应指定需要格式化的日期字段（时间戳）
    
    def get_queryset(self):
        """Return filtered queryset based on search parameters."""
        query = self.model.objects.all()

        # 处理模糊搜索
        search = self.request.GET.get('search', None)
        if search and self.vague_search_fields:
            query = query.filter(
                Q(**{f"{field}__icontains": search}) for field in self.vague_search_fields
            )
        
        # 处理精确搜索
        exact_search = self.request.GET.get('exact_search', None)
        if exact_search and self.exact_search_fields:
            query = query.filter(
                Q(**{f"{field}__exact": exact_search}) for field in self.exact_search_fields
            )
        
        return query
    
    def format_datetime(self, obj):
        """Format datetime fields from timestamp to human-readable format."""
        for field in self.datetime_fields:
            if hasattr(obj, field) and getattr(obj, field):
                timestamp = getattr(obj, field)
                try:
                    # Assuming the timestamp is in seconds and is stored as a string
                    dt = datetime.utcfromtimestamp(int(timestamp) / 1000)  # Convert ms to seconds
                    formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S')  # Adjust the format as needed
                    setattr(obj, field, formatted_time)
                except ValueError:
                    pass  # If conversion fails, leave it as is
        return obj

    def get(self, request, *args, **kwargs):
        """Handle GET request to fetch data or a single record."""
        if 'id' in kwargs:
            obj = get_object_or_404(self.model, id=kwargs['id'])
            obj = self.format_datetime(obj)  # 格式化日期字段
            return JsonResponse({'data': obj.to_dict()})
        else:
            data = list(self.get_queryset().values())
            # 格式化日期字段
            for obj in data:
                obj = self.format_datetime(obj)
            return JsonResponse({'data': data})

    def post(self, request, *args, **kwargs):
        """Handle POST request to create a new record."""
        data = request.POST
        new_obj = self.model.objects.create(**data)
        return JsonResponse({'data': new_obj.to_dict()}, status=201)

    def put(self, request, *args, **kwargs):
        """Handle PUT request to update a record."""
        if 'id' in kwargs:
            obj = get_object_or_404(self.model, id=kwargs['id'])
            data = request.POST
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
            obj = self.format_datetime(obj)  # 格式化日期字段
            return JsonResponse({'data': obj.to_dict()})
        return JsonResponse({'error': 'Invalid ID'}, status=400)

    def delete(self, request, *args, **kwargs):
        """Handle DELETE request to perform soft delete (if soft_delete_field is specified)."""
        if self.soft_delete_field is None:
            return JsonResponse({'error': 'Delete operation not allowed. No soft delete field defined.'}, status=400)
        
        if 'id' in kwargs:
            obj = get_object_or_404(self.model, id=kwargs['id'])
            setattr(obj, self.soft_delete_field, True)
            obj.deleted_at = timezone.now()  # 记录删除时间
            obj.save()
            return JsonResponse({'message': 'Soft deleted successfully'})
        return JsonResponse({'error': 'Invalid ID'}, status=400)
