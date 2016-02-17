from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/$', views.login_redirect, name='login'),
    url(r'^authenticate-user/$', views.authenticate_user, name='authenticate'),
]
