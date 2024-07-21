from django.urls import include, path
from .views import CarViewSet, index
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('', index, name='home'),
    path('', include(router.urls)),
]
