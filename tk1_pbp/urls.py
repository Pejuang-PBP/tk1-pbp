"""tk1_pbp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http.response import HttpResponseRedirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from faq import views
from rest_framework import routers

import landing_page.urls as landing_page
import dashboard_donor.urls as dashboard_donor
import dashboard_pencari_donor.urls as dashboard_pencari_donor
import faq.urls as faq
import form_donor.urls as form_donor
import form_pencari_donor.urls as form_pencari_donor
import lokasi_donor.urls as lokasi_donor

import authentication.urls as authentication

from django.contrib.auth import logout

router = routers.DefaultRouter(trailing_slash=False)
router.register('tanyadetails', views.Tanya)


def signout(request):
    logout(request)
    return HttpResponseRedirect("/")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(landing_page)),
    path("dashboard-donor/", include(dashboard_donor)),
    path("dashboard-pencari/", include(dashboard_pencari_donor)),
    path("form-donor/", include(form_donor)),
    path("form-pencari-donor/", include(form_pencari_donor)),
    path("signout", signout),
    path("lokasi-donor/", include(lokasi_donor)),
    path("faq/", include(faq)),
    path("auth/", include(authentication)),
    path("tanya/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
