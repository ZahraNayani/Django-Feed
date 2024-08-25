from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
    path('post_message/', views.post_message, name='post_message'),
    path('post_comment/<int:message_id>/', views.post_comment, name='post_comment'),
    path('like_message/<int:message_id>/', views.like_message, name='like_message'),
]
