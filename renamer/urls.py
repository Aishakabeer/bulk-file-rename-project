from django.urls import path
from . import views

urlpatterns = [
    path('', views.rename_files, name='rename_files'),
]
