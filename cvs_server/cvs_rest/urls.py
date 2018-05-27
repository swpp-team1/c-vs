from django.conf.urls import url
from cvs_rest import views


urlpatterns = [
    url(r'^login/$', views.CustomAuthToken.as_view()),
    url(r'^signup/$', views.sign_up),
]
