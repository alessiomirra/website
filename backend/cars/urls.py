from django.urls import path 
from cars import views 

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'), 
    path('showcase/', views.Showcase.as_view(), name="showcase-page"), 
    path('new-car/', views.NewCar.as_view(), name="new-car-page"), 
    path('update-car/<slug:slug>/', views.UpdateCarView.as_view(), name="update-car-page"), 
    path('remove-from-wishlist/<slug:slug>/', views.Remove.as_view(), name="remove-from-wishlist"), 
    path('delete-car/<slug:slug>/', views.DeleteCarView.as_view(), name='delete-car'),
    path('company-informations/', views.InfoesUpdateView.as_view(), name='company-infoes-page'),  
]