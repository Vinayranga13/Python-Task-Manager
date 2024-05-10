from django.contrib import admin
from django.urls import path
from task_manager import views  # Use the correct module name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/add/', views.task_form, name='task_add'),
    path('task/edit/<int:task_id>/', views.task_form, name='task_edit'),
    path('task/delete/<int:task_id>/', views.task_delete, name='task_delete'),
]
