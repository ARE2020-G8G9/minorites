# ARE Dynamic : Evolution de l'acceptation morale du groupe LGBTI

Résumé de quelques lignes présentant l'objectif de votre projet, la méthode que vous avez suivie pour le réaliser et les résultats marquants que vous avez obtenus.

## ARE Dynamic : Evolution of moral acceptance of the LGBTI group

Un titre et un résumé en anglais qui reprennent le titre et le résumé en français, mais en anglais pour attirer une audience internationale sur vos travaux !

## Présentation de l'équipe

H. Authier, M. Coumbassa, P. Crabtree et A. Guetsa


## Description synthétique du projet

**Problématique :** Comment certains facteurs influent-ils sur l’acceptation d’une minorité sociale au cours du temps ?

**Hypothèse principale :**

- Sur le long terme, on aboutit soit à une acceptation "totale" soit à une exclusion "totale" de la minorité, et il y a davantage tendance à ce qu'on aboutisse à une acceptation ; il restera peut-être un petit pourcentage de rejet mais il sera minoritaire et tendra à devenir négligeable au fil du temps.

**Hypothèses secondaires (hypothèses de travail) :** 

- Pour faciliter le travail de recherche et pouvoir se baser sur davantage d’études, on considère l’ensemble des personnes LGBTI (lesbiennes, gays, bisexuel-les, trans, intersexes) comme un groupe uni, concerné par les mêmes discriminations.
- On considère que l’appartenance au groupe LGBTI est autodéterminée (ie les individus déterminent elles/eux-mêmes si elles/ils sont LGBTI ou non).
- On considère que la population est scindée en deux sous-groupes : les personnes LGBTI et les personnes non-LGBTI.
- L’acceptation des personnes LGBTI est basée sur une autoévaluation des individus qui se considèrent (ou non) comme “acceptants”.

**Objectifs :**
Mettre en évidence l’influence des facteurs étudiés sur l’acceptation de la communauté LGBTI.

**Critère(s) d'évaluation :**
- Niveau de tolérance de l’environnement a priori
- Influence des lois (en faveur de la minorité ou au contraire discriminantes)
- Taille du groupe LGBTI a priori (ou du moins du groupe “visible”, donc sans prendre en compte les personnes “dans le placard” c’est-à-dire qui ne se revendiquent pas LGBTI, soit parce qu'elles n'en ont pas encore pris conscience soit parce qu'elles le cachent)
- Visibilité dans les médias (positive, par exemple représentantes/représentants de la minorité étudiée, ou négative)
> Néanmoins ce critère est difficilement quantifiable, et nous ne le mettrons pas forcément dans la modélisation elle-même : mais nous explorerons les sources journalistiques pour orienter notre interprétation de la modélisation.


## Présentation structurée des résultats
### Idée de modélisation :
A une échelle fixée de façon à être à la fois représentative et raisonnable en terme de puissance de calcul (par exemple 100 individus, soit un carré de 10x10 cases), où chaque individu est représenté par une case, on fixe un seuil d'acceptation (par exemple 50 sur 100). On peut définir par exemple quatre couleurs, vert, jaune, rouge, violet : où vert = au-dessus du seuil d'acceptation, jaune = autour du seuil (par exemple entre 45 et 55 si le seuil est à 50), rouge = au-dessous, et violet = les personnes LGBTI. Un avantage de cette modélisation est qu'en plus d'être assez visuellement claire, elle permet de voir directement le lien entre le nombre de personnes LGBTI, leur isolement etc. et le taux d'acceptation dans leur environnement.
Nous fixons tout d'abord des conditions initiales (un certain nombre de personnes LGBTI en fonction des statistiques en France puis les différents critères d'évaluation comme le taux de population acceptante, l'influence des lois, etc. pour établir le taux de personnes acceptantes, "neutres" ou non-acceptantes.). Cela permet d'avoir une population initiale que nous affichons. 
Ensuite, en s'inspirant du modèle de Schelling, nous parcourons chaque individu non-LGBTI un par un et éventuellement modifions son taux d'acceptation en fonction de son entourage : on suppose que si une personne a beaucoup de personnes LGBTI ou acceptantes dans son entourage elle est plus susceptible de changer d'avis au bout d'un certain temps et donc de voir son taux modifié, etc. On peut considérer toutefois que les personnes ayant un taux extrême (très bas ou très élevé) seront moins promptes à changer d'avis.
On peut considérer que chaque parcours de la population correspond à un intervalle de temps (par exemple un mois). Au bout de chaque mois on affiche le nouvel état de la population, et on arrête l'algorithme lorsqu'on a atteint un temps prédéfini ou alors que la situation est stable (ie n'a pas évolué depuis plus d'un certain nombre de tours).

Présentation du choix de modélisation, des outils, du code et des résultats (tableaux, courbes, animations...) (**avec une analyse critique**).

## Lien vers page de blog : <a href="blog.md"> C'est ici ! </a>

## Bibliographie :

**Carte mentale de nos mots-clés :** <a href="carte mentale v2.png">ici </a> 

** Ressources bibliographiques : **

<a href="https://www.lexpress.fr/actualite/societe/les-5-ans-du-mariage-pour-tous-en-5-chiffres_2001646.html"> Les 5 ans du mariage pour tous en 5 chiffres </a> par Emilie Tôn
Article journalistique de 2018, de L’express

<a href=https://fr.wikipedia.org/wiki/Mariage_homosexuel> Mariage homosexuel</a> 
Page Wikipédia, source secondaire 
 
<a href="https://www.lemonde.fr/societe/article/2019/06/26/meme-si-l-homosexualite-est-mieux-acceptee-des-poches-d-homophobie-demeurent-en-france_5481512_3224.html"> Même si l’homosexualité est mieux acceptée, des poches d’homophobie demeurent en France </a> de Solène Cordier
Article de journal de Le Monde, de 2019

Les indicateurs sociaux de l’OCDE : Comment améliorer l’intégration des minorités sexuelles et de genre, chapitre 1 
Métaétude de 2019, PDF

**<= Indiquez le canal utilisé pour les trouver (Google Scholar, sources wikipedia, ressources en ligne SU, ...)**
