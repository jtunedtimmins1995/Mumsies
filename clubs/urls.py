from django.conf.urls import url
from . import views



urlpatterns = [
    
    url(r'^$', views.home),
    url('^login/$', views.login_view),
    url('^logout/$', views.logout_view),
    url(r'^createUser/$', views.createUser),
    url(r'^createDeal/$', views.CreateDeal_view),
    url(r'^currentDeal/$', views.CurrentDeal_view),
    url(r'^editDeal/(?P<id>\d+)/$', views.EditDeal_view, name = "edit_deal"),
    url(r'^replicateDeal/(?P<id>\d+)/$', views.ReplicateDeal_view, name = "replicate_deal"),
    ]