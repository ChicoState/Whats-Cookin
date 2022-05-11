from django.urls import path
from . import views

urlpatterns = [
	# Dynamic urls
	path('dashboard', views.dashboard, name="dashboard"),
	path('createFridge/', views.createFridge, name="createFridge"),
	path('updateFridge/<str:pri_key>/', views.updateFridge, name="updateFridge"),
	path('deleteFridge/<str:pri_key>/', views.deleteFridge, name="deleteFridge"),
	
]