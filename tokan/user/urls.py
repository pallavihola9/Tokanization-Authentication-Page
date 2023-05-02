from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
 
urlpatterns = [
         path('', views.index, name ='index'),
]