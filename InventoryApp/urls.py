from django.urls import path, include
from rest_framework.routers import DefaultRouter
from InventoryApp import views

from rest_framework_simplejwt.views import (
	TokenObtainPairView,
	TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'locations', views.LocationViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
