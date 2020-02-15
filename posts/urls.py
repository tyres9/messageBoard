from django.urls import path
from .views import HomePageView,UserPostListView,PostCreateView,PostDeleteView


urlpatterns = [
    path('',HomePageView.as_view(),name = 'home'),  
    path('user/<str:username>/',UserPostListView.as_view(),name = 'user-posts'),  
    path('post/new/',PostCreateView.as_view(),name = 'post-create'), 
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post-delete'),
]
