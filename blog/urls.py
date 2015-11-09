from django.conf.urls import include, url
from . import views
# from .blog_urls import urlpatterns as blog_urls

urlpatterns = [
	# url(r'^$', )
	url(r'^blog/', include('blog.blog_urls')),
	# url(r'^', include(blog_urls)),
]
