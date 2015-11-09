from django.conf.urls import include, url
from . import views
# from .blog_urls import urlpatterns as blog_urls

urlpatterns = [
	url(r'^$', views.timetable_landing, name='home'),
	url(r'^blog/', include('blog.blog_urls')),
	url(r'^about/?$', views.timetable_about, name='about'),
]
