from rest_framework import serializers
from .models import UserProfile, Hotel, HotelImage, Room, RoomImage, Review, Booking

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'user_role', 'phone_number', 'age']

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['id', 'hotel', 'hotel_image']

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'room', 'room_image']

class HotelSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True, source='hotelimage_set')

    class Meta:
        model = Hotel
        fields = [
            'id', 'hotel_name', 'owner', 'hotel_description', 'country',
            'city', 'address', 'hotel_stars', 'hotel_video',
            'created_date', 'hotel_images'
        ]

class RoomSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True, source='roomimage_set')

    class Meta:
        model = Room
        fields = [
            'id', 'room_number', 'hotel_room', 'room_type', 'room_status',
            'room_price', 'all_inclusive', 'room_description', 'room_images'
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_name', 'hotel', 'text', 'stars', 'parent']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'hotel_book', 'room_book', 'user_book', 'check_in',
            'check_out', 'total_price', 'status_book'
        ]


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()