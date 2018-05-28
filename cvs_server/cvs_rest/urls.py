from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cvs_rest import views

urlpatterns = [
    url(r'^reviews/$', views.add_review),
    url(r'^reviews/(?P<pk>[0-9]+)/$', views.review_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)