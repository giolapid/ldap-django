from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ldap/$', views.ldap, name="ldap"),
    url(r'^host/$', views.host, name="host"),
    url(r'^ldap/result/$', views.ldapresult, name="ldap_result"),
]
