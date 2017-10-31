from django.conf.urls import url

from . import views

app_name = 'budget'
urlpatterns = [
    #  url(r'^$', views.IndexView.as_view(), name='index')
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/add_item/$', views.DetailView.add_item),
    url(r'^(?P<pk>[0-9]+)/delete_item/$', views.DetailView.delete_item),
    #  url(r'^(?P<Budget_id>[0-9]+)/add_transactions/$', views.add_transactions),
    url(r'^(?P<Budget_id>[0-9]+)/add_income/$', views.add_income),
    url(r'^(?P<Budget_id>[0-9]+)/add_expense/$', views.add_expense),
]
