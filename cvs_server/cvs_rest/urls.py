from django.conf.urls import url
from cvs_rest import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^login/$', views.CustomAuthToken.as_view()),
    url(r'^signup/$', views.sign_up),
    url(r'products/$', views.ProductList.as_view()),
    url(r'products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^reviews/$', views.ReviewList.as_view()),
    url(r'^reviews/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view()),
    url(r'comments/$', views.CommentList.as_view()),
    url(r'comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    url(r'recipes/$', views.RecipeList.as_view()),
    url(r'recipes/(?P<pk>[0-9]+)/$', views.RecipeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
