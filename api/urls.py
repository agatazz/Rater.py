from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ServiceViewSet,RatingViewSet,UserViewSet
router=routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('services',ServiceViewSet)
router.register('ratings',RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
