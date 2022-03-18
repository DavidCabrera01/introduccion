from nturl2path import url2pathname
from django.urls import URLPattern, path
from .views import BlogListView

app_name='blog'

urlpattern = {
    path('',BlogListView.as_view(),name='home')
}