from django.conf.urls import path
from . import views as posts_views



#postList | index
#singlePosts
# contacts


urlpatterns = [
    path(r'^$', post_views.postList, name="list"),
    path(r'^single-post/$', post_views.singlePosts, name="single"),
    path(r'^contacts/$', post_views.contacts, name="contacts")
]