from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .serializers import EmailSerializer
from django.utils.decorators import method_decorator


class EmailView(APIView):
   def post(self, request):
       serializer = EmailSerializer(data=request.data)
       if serializer.is_valid():
           message = serializer.validated_data['message']
           send_mail('New message', message, 'from@example.com', ['folayanjoey@gmail.com'])
           return Response({'status': 'Email sent'}, status=200)
       return Response(serializer.errors, status=400)
