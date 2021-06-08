from django.urls import path
from .views import (
    StatusDetailUpdateDeleteView,
    StatusListCreateView,
)

# status/ -> List, Create => GET, POST
# status/<id>/ -> Details, Delete, Update => GET, DELETE, PUT/PATCH

urlpatterns = [
    path("status/", StatusListCreateView.as_view()),
    path("status/<id>/", StatusDetailUpdateDeleteView.as_view()),
]
