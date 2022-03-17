from django.urls import path, re_path

from .views import (
    # index_view,
    post_detail_view,
    post_create_view,
    post_update_view,
    post_delete_view,
    # about_view,
    AboutView,
    IndexView
)


app_name = 'blog'
urlpatterns = [
    # path('', index_view, name='index'),
    path('', IndexView.as_view(), name='index'),
    # path('about/', about_view, name='about'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/create/', post_create_view, name='create'),
    re_path(r'^post/(?P<slug>[\w-]+)/$', post_detail_view, name='detail'),
    re_path(r'^post/(?P<slug>[\w-]+)/edit/$', post_update_view, name='update'),
    re_path(r'^post/(?P<slug>[\w-]+)/delete/$', post_delete_view, name='delete'),
]