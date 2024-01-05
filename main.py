import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# Chargement des données
stations = pd.read_csv('rere.csv', sep=';')

def plot_rer():
    plt.figure(figsize=(10, 8))
    couleur_par_ligne = {}
    for index, row in stations.iterrows():
        if row['type'] == 'RER':
            plt.plot(row['x'], row['y'], marker='o', color=row['color'])
            couleur_par_ligne[row['res_com']] = row['color']


    for index, row in stations.iterrows():
        connexion = row['connexion']
        if not pd.isna(connexion):
            station_connectee = stations[stations['id_gares'] == connexion].iloc[0]
            if row['type'] == 'RER' and station_connectee['type'] == 'RER':
                plt.plot([row['x'], station_connectee['x']], [row['y'], station_connectee['y']], linestyle=row['style'], color=row['color'])

     # Création de la légende personnalisée avec les couleurs des lignes RER
    legende_personnalisee = []
    for ligne, couleur in couleur_par_ligne.items():
        legende_personnalisee.append(plt.Line2D([0], [0], marker='o', color=couleur, label=f'{ligne}', linestyle=''))

    plt.title('Carte des Stations de RER à Paris')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(handles=legende_personnalisee)
    plt.show()
    display(widgets.HBox([rer_button, train_button]))

# Création du graphique des stations de métro
def plot_train():
    plt.figure(figsize=(10, 8))
    couleur_par_ligne = {}
    for index, row in stations.iterrows():
        if row['type'] == 'TRAIN':
            plt.plot(row['x'], row['y'], marker='o', color=row['color'])
            couleur_par_ligne[row['res_com']] = row['color']

    for index, row in stations.iterrows():
        connexion = row['connexion']
        if not pd.isna(connexion):
            station_connectee = stations[stations['id_gares'] == connexion].iloc[0]
            if row['type'] == 'TRAIN' and station_connectee['type'] == 'TRAIN':
                plt.plot([row['x'], station_connectee['x']], [row['y'], station_connectee['y']], linestyle=row['style'], color=row['color'])

     # Création de la légende personnalisée avec les couleurs des lignes RER
    legende_personnalisee = []
    for ligne, couleur in couleur_par_ligne.items():
        legende_personnalisee.append(plt.Line2D([0], [0], marker='o', color=couleur, label=f'{ligne}', linestyle=''))

    plt.title('Carte des Stations de Métro à Paris')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(handles=legende_personnalisee)
    plt.show()
    # Affichage des boutons
    display(widgets.HBox([rer_button, train_button]))

# Boutons pour basculer entre RER et métro
rer_button = widgets.Button(description="Afficher RER")
train_button = widgets.Button(description="Afficher TRAIN")

# Fonctions de gestion des boutons
def rer_button_click(b):
    plt.clf()  # Efface le graphique actuel
    plot_rer()

def train_button_click(b):
    plt.clf()  # Efface le graphique actuel
    plot_train()

# Attachez les fonctions de gestion aux boutons
rer_button.on_click(rer_button_click)
train_button.on_click(train_button_click)

# Affichage initial (RER)
plot_rer()