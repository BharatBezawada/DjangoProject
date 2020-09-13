from django.conf.urls import url
from django.urls import include, path
from . import views
from django.contrib.auth import views as v1

urlpatterns = [

    url(r'^$', views.index, name='home-page'),
    # url(r'^$', v1.LoginView.as_view(template_name='ClaimsApp/login.html'), name="login"),
    url(r'add_data/', views.add_data, name='add_data'),
    url(r'app_data/', views.app_data, name='app_data'),
    url(r'all_buyers/', views.buyer_data, name='buyer_data'),
    url(r'export/', views.export, name="export"),
    url(r'search/', views.search, name="search"),
    url(r'limits_upload/', views.CreditLimit, name="credit_limits_upload"),
    url(r'credit_limit_check/', views.search_limit, name="credit_limit_check"),

]
