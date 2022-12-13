from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('save/<path:password>', save, name='save'),
    path('delete/<int:pk>', delete, name='delete'),

]