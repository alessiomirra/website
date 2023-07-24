from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status 
from rest_framework import viewsets 
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated 
from django.core.mail import BadHeaderError,send_mail
from django.template.loader import render_to_string
from cars.models import Car, CompanyInfo 
from cars.api.serializers import CarSerializer, InfoSerializer 
from cars.api.pagination import CustomPagination

##### 

class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('-id')
    serializer_class = CarSerializer
    lookup_field = 'slug' 
    pagination_class = CustomPagination 
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else: 
            permission_classes = [] 
        return [permission() for permission in permission_classes]


class ShowCase(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer 

    def get_queryset(self):
        return Car.objects.filter(
            showcase = True 
        ).order_by('-id')


class ContactForm(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data 
        first_name = data["firstName"]
        last_name = data["lastName"]
        email = data["email"]
        phone_number = data["phoneNumber"]
        subject = data["subject"]
        message = data["message"]
        car = data["car"]

        object = f"A new email for '{subject}' from {first_name} {last_name}"

        msg_plain = render_to_string('email.txt',{'first_name':first_name, "last_name":last_name, "email":email, "phone_number": phone_number, "subject":subject, "message":message, "car":car})
        msg_html = render_to_string('email.html', {'first_name':first_name, "last_name":last_name, "email":email, "phone_number": phone_number, "subject":subject, "message":message, "car":car})

        try:
            send_mail(
                from_email= email, 
                subject=object, 
                msg_plain = msg_plain,
                message=message, 
                msg_html = msg_html, 
                recipient_list = ['carhub@info.com']
            )
        except BadHeaderError:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        print(data)
        return Response(status=status.HTTP_200_OK)

class AvailableCarsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cars = Car.objects.all()
        car_list = []
        if len(cars) > 0:
            for i in cars:
                element = f"{i.make} {i.model}, {i.version}"
                car_list.append(element)
            return Response(car_list, status=status.HTTP_200_OK)
        else: 
            return Response({'message':'No cars available'}, status=status.HTTP_200_OK)


class GetCompanyInfo(APIView):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        object = CompanyInfo.objects.get(id=id)
        serializer = InfoSerializer(object)
        return Response(serializer.data)