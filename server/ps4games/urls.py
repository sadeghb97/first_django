from django.urls import path
from ps4games import views

urlpatterns = [
    path('add_game/', views.add_game),
    path('get_games/', views.get_games),
    path('up_del_get_game/<int:pk>/', views.up_del_get_game),
    path('search_game/', views.search_game)
]