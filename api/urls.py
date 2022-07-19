
from django.urls import path
from api.views import OneBookAPI,AllBookAPI
from library import views

urlpatterns = [
    path('all', AllBookAPI.as_view() , name='all_book_api'),
    path('one/<int:pk>/', OneBookAPI.as_view() , name='one_book_api'),
]