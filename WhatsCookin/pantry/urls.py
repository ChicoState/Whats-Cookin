from django.urls import path
from . import views

urlpatterns = [
	# Dynamic urls
	path('dashboard/<str:pri_key>/', views.dashboard, name="dashboard"),
	path('createFridge/<str:pri_key>/', views.createFridge, name="createFridge"),
	path('updateFridge/<str:cust_key>/<str:fri_key>', views.updateFridge, name="updateFridge"),
	path('deleteFridge/<str:cust_key>/<str:fri_key>', views.deleteFridge, name="deleteFridge"),
	
]