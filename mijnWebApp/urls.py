from django.urls import path
from . import views

app_name = 'mijnApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('momenten/<int:usr_id>', views.momenten, name='momenten'),
    path('product/<int:prod_id>', views.product, name='product'),
    path('contact/', views.contact, name='contact'),

    path('add_PoetsMoment/', views.PoetsMomentCreateView.as_view(), name='add_PoetsMoment'),
    path('upd_PoetsMoment/<int:pk>', views.PoetsMomentUpdateView.as_view(), name='upd_PoetsMoment'),
    path('del_PoetsMoment/<int:pk>', views.PoetsMomentDeleteView.as_view(), name='del_PoetsMoment'),
    path('list_PoetsMomenten/<int:usr_id>', views.momenten, name='list_PoetsMomenten'),
]
