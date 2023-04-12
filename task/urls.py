from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete_item/<str:pk>/', views.deleteTask, name='delete_item'),
]