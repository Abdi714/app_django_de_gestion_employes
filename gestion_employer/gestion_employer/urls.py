"""gestion_employer URL Configuration

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
from django.urls import path
from gestion_des_employer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add', views.add, name="add"),
    path('', views.details, name="details"),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('add_departement', views.addDepartement, name="add_departement"),
    path('details_departement', views.detailsDepartemnt, name="details_departement"),
    path('update_departement/<int:id>', views.updateDepartement, name='update_departement'),
    path('delete_departement/<int:id>', views.deleteDepartement, name='delete_departement'),
]
