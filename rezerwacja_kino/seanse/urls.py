"""
URL configuration for rezerwacja_kino project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path

from seanse.views import SeanseListView, SeanseDetailView, RezerwacjaDetailView, create_reservation

urlpatterns = [
    path("seanse/", SeanseListView.as_view(), name="lista-seansow"),
    path("seanse/<int:pk>/", SeanseDetailView.as_view(), name="szczegoly-seansow"),
    path("seanse/<int:pk>/rezerwuj", create_reservation, name="rezerwuj"),
    path("rezerwacje/<int:pk>",RezerwacjaDetailView.as_view(), name="szczegoly-rezerwacji"),
]