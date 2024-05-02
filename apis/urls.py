from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GeeksViewSet, ApisViewSet

router = DefaultRouter()
router.register(r'geeks', GeeksViewSet, basename='geeks')
router.register(r'apis', ApisViewSet, basename='apis')

urlpatterns = [
    path('', include(router.urls)),
]