from django.urls import path
from .views import StatusViewset
from rest_framework.routers import DefaultRouter

# status/ -> List, Create => GET, POST
# status/<id>/ -> Details, Delete, Update => GET, DELETE, PUT/PATCH

router = DefaultRouter()
router.register(r"status", StatusViewset, basename="status")

urlpatterns = [] + router.urls
