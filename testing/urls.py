from django.urls import path
from . import views


urlpatterns= [
	path('', views.index , name='home'),
	path('create', views.createTodo , name='create'),
	path('DeleteTodo/<int:id>', views.DeleteTodo , name='delete'),
	path('UpdateTodo/<int:id>', views.UpdateTodo , name='update'),




]