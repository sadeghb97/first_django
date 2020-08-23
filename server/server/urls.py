from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
    path('ps4games/', include('ps4games.urls')),
    path('api_token_auth/', views.obtain_auth_token),
]
