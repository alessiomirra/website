from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 

from newsletter.models import Subscriber 
# Create your views here.


class SubscribeView(APIView):
    def get(self, request, *args, **kwargs):
        email = self.kwargs.get('email')
        if email: 
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created: 
                return Response({'message': 'Successfully Enrolled!', 'type':'success'}, status=status.HTTP_201_CREATED)
            else: 
                return Response({'message': 'You are already subscribed to the newsletter.', 'type': 'error'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UnsubscribeView(APIView):
    def get(self, request, *args, **kwargs):
        email = self.kwargs.get('email')
        if email:
            try: 
                subscriber = Subscriber.objects.get(email=email)
                subscriber.delete() 
                return Response({'message': 'Unsubscribing successful', 'type':'success'}, status=status.HTTP_200_OK)
            except Subscriber.DoesNotExist:
                return Response({'message': 'You are not subscribed to the newsletter', 'type': 'error'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
