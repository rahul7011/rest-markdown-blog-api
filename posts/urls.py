from django.urls import path
from .views import PostDetailView, PostListView,PostCreateView,PostUpdateView

app_name="posts"
urlpatterns = [
    path('posts/',PostListView.as_view(),name='post-list'),
    path('posts/create/',PostCreateView.as_view(),name='post-create'),
    path('posts/<slug>',PostDetailView.as_view(),name='post-detail'),
    path('posts/<slug>/update',PostUpdateView.as_view(), name='post-update')
]
