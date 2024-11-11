from django.urls import path

from .views import (

    UserProfileViewSet, HotelViewSet, HotelImageViewSet,
    RoomViewSet, RoomImageViewSet, ReviewViewSet, BookingViewSet, ImageUploadView
)

urlpatterns = [



    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='userprofile_detail'),


    path('', HotelViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
    path('hotels/<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='hotel_detail'),


    path('hotel-images/', HotelImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotelimage_list'),
    path('hotel-images/<int:pk>/', HotelImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='hotelimage_detail'),


    path('rooms/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
    path('rooms/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='room_detail'),


    path('room-images/', RoomImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='roomimage_list'),
    path('room-images/<int:pk>/', RoomImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roomimage_detail'),


    path('reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review_detail'),


    path('bookings/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
    path('bookings/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking_detail'),

    path('upload-image/', ImageUploadView.as_view(), name='upload_image'),
]
