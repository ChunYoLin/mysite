from django.conf.urls import url

from . import views

app_name = 'budget'
urlpatterns = [
    #  url(r'^$', views.IndexView.as_view(), name='index')
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<Year_name>[0-9]+)/$', views.YearView.as_view(), name='year'),
    url(r'^asset_transfer$', views.asset_transfer),
    url(r'^(?P<Year_name>[0-9]+)/(?P<Budget_id>[0-9]+)/$', views.BudgetView.as_view(), name='budget'),
    url(r'^(?P<Year_name>[0-9]+)/(?P<Budget_id>[0-9]+)/add_debt/$', views.BudgetView.add_debt),
    url(r'^(?P<Year_name>[0-9]+)/(?P<Budget_id>[0-9]+)/pay_debt/$', views.BudgetView.pay_debt),
    url(r'^(?P<Year_name>[0-9]+)/(?P<Budget_id>[0-9]+)/delete_item/$', views.BudgetView.delete_item),
    url(r'^(?P<Year_name>[0-9]+)/(?P<Budget_id>[0-9]+)/add_income/$', views.BudgetView.add_income),
    url(r'^(?P<Year_name>[0-9]+)/(?P<Budget_id>[0-9]+)/add_expense/$', views.BudgetView.add_expense),
]
