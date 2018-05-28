from django.conf.urls import url
from cvs_rest import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^login/$', views.CustomAuthToken.as_view()),
    url(r'^signup/$', views.sign_up),
    url(r'^reviews/$', views.add_review),
    url(r'^reviews/(?P<pk>[0-9]+)/$', views.review_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
