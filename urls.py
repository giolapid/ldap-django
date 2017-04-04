from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ldap_result/$', views.ldapresult, name="ldap_result"),
    url(r'^host_result/$', views.hostresult, name="host_result")
]
