"""defines URL patterns for users """

from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView


from . import views

urlpatterns = [
    # login page
    url(r'^login/$',LoginView.as_view(template_name = 'users\login.html'),name="login"),
    #logout 
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    #registration 
    url(r'^register/$', views.register, name='register'),
]