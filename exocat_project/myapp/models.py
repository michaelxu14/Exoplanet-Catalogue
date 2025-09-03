from django.db import models
import math
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

# Create your models here.

class DataProcess:
    def __init__(self, df):
        self.df = df
        self.planetList = []


    def processDataFromFile(self): 
        self.df = pd.read_csv("hwc.csv")

        self.df = self.df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

        # Replace NaN values with 0
        self.df = self.df.replace({pd.NA: 0, float('nan'): 0, None: 0})
        self.df = self.df.fillna(0)

        for index, row in self.df.iterrows():
            planet = Planet(
                name=row['P_NAME'],
                type=row['P_TYPE'],
                detectionMethod=row['P_DETECTION'],
                mass=row['P_MASS'],
                radius=row['P_RADIUS'],
                flux=row['P_FLUX'],
                tSurf=row['P_TEMP_SURF'],
                period=row['P_PERIOD'],
                age = row['S_AGE'],
                distance=row['S_DISTANCE'],
                esi=row['P_ESI']
            )
            self.planetList.append(planet)


    def getPlanetList(self):
        return self.planetList

    def getPlanetByName(self, name):
        for planet in self.planetList:
            if planet.get_name() == name:
                return planet
        return None
    
    def sortByMostHabitable(self):
        self.planetList.sort(key=lambda p: p.get_esi(), reverse=True)

    #for debug

    def plotHabitabilityVSDistance(self):
        valid = [p for p in self.planetList
                if isinstance(p.get_esi(), (int, float)) and not math.isnan(p.get_esi())]

        if not valid:
            print("No planets with valid ESI found.")
            return

        names = [p.get_name() for p in valid]
        esi = [p.get_esi() for p in valid]
        distance = [p.get_distance() for p in valid]

        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(distance, esi, c=esi, cmap="viridis", s=50, alpha=0.7, edgecolors="k")
        plt.colorbar(scatter, label="Earth Similarity Index (ESI)")
        plt.xlabel("Distance (light years)")
        plt.ylabel("Earth Similarity Index (0–1)")
        plt.title("Exoplanet Habitability (ESI vs Distance)")

        #best chance = weighted avg?

        mostEarthlike = max(valid, key=lambda p: p.get_esi())
        plt.scatter(mostEarthlike.get_distance(), mostEarthlike.get_esi(),
                    color="red", edgecolors="black", s=120,
                    label=f"Most Earth-like: {mostEarthlike.get_name()}")
        plt.legend()
        plt.show()


#add more stuff later


class Planet:
    def __init__(self, name, type, detectionMethod, mass, radius, flux, tSurf, period, age, distance, esi):
        self.name = name
        self.type = type
        self.detectionMethod = detectionMethod
        self.mass = mass
        self.radius = radius
        self.flux = flux
        self.tSurf = tSurf
        self.period = period
        self.age = age
        self.distance = distance
        self.esi = esi

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_flux(self):
        return self.flux

    def set_flux(self, flux):
        self.flux = flux

    def get_tSurf(self):
        return self.tSurf

    def set_tSurf(self, tSurf):
        self.tSurf = tSurf

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def get_esi(self):
        return self.esi

    def set_esi(self, esi):
        self.esi = esi

    def __str__(self):
        return f"Planet(name={self.name}, type={self.type}, mass={self.mass}, radius={self.radius}, flux={self.flux}, tSurf={self.tSurf}, period={self.period}, distance={self.distance}, esi={self.esi})"