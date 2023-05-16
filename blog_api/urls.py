from .views import PostList, PostListDetailfilter, CreatePost, EditPost, AdminPostDetail, DeletePost, \
    PostDetailId, PostDetailSlug
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('<int:pk>/', PostDetailId.as_view(), name='detailpost'),
    path('<str:pk>/', PostDetailSlug.as_view(), name='detailpost'),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]
