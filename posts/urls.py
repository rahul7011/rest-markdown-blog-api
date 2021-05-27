from django.urls import path
from .views import PostDetailView, PostListView

app_name="posts"
urlpatterns = [
    path('posts/',PostListView.as_view(),name='post-list'),
    path('posts/<slug>',PostDetailView.as_view(),name='post-detail')
]
