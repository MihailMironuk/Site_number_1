from django.urls import path
from books import views

urlpatterns = [
    path('info/', views.info_view),
    path('hobbies/', views.hobbies_view),
    path('time/', views.current_time_view),
    path('random/', views.random_numbers_view),
]