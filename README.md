# Mihaly Cap Projet
Création de différent module pour automatiser des tâches facilitant le travail de notre client. </br>
Anyi CHEN </br>
Thomas DOGNON </br>
Pierre HANNE </br>
Jacky HOANG </br>
Jonathan NICOLAÏ </br>
### Pré-requis
- Installer Blender </br>
- Installer Python </br>
### Modules
1. Module de réorientation
2. Module de réparation
> #### Module de réorientation
Ce module a pour but de réorienter un modèle 3D sur le plan XY et le recentrer en 0,0. </br>
Il est fréquent que les modèles générés par différents systèmes de scan ne prennent pas soin de réorienter ni recentrer le modèle mais l’expriment dans leur repère caméra. </br>
Ce module est susceptible d’être utilisé à différentes étapes de traitement des modèles 3D. </br>

> #### Module de réparation
 Les modèles digitalisés en 3D peuvent comporter des trous de digitalisation, notamment sur les zonesou l’algorithme de reconstruction n'a pas pu déterminer la couleur et un point du maillage. Ce module permet de réparer les modèles (reboucher les trous). </br>
Il est utilisable:
- En mode détection(sans assistance utilisateur); des données sur les zones à trou sont données.
- En mode script (sans assistance utilisateur). 
- En mode interactif (l’utilisateur a accès aux résultats de recherche de trou et se voit proposer un traitement itératif pour les corriger à partir de paramètres réglables à définir).
