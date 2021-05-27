from django.urls import path
from . import views

app_name = 'mijnApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:prod_id>', views.product, name='product'),
    path('contact/', views.contact, name='contact'),
]
