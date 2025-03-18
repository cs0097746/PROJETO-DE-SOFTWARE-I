from site_inf.views import index
from django.urls import path
 
app_name = 'site_inf'
 
urlpatterns = [
     path('', index, name='index'),
 ]