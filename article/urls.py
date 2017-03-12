from django.conf.urls import url

from .views import article_list
from .views import article_create
from .views import article_detail

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)',article_list),
    #block_id这一板块下面的文章列表,URL模式为/article/list/所属板块ID
    url(r'^create/(?P<block_id>\d+)',article_create),
    url(r'^detail/(?P<article_id>\d+)',article_detail),
]