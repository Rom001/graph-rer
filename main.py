import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
stations = pd.read_csv('rere.csv', sep=';')


# Création du graphique
plt.figure(figsize=(10, 8))
for ligne in stations['ligne'].unique():
    ligne_data = stations[stations['ligne'] == ligne]
    plt.plot(ligne_data['x'], ligne_data['y'], marker='o', label=ligne)

plt.title('Carte des Stations de RER à Paris')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()

