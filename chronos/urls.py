from django.urls import path
from chronos import views

app_name = 'chronos'

urlpatterns  = [
    path('', views.index, name='index'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_task/', views.add_task),
    path('toggle_completion/', views.toggle_completion),
]