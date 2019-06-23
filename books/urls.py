from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Bookstore API')

router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
]
