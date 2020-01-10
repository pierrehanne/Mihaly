# Mihaly Cap Projet
Création de différent module pour automatiser des tâches facilitant le travail de notre client.
## Contexte
Les modèles 3D qui proviennent de digitalisation pardifférentes technologies de scan comportent des défauts à corriger tel des trous dans le modèle, des déformations légères. 
## Objectifs
- Les modules sont appelables en script python </br>
- Les modules peuvent faire appel à un outil type Meshlab, Blender </br>
- Les modules doivent permettre de s'appliquer à des maillages jusqu'à 80 millions de vertex </br>
### Pré-requis
- Posséder un ordinateur avec 8RAM mini </br>
- Installer Blender </br>
- Installer Meshlab </br>
- Installer Python </br>
```
On est ensemble dans la réussite ! Oubliez pas
```
### Modules attendues
1. Module de réorientation
2. Module de réparation
3. Module de mise à plat
4. Module de nettoyage
5. Module d'extraction d'images
6. Module statistique du modèle
7. Module de simplification du modèle

> #### Module de réorientation
> Ce module a pour but de réorienter un modèle 3D sur le plan XY et le recentrer en 0,0. </br>
> Il est fréquent que les modèles générés par différents systèmes de scan ne prennent pas soin de réorienter ni recentrer le modèle mais l’expriment dans leur repère caméra. </br>
> Ce module est susceptible d’être utilisé à différentes étapes de traitement des modèles 3D. </br>

> #### Module de réparation
> Les modèles digitalisés en 3D peuvent comporter des trous de digitalisation, notamment sur les zonesou l’algorithme de reconstruction n'a pas pu déterminer la couleur et un point du maillage. Ce module permet de réparer les modèles (reboucher les trous). </br>
> Il est utilisable:
> - En mode détection(sans assistance utilisateur); des données sur les zones à trou sont données.
> - En mode script (sans assistance utilisateur). 
> - En mode interactif (l’utilisateur a accès aux résultats de recherche de trou et se voit proposer un traitement itératif pour les corriger à partir de paramètres réglables à définir).

> ##### Module de mise à plat
> Ce module permet d’aplanir les ondulations lentes (courbure légères) d’une surface.</br>
> Il permet de supprimer la partie basse fréquence présentes sur un modèledigitalisé.
