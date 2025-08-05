import pandas as pd

BAN = pd.read_csv('https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz', sep=';', encoding='utf-8')
bdx_metropole = pd.read_csv('georef-france-commune.csv', sep=';')

# conserver uniquement les adresses de la métropole
liste_communes = bdx_metropole['Code Officiel Commune']
BAN = BAN[BAN['code_insee'].isin(liste_communes)]

# nettoyage du DataFrame des adresses
BAN = BAN[['numero', 'nom_voie', 'code_postal', 'code_insee', 'nom_commune', 'lon', 'lat']]

# export, conserver les caractères spéciaux
BAN.to_csv('adresses_bdx_metropole.csv', index=False, encoding='utf-8')
BAN.to_json('adresses_bdx_metropole.json', force_ascii=False)