"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from billing.views import PriceView, PorsServiceView, LineServiceView, TotalCostReceiptView, TotalCostReceiptPerServiceView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('price/', PriceView.as_view(), name='price_view'),

    path('pors/', PorsServiceView.as_view()),
    path('line/', LineServiceView.as_view()),

    path('receipt/', TotalCostReceiptView.as_view()),
    path('receipt/<str:service_name>', TotalCostReceiptPerServiceView.as_view())


]
