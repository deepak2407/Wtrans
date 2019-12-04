from django.urls import path
from. import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('buses',views.buses,name='buses'),
    path('Route',views.Route,name='Route')
]
