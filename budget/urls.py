from django.conf.urls import url

from . import views

app_name = 'budget'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_item/$', views.IndexView.add_item),
    url(r'^delete_item/$', views.IndexView.delete_item),
    url(r'^add_transactions/$', views.IndexView.add_transactions),
]
