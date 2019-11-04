from rest_framework import routers
from . import views
from .views import UserViewSet, OrderViewSet, BookViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'order', OrderViewSet)
router.register(r'book', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index', views.indexView, name="index")
]