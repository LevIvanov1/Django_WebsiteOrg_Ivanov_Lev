from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('news/', views.news_list, name='news_list'),
        path('contact/', views.contact, name='contact'),
        path('register/', views.register, name='register'),
        path('profile/', views.profile, name='profile'),
        path('news/<int:news_id>/', views.news_detail, name='news_detail'),
        path('search/', views.news_search, name='news_search'),
        path('news/create/', views.news_create, name='news_create'),
        path('news/<int:news_id>/edit/', views.news_edit, name='news_edit'),
        path('news/<int:news_id>/delete/', views.news_delete, name='news_delete'),
        path('register/', views.register, name='register'),
]