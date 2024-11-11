from django_filters import rest_framework as filters
from .models import Room

class RoomFilter(filters.FilterSet):
    room_price_gte = filters.NumberFilter(field_name="room_price", lookup_expr='gte', label="Room price is greater than")
    room_price_lte = filters.NumberFilter(field_name="room_price", lookup_expr='lte', label="Room price is less than")

    class Meta:
        model = Room
        fields = {
            'room_type': ['exact'],
            'room_status': ['exact'],
            'all_inclusive': ['exact'],
        }

import django_filters
from .models import Hotel


class HotelFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains", label="Country")
    city = django_filters.CharFilter(field_name="city", lookup_expr="icontains", label="City")
    hotel_stars = django_filters.NumberFilter(field_name="hotel_stars", lookup_expr="exact", label="Hotel stars")

    class Meta:
        model = Hotel
        fields = ['country', 'city', 'hotel_stars']