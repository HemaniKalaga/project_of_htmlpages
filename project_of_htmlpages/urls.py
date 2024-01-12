"""
URL configuration for project_of_htmlpages project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('internal/',internal,name='internal'),
    path('HtmlLoginForm/',HtmlLoginForm,name='HtmlLoginForm '),
    path('anchortag/',anchortag,name='anchortag'),
    path('bootstrap_grid/',bootstrap_grid,name='bootstrap_grid'),
    path('InlineExternal/',InlineExternal,name='InlineExternal'),
    path('selectors/',selectors,name='selectors'),
    path('table/',table,name='table'),
    path('css1/',css1,name='css1'),
    path('PrimeAndComposite/',PrimeAndComposite,name='PrimeAndComposite'),
    path('perfect/',perfect,name='perfect'),
    path('booking/',booking,name='booking'),
    

]
