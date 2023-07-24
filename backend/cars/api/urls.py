from django.urls import path, include 
from rest_framework import routers 
from cars.api import views 

######## 

router = routers.DefaultRouter()
router.register(r'cars', views.CarViewset)

urlpatterns = [
    path('', include(router.urls)), 
    path('showcase/', views.ShowCase.as_view(), name="showcase"), 
    path('contact/', views.ContactForm.as_view(), name="contact-form"), 
    path('available/', views.AvailableCarsAPIView.as_view(), name="available-cars"), 
    path('company-info/<int:pk>/', views.GetCompanyInfo.as_view(), name='company-info'), 
]