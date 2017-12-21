from django.contrib import admin
from django.urls import path
from axeljacobsen.views import *

home = HomePage()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
]
