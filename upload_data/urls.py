
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"), 
    path('update_db', views.upload_data_ftn, name = "update_db_name")    
]