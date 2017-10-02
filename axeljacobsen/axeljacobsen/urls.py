from django.conf.urls import url
from django.contrib import admin

from axeljacobsen.views import HomePage

home = HomePage()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.home, name='home')
]
