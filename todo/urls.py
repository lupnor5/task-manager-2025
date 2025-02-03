from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:task_id>',views.delete , name='delete'),
    path('update/<int:task_id>',views.update , name='update'),
]