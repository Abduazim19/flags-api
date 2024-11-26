# flags/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlagViewSet

router = DefaultRouter()
router.register(r'flags', FlagViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
