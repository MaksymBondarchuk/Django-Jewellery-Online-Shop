"""Lab1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import Shop.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', Shop.views.home),
    url(r'^home', Shop.views.home),

    url(r'^order', Shop.views.order),
    url(r'^complete', Shop.views.complete),

    #  Filtration
    url(r'^metal/([^/]+)/(true|false)', Shop.views.metal),
    url(r'^(fineness|weight|price)/([a-z]+)/([\d,.-]+)', Shop.views.update_filter),

    url(r'^buy/([^/]+)/([\d]+)', Shop.views.buy),
    url(r'^remove/([^/]+)', Shop.views.remove),
]
