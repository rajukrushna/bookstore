from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)