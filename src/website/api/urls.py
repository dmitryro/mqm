from django.conf.urls import include, patterns, url
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^_auth/', include('rest_framework.urls', namespace='rest_framework')),
)
