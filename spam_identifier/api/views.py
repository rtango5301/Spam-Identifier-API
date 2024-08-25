from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

from .models import Contact
from .serializers import ContactSerializer
from django.db.models import Q
from django.http import HttpResponse

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SearchByNameView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        query = self.request.query_params.get('name', '')
        return Contact.objects.filter(
            Q(name__istartswith=query) | Q(name__icontains=query)
        ).order_by('-name__istartswith')

class SearchByPhoneView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        query = self.request.query_params.get('phone', '')
        return Contact.objects.filter(phone_number=query)
    
def home_view(request):
    return HttpResponse("Welcome to the Spam Identifier API!")