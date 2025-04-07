from django.urls import path
from .views import DatabaseView, DatafieldView, DatatableView

urlpatterns = [
    path('database/', DatabaseView.as_view(), name='database'),
    path('datatable/', DatatableView.as_view(), name='datatable'),
    path('datafield/', DatafieldView.as_view(), name='datafield'),
]
