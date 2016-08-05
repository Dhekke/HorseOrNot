from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit/(?P<profile_id>[0-9]+)$', views.submit, name='submit'),
]
