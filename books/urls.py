from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)