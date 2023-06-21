from django.urls import path
from my_app import views


app_name ='myapp'




urlpatterns = [
    path('', views.home, name ='home'),
    path('menu/', views.menu, name ='menu'),
    path('services/', views.services, name ='services'),
    path('about/', views.about, name ='about'),
    path('contact/', views.contact, name ='contact'),

    path('<slug:category_slug>/', views.pizza_list, name ='pizza_list_by_category'),
    path('<int:id>/<slug:slug>/', views.pizza_detail, name ='pizza-detail'),


]