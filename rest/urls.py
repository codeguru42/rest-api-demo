from django.urls import path, include
from rest_framework import routers

from rest import views

router = routers.DefaultRouter()
router.register(r'baseball_cards', views.BaseballCardViewSet)

urlpatterns = [
    path('', include(router.urls))
]
