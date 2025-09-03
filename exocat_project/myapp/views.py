

from django.shortcuts import render
import pandas as pd
from myapp.models import DataProcess

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def data(request):
    dataProcess = DataProcess(pd.DataFrame())
    dataProcess.processDataFromFile()
    planet_list = dataProcess.getPlanetList()
    dataProcess.sortByMostHabitable()  

    return render(request, "data.html", {"planets": planet_list})

