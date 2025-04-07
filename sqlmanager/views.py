from django.http.response import JsonResponse
from .models import Databasemanagement, Tablemanagement, Fieldmanagement
from sqlhelper.Base.base_views import CRUDView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication



class DatabaseView(CRUDView):

    authentication_classes = []
    permission_classes = [AllowAny]

    model = Databasemanagement
    vague_search_fields = ['database_name', 'system_name', 'description']
    exact_search_fields = ['creator', 'software']
    datetime_fields = ['created', 'updated']  

    def get_queryset(self):
        query = super().get_queryset()  
        return query  
    


class DatatableView(CRUDView):

    authentication_classes = []
    permission_classes = [AllowAny]

    model = Tablemanagement
    vague_search_fields = ['table_name', 'description']
    exact_search_fields = ['creator', 'status']
    datetime_fields = ['created', 'updated']  

    def get_queryset(self):
        query = super().get_queryset()  
        return query  
    


class DatafieldView(CRUDView):

    authentication_classes = []
    permission_classes = [AllowAny]

    model = Fieldmanagement
    datetime_fields = ['created', 'updated']  

    def get_queryset(self):
        query = super().get_queryset()  
        return query  