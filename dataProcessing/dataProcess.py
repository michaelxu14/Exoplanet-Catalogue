import math
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

from planet import Planet


class DataProcess:
    def __init__(self, df):
        self.df = df
        self.planetList = []


    def processDataFromFile(self):
        self.df = pd.read_csv("exocat_project/hwc.csv")


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

   

#test stuff
def main():
    data_process = DataProcess(pd.DataFrame())
    data_process.processDataFromFile()
    planet_list = data_process.getPlanetList()
    for planet in planet_list:
        print(planet.__str__())


    data_process.sortByMostHabitable()
    print("\nTop 5 Most Habitable Exoplanets:")
    data_process.plotHabitabilityVSDistance()


if __name__ == "__main__":
    main()
    
        


    
