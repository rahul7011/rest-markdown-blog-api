from django.urls import path
from .views import PostDetailView, PostListView,PostCreateView

app_name="posts"
urlpatterns = [
    path('posts/',PostListView.as_view(),name='post-list'),
    path('posts/create/',PostCreateView.as_view(),name='post-create'),
    path('posts/<slug>',PostDetailView.as_view(),name='post-detail')
]
