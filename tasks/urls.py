from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name = 'home'),
    path('update_task/<str:pk>/', views.updateTask,name='update_task'),
    path('delete/<str:pk>/',views.deleteTask, name = 'delete')
]

