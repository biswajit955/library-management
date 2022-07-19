from unicodedata import name
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path
from library import views

urlpatterns = [
    path('register/', views.register , name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='library/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('', views.BookListView.as_view(), name='book-view'),
    path('book_create', login_required(views.BookCreateView.as_view(), login_url='login'), name='book-create'),
    path('book/<int:pk>/update', login_required(views.BookUpdateView.as_view(), login_url='login'), name='book-update'),
    path('book/<int:pk>/delete', login_required(views.BookDeleteView.as_view(), login_url='login'), name='book-delete'),

]