from django.urls import path

from .views import (
    index_view,
    post_detail_view,
    post_create_view,
    post_update_view,
    post_delete_view
)


app_name = 'blog'
urlpatterns = [
    path('', index_view, name='index'),
    path('post/<int:pk>/', post_detail_view, name='detail'),
    path('post/<int:pk>/update/', post_update_view, name='update'),
    path('post/<int:pk>/delete/', post_delete_view, name='delete'),
    path('post/create/', post_create_view, name='create'),
]