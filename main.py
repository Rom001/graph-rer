import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
stations = pd.read_csv('rere.csv', sep=';')

# Création du graphique
plt.figure(figsize=(10, 8))

# Tracer les stations
for index, row in stations.iterrows():
    plt.plot(row['x'], row['y'], marker='o', color='purple')




for index, row in stations.iterrows():
    connexion = row['connexion']
    if not pd.isna(connexion):
        station_connectee = stations[stations['id'] == connexion].iloc[0]
        plt.plot([row['x'], station_connectee['x']], [row['y'], station_connectee['y']], color='purple')



plt.title('Carte des Stations de RER à Paris')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend("E", fontsize=12)
plt.show()


