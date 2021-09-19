from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EmployerForm
from .models import Employer
from .forms import DepartementForm
from .models import Departement

#Gestion des vues des employers 
# Create your views here.
def add(request):
    form = EmployerForm(request.POST or None)
    #employer = Employer.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form': form})

def details(request):
    employer = Employer.objects.all()
    return render(request, 'details.html', {'employer': employer})

def update(request, id):
    employer = Employer.objects.get(id=id)
    form = EmployerForm(request.POST, instance=employer)
    if form.is_valid():
       form.save()
       return HttpResponseRedirect('/details')
    return render(request, 'update.html', {'employer': employer})

def delete(request, id):
    form = Employer.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')


#Gestion des vues de departements 
# fonction d ajout
def addDepartement(request):
    form = DepartementForm(request.POST or None)
    #employer = Employer.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add_departement.html', {'form': form})

#fonction details departement 
def detailsDepartemnt(request):
    departement = Departement.objects.all()
    return render(request, 'details_departement.html', {'departement': departement})

#mise a jour departement
def updateDepartement(request, id):
    departement = Departement.objects.get(id=id)
    form = DepartementForm(request.POST, instance=departement)
    if form.is_valid():
       form.save()
       return HttpResponseRedirect('/details_departement')
    return render(request, 'update_departement.html', {'departement': departement})

# suppression d'un departement 

def deleteDepartement(request, id):
    form = Departement.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/details_departement')