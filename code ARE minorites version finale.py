#Code ARE minorites

import random
import math
import matplotlib as mpl
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import numpy as np
from time import sleep

#On travaille sur une population de n*n habitants : pour la représentation graphique et l'étude du voisinage en deux dimensions on étudiera donc une matrice de y*y (soit une liste contenant y listes de y éléments chacune), que l'on convertira ensuite en tableau pour la partie affichage graphique. (à l'aide de Numpy)

#Les fonctions distrib_alea et tolerance travaillent uniquement sur une liste de y et on assemblera y de ces listes pour le voisinage total.


#Partie "calculatoire" : on définit le voisinage, la tolérance et on fait fonctionner la modélisation mais sans se préoccuper de l'aspect graphique ou d'afficher des résultats.

def distrib_alea(n, y):
    """
distribution de la minorité dans la population avec 1 la minorité et 0 le reste. Prend en entrée deux entiers : y la taille de la population et n la taille de la minorité.
"""
    res = [0 for i in range(y)]
    compteur = 0
    while compteur<n: 
        i = random.randint(0, y-1)
        if res[i] != 1: 
            res[i] = 1 
            compteur += 1
    return res



def tolerance(n, y, taux_tolerance, minorite, taux_neutre, taux_accept):
    """
    int * int * float * float * int * int -> list[int]
    Hypothèse : taux_tolerance et minorite sont compris entre 0 et 1.
    Distribue la tolérance au sein d’une population de taille y avec un groupe de taille n, un taux de population tolérante taux_tolerance et un pourcentage minorite en dessous duquel on considère que le groupe de taille n est une minorité. (on considère qu'une personne est tolérante à partir de taux_accept, car entre taux_neutre et taux_accept elle est "neutre".)
    """
    x = distrib_alea(n,y)
    compteur = 0 #le nombre de personnes tolerantes
    taux_atteint = 0 #indique s'il y a assez de personnes tolérantes dans la population ou non
    if n/len(x) > minorite: #ie si le groupe n’est pas une minorité
        
        print("Le groupe n'est pas une minorité.\n'")
    else:
        i = 0
        while i < (len(x)):
            if x[i]==1:
                x[i]=110 #La minorité est considérée comme totalement acceptante. De plus on lui donne une tolérance "supérieure" au taux de tolérance possible car cela la rend facilement repérable et donc plus facile à traiter graphiquement.
            else:
                while compteur/len(x) < taux_tolerance and i < len(x): #Il n'y a pas encore ""suffisamment"" de personnes tolérantes dans la population par rapport au taux fixé dans les paramètres.
                    if x[i] == 1:
                        x[i] = 110
                    elif x[i] == 0: #La personne n'est pas LGBTI et n'a pas encore un taux de tolérance
                        x[i] = random.randint(0, 100)
                        if taux_accept < x[i] <= 100:
                            compteur += 1
                    i += 1
                if compteur/len(x) >= taux_tolerance:
                    taux_atteint = 1
                if taux_atteint == 1 and i < len(x): #Pour éviter un index out of range
                    x[i]=random.randint(0,taux_accept)
            i = i + 1
        if taux_atteint == 0: #Dans ce cas on n'a pas assez de personnes tolérantes donc on recommence.
            return(tolerance(n, y, taux_tolerance, minorite, taux_neutre, taux_accept))
        return x

def construct_voisinage(n, y, taux_tolerance, minorite, taux_neutre, taux_accept):
    """
    int * int * float * float * int * int -> list[list[int]]
    Construit un voisinage complet, c'est à dire dans notre cas de taille y*y avec les mêmes paramètres et hypothèses que précédemment : on génère y fois une liste de taille y."""
    resultat = []
    for loop in range(y):
        resultat.append(tolerance(n, y, taux_tolerance, minorite, taux_neutre, taux_accept))
    return resultat


def facteur_exterieur(tolerance, taux_neutre, taux_accept):
    """Number*int*int->Number
    Hypothèse : taux_neutre < taux_accept
    On incrémente aux individus de tolérance tolerance au premier tour des valeurs différentes (arbitraires) selon si ils appartiennent à la classe de gens moyennement acceptant ("neutre") ou totalement acceptant. On considère que les personnes neutres n'ont pas encore d'avis poussé sur la question et donc sont plus susceptibles d'être influencées positivement, tandis que les personnes non acceptantes ne le sont pas du tout et les personnes déjà acceptantes le sont moins.
    """
    if taux_neutre <= tolerance <= taux_accept:
        tolerance += 3
    elif taux_accept < tolerance <= 100:
        if tolerance + taux_accept > 100 and tolerance != 110:
            tolerance = 100 #On s'assure que le taux de tolérance ne dépasse pas 100, et on ne considère pas les personnes LGBTI car sinon leur taux serait ramené à 100 au lieu de 110.
        else:
            tolerance = tolerance + 1
    return tolerance

def influence_voisinage(tolerance_vois, taille_vois, pourcentage_influence, présence_facteurs_exterieurs, taux_neutre, taux_accept):
    """
    list[list[int]] * int * int * int * int * int -> list[int]
    Hypothèse : les valeurs de tolerance_vois sont comprises entre 0 et 100 de même que pourcentage_influence.
    présence_facteurs_exterieurs est la présence ou non de facteur exterieur tel que les lois, la prévalence des groupes religieux, la médiatisation de la minorité. A 0 il n'existe pas, à 1 il est présent.

    Parcourt la liste tolerance_vois du taux de tolérance de l'environnement et modifie la tolérance en fonction du pourcentage d'influence et du taux de tolérance des voisins (on considère un voisinage de la taille taille_vois en haut, en bas, à gauche, à droite et dans les diagonales ; par exemple si taille_vois = 1 on considère 8 voisins.). 
    """
    
    #moyenne : int correspond à la moyenne du taux de tolérance du voisinage.
    moyenne = 0
    nb_voisins = 0 #Pour le calcul de la moyenne, cela évite de faire du cas par cas
    #On renvoie une nouvelle liste afin que lors d'un tour du voisinage, le taux de tolérance ne soit pas affecté par les changements qui ont eu lieu lors du même tour. ie on considère que tous les changements ont lieu en même temps sans s'inter-influencer (par exemple on effectue un sondage tous les mois).
    
    resultat = []
    liste = [] #Servira de liste intermédiaire, afin d'éviter de modifier la liste d'origine.
    m=0 #Représente l'incrémentation de l'influence des facteurs extérieurs au cours du temps 
        
    for i in range (len(tolerance_vois)):
        for j in range (len(tolerance_vois[i])):
            taux_tolerance = 110 #On initialise le taux de tolérance à 110 ; ainsi si la personne est LGBTI le taux n'est pas modifié, sinon on le modifie à la fin.
            #Choix de la personne dont on étudie la tolérance
            if tolerance_vois[i][j] == 110: #Si la personne est LGBTI sa tolérance ne change pas.
                liste.append(110)
            else:
                for voisin_i in range(i - taille_vois, i + taille_vois + 1):
                    for voisin_j in range(j - taille_vois, j + taille_vois + 1): #On parcourt les voisins considérés, en prenant également en compte la tolérance de la personne considérée.
                        if (0 <= voisin_i < len(tolerance_vois)) and (0 <= voisin_j < len(tolerance_vois[i])): #on vérifie que le voisin considéré existe bel et bien, en prenant en compte dans la moyenne le cas où le voisin considéré est lui-même.
                            moyenne += (tolerance_vois[voisin_i][voisin_j])
                            nb_voisins += 1 
                            
                moyenne = moyenne/nb_voisins
                m = m + 1
                
                #Calcul du nouveau taux de tolérance en fonction de l'influence du voisinage
                if présence_facteurs_exterieurs==1:
                    taux_tolerance = round(facteur_exterieur(tolerance_vois[i][j] + (moyenne - tolerance_vois[i][j]) * (pourcentage_influence/100),taux_neutre, taux_accept)+m)
                    
                else:
                    taux_tolerance = round(tolerance_vois[i][j] + (moyenne - tolerance_vois[i][j]) * (pourcentage_influence/100))
                if taux_tolerance <= 100:
                    liste.append(taux_tolerance)
                else:
                    liste.append(100)
    
            moyenne = 0 #On réinitialise la moyenne de tolérance du voisinage et le nombre de voisins
            nb_voisins = 0
            m = 0
        
        resultat.append(liste)
        liste = []
        
    return resultat


# Partie affichage graphique et modélisation

def affiche(tolerance_vois, taux_neutre, taux_accept):
    """list[list[int]] -> NoneType
    Permet d'afficher la tolérance du voisinage selon le code couleur indiqué, avec violet pour les personnes LGBTI.
    """
    valeurs = np.array(tolerance_vois)
    
    #Choix des couleurs
    couleurs = mpl.colors.ListedColormap([(0.8, 0.2, 0.2),(1, 0.8, 0.4),(0.2, 0.7, 0.3), (0.7, 0.5, 0.9)])
    bounds=[0,taux_neutre, taux_accept, 101, 110]
    norm = mpl.colors.BoundaryNorm(bounds, couleurs.N)
    
    img = pyplot.imshow(valeurs,interpolation='nearest',
                        cmap = couleurs,norm=norm)
    
    #Légende
    pyplot.title("Modélisation du voisinage")
    pyplot.colorbar(img,cmap=couleurs,
                    norm=norm,boundaries=bounds,ticks=[0, taux_neutre, taux_accept, 100, 110])
    
    pyplot.show()
    
    
def modelisation(n, y, taux_tolerance, taille_vois, minorite, pourcentage_influence, présence_facteurs_exterieurs, taux_neutre, taux_accept, temps):
    """
    Mêmes paramètres que précédemment ; le temps indique le nombre de tours que l'on veut faire effectuer à la simulation. Cette fonction permet de modéliser et d'afficher toute la simulation.
    """
    #On construit et affiche le voisinage au temps T0.
    voisinage = construct_voisinage(n, y, taux_tolerance, minorite, taux_neutre, taux_accept)
    affiche(voisinage, taux_neutre, taux_accept)
    
    #Choix des couleurs
    couleurs = mpl.colors.ListedColormap([(0.8, 0.2, 0.2),(1, 0.8, 0.4),(0.2, 0.7, 0.3), (0.7, 0.5, 0.9)])
    bounds=[0, taux_neutre , taux_accept, 101, 110]
    norm = mpl.colors.BoundaryNorm(bounds, couleurs.N)
    pyplot.show() 
    pyplot.pause(1)  
    pyplot.ion()
    
    for loop in range(temps):
    
        voisinage = influence_voisinage(voisinage, taille_vois, pourcentage_influence, présence_facteurs_exterieurs, taux_neutre, taux_accept)

        valeurs = np.array(voisinage)
        img = pyplot.imshow(valeurs,interpolation='nearest',
                            cmap = couleurs,norm=norm)
        
                        
        pyplot.pause(1)
        pyplot.draw()
        
    pyplot.ioff()


#Programme prenant en charge la modélisation avec l'entrée des paramètres par l'utilisatrice/utilisateur

print("Entrez la taille de la grille : (de côté, par exemple 10 correspondra à une population de 10x10 = 100) \n")
y=int(input())
print("Entrez le nombre de personnes pour chaque ligne appartenant à la minorité (ie pour une grille de 10x10 individus, entrer 2 pour avoir en tout 20 individus) : \n")
n=int(input())
print("Entrez le taux de population tolérante : (flottant entre 0 et 1) \n")
taux_tolerance = float(input())
print("Entrez le pourcentage en dessous du quel on considère un groupe comme minorité : (flottant entre 0 et 1) \n")
minorite = float(input())
print("Entrez le pourcentage d'influence : (flottant entre 0 et 100) \n")
pourcentage_influence = float(input())
facteur_ext = ""
while facteur_ext != "y" and facteur_ext != "n":
    print("Y'a t'il présence de facteurs extérieurs ? (y/n) : \n")
    facteur_ext = input()
    if facteur_ext == "y":
        présence_facteurs_exterieurs = 1
    elif facteur_ext == "n":
        présence_facteurs_exterieurs = 0
print("Entrez le taux d'acceptation correspondant à la neutralité : \n")
taux_neutre = int(input())
print("Entrez le taux d'acceptation correspondant à l'acceptation totale : \n")
taux_accept = int(input())
print("Entrez le nombre de boucles sur lequel vous voulez réaliser la simulation : \n")
temps = int(input())

modelisation(n,y,taux_tolerance,1,minorite,pourcentage_influence,présence_facteurs_exterieurs,taux_neutre,taux_accept,temps)

