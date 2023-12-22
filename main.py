import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Chargement des données
data = {
    'nom': ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F'],
    'ligne': ['A', 'A', 'A', 'B', 'B', 'C'],
    'x': np.random.rand(6),
    'y': np.random.rand(6)
}
stations = pd.DataFrame(data)
# Création du graphique
plt.figure(figsize=(10, 8))
for ligne in stations['ligne'].unique():
    ligne_data = stations[stations['ligne'] == ligne]
    plt.plot(ligne_data['x'], ligne_data['y'], marker='o', label=f'Ligne {ligne}')

plt.title('Carte des Stations de RER à Paris')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()
