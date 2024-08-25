from django.urls import path
from .views import RegisterUserView
from .views import SearchByNameView, SearchByPhoneView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('search/name/', SearchByNameView.as_view(), name='search_name'),
    path('search/phone/', SearchByPhoneView.as_view(), name='search_phone'),
]
