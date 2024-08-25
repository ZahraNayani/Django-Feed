# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from feed import views as feed_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', feed_views.home, name='home'),  # Home page
    path('feed/', include('feed.urls')),  # Route to feed app

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=False), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Registration URL
    path('register/', feed_views.register, name='register'),
]
