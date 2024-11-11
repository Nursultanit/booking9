from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Room
from .serializers import RoomSerializer
from .serializers import ImageSerializer
from .filters import RoomFilter
from .filters import HotelFilter
from rest_framework import viewsets, filters
from .models import UserProfile, Hotel, HotelImage, Room, RoomImage, Review, Booking
from .serializers import (
    UserProfileSerializer, HotelSerializer, HotelImageSerializer,
    RoomSerializer, RoomImageSerializer, ReviewSerializer, BookingSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():

            return Response({"message": "Изображение загружено успешно"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'user_role', 'phone_number']
    ordering_fields = ['username', 'age', 'user_role']


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = HotelFilter
    ordering_fields = ['hotel_stars']
    search_fields = ['name', 'city']


class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = RoomFilter
    ordering_fields = ['room_price']
    search_fields = ['room_type', 'room_status']


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
