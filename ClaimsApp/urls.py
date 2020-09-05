
from django.conf.urls import url
from django.urls import include, path
from .import views

urlpatterns = [
    url(r'^$', views.index, name='home-page'),
    url(r'add_data/', views.add_data, name='add_data'),
    url(r'app_data/', views.app_data , name='app_data'),
    url(r'all_buyers/', views.buyer_data, name='buyer_data'),
    url(r'export/', views.export , name="export"),
    url(r'search/', views.search , name="search"),


]