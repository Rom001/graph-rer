import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données
stations = pd.read_csv('rera.csv', sep=';')

# Création du graphique
plt.figure(figsize=(10, 8))

# Dictionnaire pour stocker les correspondances entre les couleurs et les lignes RER
couleur_par_ligne = {}

# Traçage des stations
for index, row in stations.iterrows():
    # Calcul de la taille en fonction de l'affluence (vous pouvez ajuster le facteur d'échelle)
    taille_marqueur = row['trafic'] * 0.000002
    transparence = 0.5
    plt.plot(row['x'], row['y'], marker='o', color=row['color'], markersize=taille_marqueur, alpha=transparence)
    # Associez la couleur à la ligne RER dans le dictionnaire
    couleur_par_ligne[row['ligne']] = row['color']

# Traçage des connexions
for index, row in stations.iterrows():
    connexion = row['connexion']
    if not pd.isna(connexion):
        station_connectee = stations[stations['id_gares'] == connexion].iloc[0]
        plt.plot([row['x'], station_connectee['x']], [row['y'], station_connectee['y']], linestyle=row['style'], color=row['color'])

# Création de la légende personnalisée avec les couleurs des lignes RER
legende_personnalisee = []
for ligne, couleur in couleur_par_ligne.items():
    legende_personnalisee.append(plt.Line2D([0], [0], marker='o', color=couleur, label=f'Ligne {ligne}', linestyle=''))

# Afficher la légende personnalisée
plt.legend(handles=legende_personnalisee)

plt.title('Carte des Stations de RER à Paris')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.show()