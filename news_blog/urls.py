from django.urls import path
from news_blog import views


urlpatterns = [
    path('news_blog/', views.news_blog_view),
    path('hello/', views.hello_view),
]