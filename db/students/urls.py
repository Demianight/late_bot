from rest_framework.routers import SimpleRouter
from .views import StudentViewSet
from django.urls import path, include


router = SimpleRouter()

router.register(
    'students',
    StudentViewSet,
    'students'
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken'))
]
