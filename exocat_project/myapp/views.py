

from django.shortcuts import render
import pandas as pd
from dataProcessing.dataProcess import DataProcess

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def data(request):
    data_process = DataProcess(pd.DataFrame())
    data_process.processDataFromFile()
    planet_list = data_process.getPlanetList()
    data_process.sortByMostHabitable()  # optional: sort planets

    return render(request, "home.html", {"planets": planet_list})

