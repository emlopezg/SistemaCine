"""SistemaCine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from inicio import views as iniviews
from django.views.static import serve
from stock import views as stviews
from stock import models as stomod
from django.conf import settings
from productos.views import ComboList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main$', iniviews.main, name='main'),
    url(r'^$', iniviews.main, name='main'),
    url(r'^login', views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^logout$', views.logout, {'template_name': 'index.html'}, name="logout"),
    url(r'^registrar', iniviews.newUser, name = "registrar"),
    url(r'^compra', stviews.Reserva, name = "compra"),
    #url(r'^booking/', include('booking.urls')),
    #url(r'^imprimirticket/(?P<reservaasiento>[^/]+)/$', stviews.report, name = "ticket"), ?P<product>\w+)/$
    #url(r'^imprimirticket/$', stviews.report, name = "ticket"),
    #url(r'^imprimirticket/$', stomod.report, name = "ticket"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

