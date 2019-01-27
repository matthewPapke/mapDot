from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getBtcPrice', views.get_btc_price, name='get_btc_price'),
]