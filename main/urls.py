from django.urls import path

from main.apps import MainConfig
from main.views import test

app_name = MainConfig.name

urlpatterns = [
    path("", test, name='test'),
    # path('test/', test, name='test'),
 ]
