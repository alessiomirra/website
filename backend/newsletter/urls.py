from django.urls import path 
from . import views 

urlpatterns = [
    path('subscribe/<str:email>/', views.SubscribeView.as_view(), name='subscribe'),
    path('unsubscribe/<str:email>/', views.UnsubscribeView.as_view(), name='unsubscribe'),
]