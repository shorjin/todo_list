from django.urls import path
from . import views

urlpatterns = [
    # load page of the app that will be sending the index.html file
    path('', views.index, name='index'),  # Add a comma here
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('delete_completed/', views.delete_completed, name='delete_completed')
    
]