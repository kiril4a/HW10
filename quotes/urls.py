from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quotes-home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('add_author/', views.add_author, name='add-author'),
    path('add_quote/', views.add_quote, name='add-quote'),
    path('author/<int:pk>/', views.author_detail, name='author-detail'),
]
