import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
stations = pd.read_csv('rere.csv', sep=';')

# Création du graphique
plt.figure(figsize=(10, 8))

# Tracer les stations
for index, row in stations.iterrows():
    plt.plot(row['x'], row['y'], marker='o', color=row['color'])




for index, row in stations.iterrows():
    connexion = row['connexion']
    if not pd.isna(connexion):
        station_connectee = stations[stations['id_gares'] == connexion].iloc[0]
        plt.plot([row['x'], station_connectee['x']], [row['y'], station_connectee['y']], linestyle=row['style'], color=row['color'])



plt.title('Carte des Stations de RER à Paris')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()


