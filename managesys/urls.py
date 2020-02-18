from django.urls import path
from . import views

app_name="managesys"
urlpatterns = [
    path('create',views.create,name='creation'),
    path('instructions',views.instructions,name='instructions'),
    path('',views.index,name='index')
]