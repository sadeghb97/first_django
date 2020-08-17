from django.urls import path
from first_app import views

urlpatterns = [
    path('helloworld', views.hello_world)
]