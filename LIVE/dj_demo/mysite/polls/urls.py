from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = staticfiles_urlpatterns()
urlpatterns += [url(r'^.*$', views.index, name='index'),]

#http://162.243.219.59/
