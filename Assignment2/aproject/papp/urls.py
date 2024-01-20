
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('add/', views.addtask, name = "Add"),
    path('show/', views.showtask, name = "Show"),
    path('delete/<str:id>', views.deletetask, name = "Delete"),
    path('edit/<str:id>', views.edittask, name = "Edit"), 
    path('complete/<str:id>', views.completetask, name = "Complete"), 
   
]

