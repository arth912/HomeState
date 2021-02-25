from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('buy_property',views.buy_property,name='buy_property'),
    path('sell_property',views.sell_property,name='sell_property'),
    path('prediction',views.prediction,name='prediction'),
    path('result/',views.result,name='result'),
    path('agent',views.agent,name='agent'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),

]