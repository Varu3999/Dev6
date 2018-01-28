from django.contrib import admin
from django.conf.urls import include ,url
from . import views
urlpatterns = [
    url('^login/$', views.login , name='login'),
    url('^loggedin/$',views.loggedin , name = 'loggedin'),
    url('^logout/$',views.logout, name = 'logout'),
    url('^invalid/$', views.invalid, name = 'invalid'),
    url('^auth/$',views.auth, name = 'auth'),
    url('^register/$', views.register, name ='register'),
    url('^success/$', views.success, name = 'success'),
    url('^home/$', views.home, name = 'home')
]
