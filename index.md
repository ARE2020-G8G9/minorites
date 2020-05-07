# ARE Dynamic : Evolution de l'acceptation morale du groupe LGBTI

Dans l'idée de dynamisme, le thème qui nous a le plus séduites fut celui des phénomènes sociaux. Ces phénomènes étant incroyablement durs à modéliser à notre niveau, nous avions comme objectif de peindre un portrait de quelques leviers sociaux, notamment sur l'acceptation de la minorité LGBTI. 
On a imaginé un système de points d'acceptation, théorique, qu'on a couplé avec une adaptation du modèle de Schelling pour représenter l'influence inconsciente de notre entourage. Le point crucial fut la modélisation des facteurs extérieurs sociaux (lois, médiatisation, prévalence des groupes religieux...etc), qui se sont révélés être des catalyseurs extrêmement puissants des leviers d'acceptation de la population.

## ARE Dynamic : Evolution of moral acceptance of the LGBTI group

In the idea of dynamism, the theme that most appealed to us was that of social phenomena. These phenomena are incredibly hard to model at our level; therefore, our goal was to paint an accurate picture of some social levers, especially related to the acceptance of the LGBTI group.
We imagined a theoretical system of “acceptance points”, coupled with an adaptation of the Schelling model to show the unconscious influence of our surroundings. The crucial issue was to model external social factors such as laws, media visibility, religious prevalence etc., which turned out to be extremely powerful catalysts of public acceptance levers.


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

A une échelle fixée de façon à être à la fois représentative et raisonnable en terme de puissance de calcul (par exemple 100 individus, soit un carré de 10x10 cases), où chaque individu est représenté par une case, on fixe un seuil d'acceptation (par exemple 50 sur 100). On peut définir par exemple quatre couleurs, vert, jaune, rouge, violet : où vert = au-dessus du seuil d'acceptation, jaune = autour du seuil (par exemple entre 45 et 55 si le seuil est à 50), rouge = au-dessous, et violet = les personnes LGBTI, dont on considère qu'elles ont un seuil supérieur à 100 car elles seront plus promptes à influencer positivement le seuil de leur entourage. 
Un avantage de cette modélisation est qu'en plus d'être assez visuellement claire, elle permet de voir directement le lien entre le nombre de personnes LGBTI, leur isolement etc. et le taux d'acceptation dans leur environnement.

Nous fixons tout d'abord des conditions initiales (un certain nombre de personnes LGBTI en fonction des statistiques en France puis les différents critères d'évaluation comme le taux de population acceptante, l'influence des lois, etc. pour établir le taux de personnes acceptantes, "neutres" ou non-acceptantes.). Cela permet d'avoir une population initiale que nous affichons.

Ensuite, en s'inspirant du modèle de Schelling, nous parcourons chaque individu non-LGBTI un par un et éventuellement modifions son taux d'acceptation en fonction de son entourage et de la présence ou non de facteurs extérieurs : on suppose que si une personne a beaucoup de personnes LGBTI ou acceptantes dans son entourage elle est plus susceptible de changer d'avis au bout d'un certain temps et donc de voir son taux modifié, etc. On peut considérer toutefois que les personnes ayant un taux extrême (très bas ou très élevé) seront moins promptes à changer d'avis.

On peut considérer que chaque parcours de la population correspond à un intervalle de temps (par exemple un mois). Au bout de chaque mois on affiche le nouvel état de la population, et on arrête l'algorithme lorsqu'on a atteint un temps prédéfini.


### Résultats de la modélisation :

**Présentation du programme Python permettant d'afficher une modélisation avec des paramètres que l'on choisit :** <a href= "code ARE minorites version finale.py" ici </a>
**Présentation de nos résultats en faisant varier différents paramètres :** <a href= "Tests variation paramètres.pdf" ici </a>


### Interprétation de notre modèle, ressemblance avec la réalité, analyse critique :

En fin de projet, nous allons dresser quelques réflexions qui ressortent de notre travail final.

Le premier point, c'est **l'état des lieux** de notre projet comparé à ce que nous avions prévu de base. Un point crucial était de juger la balance simplicité/faisabilité et pertinence du modèle ; car nous savions très bien à quel point les modèles sociaux sont multifactoriels. Le rendu s'avère satisfaisant, en vertu d'une capacité prédictive suffisamment cohérente (il semble en effet décrire les mécanismes triviaux de mutations sociales), et de multiples facteurs qui permettent d'explorer les possibilités.

**Ensuite, avec les tests accessibles, on voit quelques points intéressants :**

Le premier point c'est que plus il y a un grand pourcentage de personne acceptantes, plus la croissance de l'acceptation se fait rapidement, c'est l'idée de ''cercle vertueux'', boucle rétroactive qui favorise les majorités.

Le deuxième point c'est la constatation d'une évolution profondément lente dans des conditions peu favorables (peu de LGBTI, pas de facteurs extérieurs) ou la croissance de l’acceptation se voit être particulièrement stagnante.

On peut émettre un début de comparaison avec cet article de *Le Monde* : << Même si l’homosexualité est mieux acceptée, des poches d’homophobie demeurent en France >> de Solène Cordier (cf bibliographie en bas de page)

<< Ainsi, 85 % des Français considèrent que l’homosexualité est « une manière acceptable de vivre sa vie » (en 2019), contre 24 % en 1975 >>

En 44 ans, l'acceptation à augmenté de 64 points ; on doit donc s'attendre a voir un changement très lent par période de 6 mois, soit moins d'un pourcent, quand l'acceptation est un groupe qui n'est pas encore largement majoritaire. C'est donc cohérent avec notre modèle.

Le troisième point est l'identification des facteurs sociaux comme rôle de catalyseurs, et c'est effectivement ce qu'il en ressort des différentes études qui placent ces facteurs comme dynamiques intégrantes des LGBTI. De plus, ces facteurs sont auto-influençants, et nous avons essayé de représenter cela avec une boucle incrémentative du nombre de points que l'influence apporte à chaque individu ; plus il y a de facteurs externes, et plus il y a de facteurs externes.

Les différents tests montrent l'importance comparative des trois facteurs importants, le groupe LGBTI, l'acceptation initiale, et la présence de facteurs sociaux. Il n'y a pas l'air d'avoir de différence significative entre ces trois facteurs, sauf peut-être pour les facteurs extérieurs, plus efficaces. Il nous paraît cependant difficile de déterminer si comparer les puissances d'influence à partir de notre modèle est pertinent, au vu des données empiriques manquantes, aussi précises et simplifiées.

Enfin le point crucial est que les conditions nécessaires à une croissance rapide de l'acceptation est la haute proportion du groupe LGBTI, du groupe acceptant, et de facteurs sociaux. Sans cela on est destiné à une croissance faible qui augmente petit à petit.

Le résultat final met en évidence les **mécaniques principales d'acceptation**, avec quelques aspects cruciaux ressemblants avec la réalité, d'une manière assez claire. Sur tous les points abordés, il semble cohérent avec la réalité et les connaissances sociologiques sur le sujet ; et c'est le gros point fort de notre modèle. Il permet dans une certaine mesure l'extrapolation et l'analyse de ces phénomènes avec un certain degré de sûreté.

**Le point critique** le plus important est peut-être le regroupement de tous les facteurs sociaux externes sous un paramètre ; cela est dû à la complexité de hiérarchiser ceux-ci en terme d'influence car ils s'inter-influencent tous, à la difficulté d'établir une échelle de quantité d'influence extérieure, et au manque de données disponibles. Ce travail aurait pu être fait néanmoins, mais il aurait représenté une difficulté robuste que nous avons préféré éviter.

Évidemment, on mettra aussi en évidence la faible qualité prédictive de notre modèle en raison d'une trop grande simplification (volontaire). Le modèle n'étant pas au final créé pour ressembler et prédire, mais plutôt pour imiter les mécaniques et leviers sociaux mis en jeu dans notre réalité à échelle simplifié.


## Lien vers page de blog : <a href="blog.md"> C'est ici ! </a>

## Bibliographie :

**Carte mentale de nos mots-clés :** <a href="carte mentale v2.png"> ici </a> 

**Ressources bibliographiques : **

<a href="https://www.lexpress.fr/actualite/societe/les-5-ans-du-mariage-pour-tous-en-5-chiffres_2001646.html"> Les 5 ans du mariage pour tous en 5 chiffres </a> par Emilie Tôn
Article journalistique de 2018, de L’express

<a href=https://fr.wikipedia.org/wiki/Mariage_homosexuel> Mariage homosexuel</a> 
Page Wikipédia, source secondaire 
 
<a href="https://www.lemonde.fr/societe/article/2019/06/26/meme-si-l-homosexualite-est-mieux-acceptee-des-poches-d-homophobie-demeurent-en-france_5481512_3224.html"> Même si l’homosexualité est mieux acceptée, des poches d’homophobie demeurent en France </a> de Solène Cordier
Article de journal de Le Monde, de 2019

<a href="https://www.oecd.org/fr/publications/panorama-de-la-societe-19991304.htm"> Les indicateurs sociaux de l’OCDE : Comment améliorer l’intégration des minorités sexuelles et de genre </a>, chapitre 1 

Métaétude de 2019, PDF

<a href=https://courspython.com/animation-matplotlib.html> Apprendre à réaliser une animation avec matplotlib</a>
Ressource utilisée pour le rendu graphique du code. (Nous avons également utilisé les documentations de numpy et matplotlib)

Nous avons essentiellement utilisé Google ainsi que Google Scholar.
