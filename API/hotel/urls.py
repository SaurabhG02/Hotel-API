from django.urls import path,include
from hotel.views import HotelModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hotels',HotelModelViewSet)


urlpatterns = [
    path("",include(router.urls)),
]