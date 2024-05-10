from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import views from this package

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task_list'),  # Main task list
    path('task/<int:pk>/', views.task_detail, name='task_detail'),  # Task detail
    path('task/add/', views.task_add, name='task_add'),  # Add new task
    path('task/edit/<int:pk>/', views.task_edit, name='task_edit'),  # Edit existing task
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
