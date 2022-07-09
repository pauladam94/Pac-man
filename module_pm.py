
# coding: utf8

import pygame as py
from random import randint
#from C:/Users/marin/Documents/Perso/Python/GENERAL/Couleur import *
py.init()

NOIR        = (0,0,0)
BLANC       = (255,255,255)
### def des variables :
# def couleur de fonc
C_FOND = NOIR

LARGUEUR = 990
HAUTEUR = 570

# importation des sons :
son_gen = py.mixer.Sound("son_gen.ogg")
point = py.mixer.Sound("point.ogg")

# importation des images :
pac_d = py.image.load("pac.png")
pac_h = py.transform.rotate(pac_d,90)
pac_g = py.transform.rotate(pac_d,180)
pac_b = py.transform.rotate(pac_d,270)

#pac_g.convert()
#pac_d.convert()
pac = [pac_h , pac_g , pac_b , pac_d]

fond = py.image.load("fond.png")
#fond.convert()

boule_j = py.image.load("boule.png")

logo = py.image.load("LOGO.png")
#logo.convert()

fant = py.image.load("fantome.png")
#fantome.convert()

#nombre de pixel par coté de carré
cote = 30

# Variable :
Xpm, Ypm= 2*cote, 3*cote

# def direction initial :
DIRECTION = "bas"
DIRECTION_last = "bas"
DIRECTION_next = ""
DIRECTION_com = ""

# def taille initial du snake :
taille = 2

# def vitese d'actualisation de la page :
speed = 200

#compteur de passaga dans la main boucle :
compteur = 0

# def du score initial :
score = 0

# def liste de direction :
direct = [ "haut" , "gauche" , "bas" , "droite" ]

# liste des bors du terrain :
bors = [
[ 0 , 8 ],[ 1 , 8 ],[ 1 , 7 ],[ 1 , 6 ],[ 1 , 5 ],[ 1 , 4 ],[ 1 , 3 ],[ 1 , 2 ],[ 1 , 1 ],[ 2 , 1 ],[ 3 , 1 ],[ 4 , 1 ],[ 5 , 1 ],[ 6 , 1 ],
[ 7 , 1 ],[ 8 , 1 ],[ 9 , 1 ],[ 10 , 1 ],[ 11 , 1 ],[ 12 , 1 ],[ 13 , 1 ],[ 14 , 1 ],[ 15 , 1 ],[ 16 , 1 ],[ 17 , 1 ],[ 18 , 1 ],
[ 19 , 1 ],[ 20 , 1 ],[ 22 , 1 ],[ 21 , 1 ],[ 23 , 1 ],[ 24 , 1 ],[ 25 , 1 ],[ 27 , 1 ],[ 26 , 1 ],[ 28 , 1 ],[ 30 , 1 ],[ 29 , 1 ],
[ 31 , 1 ],[ 31 , 1 ],[ 31 , 2 ],[ 31 , 3 ],[ 31 , 4 ],[ 31 , 5 ],[ 31 , 6 ],[ 31 , 7 ],[ 31 , 8 ],[ 32 , 8 ],[ 29 , 6 ],[ 29 , 5 ],
[ 29 , 4 ],[ 29 , 3 ],[ 28 , 3 ],[ 28 , 6 ],[ 27 , 6 ],[ 26 , 6 ],[ 25 , 6 ],[ 25 , 5 ],[ 25 , 4 ],[ 25 , 3 ],[ 26 , 3 ],[ 23 , 3 ],
[ 23 , 4 ],[ 23 , 5 ],[ 23 , 6 ],[ 23 , 7 ],[ 23 , 7 ],[ 23 , 8 ],[ 24 , 8 ],[ 25 , 8 ],[ 26 , 8 ],[ 27 , 8 ],[ 29 , 8 ],[ 29 , 10 ],
[ 29 , 12 ],[ 29 , 11 ],[ 29 , 13 ],[ 29 , 14 ],[ 29 , 15 ],[ 27 , 14 ],[ 27 , 15 ],[ 26 , 14 ],[ 26 , 15 ],[ 25 , 14 ],[ 25 , 15 ],
[ 26 , 12 ],[ 26 , 11 ],[ 25 , 11 ],[ 25 , 10 ],[ 27 , 11 ],[ 27 , 10 ],[ 32 , 10 ],[ 31 , 10 ],[ 31 , 11 ],[ 31 , 12 ],[ 31 , 13 ],
[ 31 , 14 ],[ 31 , 14 ],[ 31 , 15 ],[ 31 , 16 ],[ 31 , 17 ],[ 30 , 17 ],[ 29 , 17 ],[ 28 , 17 ],[ 27 , 17 ],[ 26 , 17 ],[ 25 , 17 ],
[ 25 , 17 ],[ 24 , 17 ],[ 23 , 17 ],[ 23 , 15 ],[ 23 , 14 ],[ 23 , 13 ],[ 23 , 12 ],[ 23 , 11 ],[ 23 , 10 ],[ 21 , 10 ],[ 21 , 11 ],[ 21 , 12 ],
[ 21 , 12 ],[ 20 , 12 ],[ 19 , 12 ],[ 21 , 13 ],[ 21 , 14 ],[ 21 , 15 ],[ 19 , 14 ],[ 19 , 15 ],[ 22 , 17 ],[ 21 , 17 ],[ 20 , 17 ],[ 19 , 17 ],
[ 18 , 17 ],[ 18 , 17 ],[ 17 , 17 ],[ 17 , 15 ],[ 17 , 14 ],[ 17 , 12 ],[ 17 , 13 ],[ 17 , 11 ],[ 17 , 10 ],[ 18 , 10 ],[ 19 , 10 ],
[ 19 , 8 ],[ 18 , 8 ],[ 18 , 8 ],[ 17 , 8 ],[ 17 , 7 ],[ 17 , 6 ],[ 17 , 5 ],[ 17 , 4 ],[ 17 , 3 ],[ 19 , 3 ],[ 19 , 4 ],[ 19 , 5 ],
[ 19 , 6 ],[ 21 , 8 ],[ 21 , 7 ],[ 21 , 6 ],[ 21 , 5 ],[ 21 , 5 ],[ 21 , 4 ],[ 21 , 4 ],[ 21 , 3 ],[ 12 , 3 ],[ 13 , 3 ],[ 14 , 3 ],
[ 15 , 3 ],[ 15 , 4 ],[ 15 , 5 ],[ 15 , 6 ],[ 15 , 7 ],[ 15 , 8 ],[ 13 , 7 ],[ 13 , 8 ],[ 12 , 8 ],[ 12 , 7 ],[ 13 , 5 ],[ 12 , 5 ],[ 11 , 5 ],
[ 10 , 5 ],[ 10 , 4 ],[ 10 , 3 ],[ 10 , 6 ],[ 10 , 7 ],[ 10 , 8 ],[ 8 , 7 ],[ 8 , 8 ],[ 7 , 7 ],[ 7 , 8 ],[ 6 , 7 ],[ 6 , 8 ],
[ 5 , 7 ],[ 5 , 8 ],[ 5 , 5 ],[ 6 , 5 ],[ 7 , 5 ],[ 8 , 5 ],[ 8 , 4 ],[ 8 , 3 ],[ 7 , 3 ],[ 6 , 3 ],[ 5 , 3 ],[ 4 , 3 ],[ 3 , 3 ],
[ 3 , 4 ],[ 3 , 5 ],[ 3 , 6 ],[ 3 , 7 ],[ 3 , 8 ],[ 0 , 10 ],[ 1 , 10 ],[ 1 , 12 ],[ 1 , 11 ],[ 1 , 13 ],[ 1 , 14 ],[ 1 , 15 ],[ 1 , 15 ],[ 1 , 16 ],
[ 1 , 17 ],[ 2 , 17 ],[ 3 , 17 ],[ 4 , 17 ],[ 5 , 17 ],[ 6 , 17 ],[ 8 , 17 ],[ 7 , 17 ],
[ 9 , 17 ],[ 10 , 17 ],[ 11 , 17 ],[ 12 , 17 ],[ 13 , 17 ],[ 14 , 17 ],[ 15 , 17 ],[ 16 , 17 ],[ 15 , 15 ],[ 14 , 15 ],[ 13 , 15 ],
[ 13 , 13 ],[ 13 , 12 ],[ 15 , 14 ],[ 15 , 13 ],[ 15 , 12 ],[ 15 , 11 ],[ 15 , 10 ],[ 14 , 10 ],[ 13 , 10 ],[ 11 , 10 ],[ 11 , 11 ],
[ 11 , 12 ],[ 11 , 13 ],[ 11 , 14 ],[ 11 , 15 ],[ 11 , 14 ],[ 10 , 15 ],[ 10 , 15 ],[ 10 , 14 ],[ 9 , 12 ],[ 9 , 11 ],[ 9 , 10 ],
[ 8 , 10 ],[ 8 , 11 ],[ 8 , 12 ],[ 8 , 13 ],[ 8 , 14 ],[ 8 , 15 ],[ 6 , 15 ],[ 6 , 14 ],[ 6 , 14 ],[ 5 , 14 ],[ 5 , 14 ],[ 5 , 15 ],
[ 3 , 15 ],[ 3 , 14 ],[ 3 , 13 ],[ 3 , 12 ],[ 3 , 11 ],[ 3 , 10 ],[ 4 , 12 ],[ 5 , 12 ],[ 6 , 12 ],[ 5 , 10 ],[ 6 , 10 ],[ 7 , 10 ],
]
for i in range(len(bors)):
    bors[i][0] *= cote
    bors[i][1] *= cote

# liste des bonbons jaune :
bonbon = [[ 2 , 2 ],
[ 2 , 3 ],[ 3 , 2 ],[ 2 , 4 ],[ 2 , 5 ],[ 2 , 6 ],[ 2 , 7 ],[ 2 , 8 ],[ 2 , 9 ],[ 1 , 9 ],[ 1 , 9 ],[ 1 , 9 ],
[ 0 , 9 ],[ 2 , 10 ],[ 2 , 11 ],[ 2 , 12 ],[ 2 , 13 ],[ 2 , 15 ],[ 2 , 14 ],[ 2 , 16 ],[ 3 , 16 ],[ 4 , 16 ],[ 4 , 15 ],
[ 6 , 13 ],[ 7 , 13 ],[ 7 , 14 ],[ 7 , 15 ],[ 7 , 16 ],[ 6 , 16 ],[ 5 , 16 ],[ 8 , 16 ],[ 4 , 14 ],[ 4 , 13 ],[ 5 , 13 ],
[ 9 , 16 ],[ 10 , 16 ],[ 11 , 16 ],[ 12 , 16 ],[ 13 , 16 ],[ 14 , 16 ],[ 15 , 16 ],[ 16 , 16 ],[ 18 , 16 ],[ 17 , 16 ],
[ 19 , 16 ],[ 20 , 16 ],[ 21 , 16 ],[ 22 , 16 ],[ 23 , 16 ],[ 24 , 16 ],[ 25 , 16 ],[ 26 , 16 ],[ 27 , 16 ],[ 28 , 16 ],
[ 29 , 16 ],[ 30 , 16 ],[ 30 , 15 ],[ 30 , 14 ],[ 30 , 13 ],[ 30 , 13 ],[ 30 , 12 ],[ 30 , 11 ],[ 30 , 10 ],[ 30 , 9 ],
[ 30 , 8 ],[ 30 , 7 ],[ 30 , 6 ],[ 30 , 5 ],[ 30 , 4 ],[ 30 , 2 ],[ 30 , 3 ],[ 29 , 2 ],[ 27 , 2 ],[ 28 , 2 ],[ 25 , 2 ],
[ 26 , 2 ],[ 24 , 2 ],[ 22 , 2 ],[ 23 , 2 ],[ 21 , 2 ],[ 19 , 2 ],[ 20 , 2 ],[ 18 , 2 ],[ 17 , 2 ],[ 16 , 2 ],[ 16 , 2 ],
[ 15 , 2 ],[ 14 , 2 ],[ 13 , 2 ],[ 12 , 2 ],[ 11 , 2 ],[ 10 , 2 ],[ 8 , 2 ],[ 9 , 2 ],[ 6 , 2 ],[ 7 , 2 ],[ 5 , 2 ],[ 4 , 2 ],
[ 3 , 9 ],[ 4 , 9 ],[ 5 , 9 ],[ 6 , 9 ],[ 7 , 9 ],[ 8 , 9 ],[ 9 , 9 ],[ 10 , 9 ],[ 11 , 9 ],[ 12 , 9 ],[ 13 , 9 ],[ 14 , 9 ],
[ 15 , 9 ],[ 16 , 9 ],[ 17 , 9 ],[ 18 , 9 ],[ 19 , 9 ],[ 20 , 9 ],[ 21 , 9 ],[ 22 , 9 ],[ 23 , 9 ],[ 24 , 9 ],[ 25 , 9 ],
[ 26 , 9 ],[ 27 , 9 ],[ 28 , 9 ],[ 29 , 9 ],[ 7 , 12 ],[ 7 , 11 ],[ 6 , 11 ],[ 6 , 11 ],[ 5 , 11 ],[ 4 , 11 ],[ 4 , 10 ],
[ 4 , 8 ],[ 4 , 7 ],[ 4 , 6 ],[ 4 , 5 ],[ 5 , 4 ],[ 4 , 4 ],[ 7 , 4 ],[ 6 , 4 ],[ 5 , 6 ],[ 6 , 6 ],[ 7 , 6 ],[ 9 , 6 ],[ 9 , 6 ],
[ 8 , 6 ],[ 9 , 7 ],[ 9 , 8 ],[ 9 , 5 ],[ 9 , 4 ],[ 9 , 4 ],[ 9 , 4 ],[ 9 , 3 ],[ 11 , 8 ],[ 11 , 7 ],[ 11 , 6 ],[ 12 , 6 ],
[ 13 , 6 ],[ 14 , 6 ],[ 14 , 5 ],[ 14 , 4 ],[ 13 , 4 ],[ 12 , 4 ],[ 11 , 4 ],[ 11 , 3 ],[ 14 , 7 ],[ 14 , 8 ],[ 16 , 3 ],
[ 16 , 4 ],[ 16 , 5 ],[ 16 , 6 ],[ 16 , 6 ],[ 16 , 7 ],[ 16 , 8 ],[ 18 , 3 ],[ 18 , 4 ],[ 18 , 5 ],[ 18 , 6 ],[ 18 , 7 ],
[ 19 , 7 ],[ 20 , 7 ],[ 20 , 6 ],[ 20 , 5 ],[ 20 , 4 ],[ 20 , 3 ],[ 20 , 8 ],[ 22 , 7 ],[ 22 , 8 ],[ 22 , 6 ],[ 22 , 5 ],
[ 22 , 4 ],[ 22 , 3 ],[ 24 , 3 ],[ 24 , 3 ],[ 24 , 4 ],[ 24 , 6 ],[ 24 , 6 ],[ 24 , 5 ],[ 24 , 7 ],[ 25 , 7 ],[ 26 , 7 ],
[ 27 , 7 ],[ 28 , 7 ],[ 29 , 7 ],[ 28 , 8 ],[ 28 , 10 ],[ 28 , 10 ],[ 28 , 11 ],[ 28 , 12 ],[ 28 , 12 ],[ 28 , 13 ],
[ 28 , 13 ],[ 28 , 14 ],[ 28 , 15 ],[ 26 , 10 ],[ 24 , 10 ],[ 24 , 11 ],[ 24 , 12 ],[ 24 , 13 ],[ 24 , 14 ],[ 24 , 14 ],
[ 24 , 15 ],[ 25 , 12 ],[ 25 , 13 ],[ 26 , 13 ],[ 27 , 13 ],[ 27 , 12 ],[ 22 , 15 ],[ 22 , 14 ],[ 22 , 13 ],[ 22 , 12 ],
[ 22 , 11 ],[ 22 , 10 ],[ 20 , 10 ],[ 20 , 11 ],[ 19 , 11 ],[ 18 , 11 ],[ 18 , 12 ],[ 18 , 13 ],[ 19 , 13 ],[ 20 , 13 ],
[ 20 , 14 ],[ 20 , 15 ],[ 18 , 14 ],[ 18 , 15 ],[ 16 , 15 ],[ 16 , 14 ],[ 16 , 13 ],[ 16 , 13 ],[ 16 , 12 ],[ 16 , 11 ],
[ 16 , 11 ],[ 16 , 10 ],[ 12 , 10 ],[ 12 , 11 ],[ 12 , 12 ],[ 12 , 13 ],[ 12 , 14 ],[ 12 , 15 ],[ 13 , 14 ],[ 14 , 14 ],
[ 14 , 13 ],[ 14 , 12 ],[ 14 , 11 ],[ 13 , 11 ],[ 10 , 10 ],[ 10 , 11 ],[ 10 , 12 ],[ 10 , 13 ],[ 9 , 13 ],[ 9 , 14 ],[ 9 , 15 ]
]

for i in range(len(bonbon)):
    bonbon[i][0] *= cote
    bonbon[i][1] *= cote

# liste des intersections :
intersections = [
[ 27 , 5 ],[ 26 , 9 ],
[ 2 , 9 ],[ 2 , 2 ],[ 4 , 4 ],[ 7 , 4 ],[ 4 , 6 ],[ 4 , 9 ],
[ 4 , 11 ],[ 2 , 16 ],[ 4 , 16 ],[ 4 , 13 ],[ 7 , 13 ],[ 7 , 11 ],[ 7 , 16 ],[ 9 , 16 ],[ 9 , 13 ],
[ 10 , 13 ],[ 10 , 9 ],[ 9 , 9 ],[9 , 6 ],[ 9 , 2 ],[ 11 , 2 ],[ 11 , 4 ],[ 14 , 4 ],[ 14 , 6 ],
[ 11 , 6 ],[ 11 , 9 ],[ 12 , 9 ],[ 14 , 9 ],[ 12 , 11 ],[ 14 , 11 ],[ 14 , 14 ],[ 12 , 14 ],[ 12 , 16 ],
[ 16 , 16 ],[ 16 , 9 ],[ 16 , 2 ],[ 18 , 2 ],[ 20 , 2 ],[ 18 , 7 ],[ 20 , 7 ],[ 20 , 9 ],[ 20 , 11 ],
[ 18 , 11 ],[ 18 , 13 ],[ 20 , 13 ],[ 18 , 16 ],[ 20 , 16 ],[ 22 , 16 ],[ 22 , 9 ],[ 22 , 2 ],[ 24 , 2 ],
[ 24 , 7 ],[ 27 , 2 ],[ 26 , 4 ],[ 28 , 4 ],[ 28 , 5 ],[ 26 , 5 ],[ 27 , 4 ],[ 30 , 2 ],[ 30 , 7 ],
[ 28 , 7 ],[ 28 , 9 ],[ 26 , 10 ],[ 24 , 9 ],[ 24 , 16 ],[ 24 , 13 ],[ 24 , 12 ],[ 25 , 12 ],
[ 25 , 12 ],[ 25 , 13 ],[ 27 , 12 ],[ 27 , 13 ],[ 28 , 12 ],[ 28 , 13 ],[ 28 , 16 ],[ 30 , 16 ],[ 30 , 9 ]
]

for i in range(len(intersections)):
    intersections[i][0] *= cote
    intersections[i][1] *= cote

# liste des positions et direction des fantomes :
fantome = [ 
[ 26 , 5 , "haut" ],[ 26 , 5 , "haut" ],
[ 28 , 5 , "haut" ],[ 28 , 5 , "haut" ],
[ 28 , 5 , "haut" ],[ 28 , 5 , "haut" ]
]

for i in range(len(fantome)):
    fantome[i][0]*=30
    fantome[i][1]*=30

def aff_debut(window):
    logo(window)
    py.display.update()
    dem = py.font.SysFont("arial", 30)
    aff = derender("appuyez sur la barre espace pour commencer", True, (255,255,255))
    window.blit(aff, [10,400] )
    py.display.update()

# fonction qui permet de renvoyer la prochaine position
# de la tete du serpent en fonction de sa direction
def direct_pos(direction, posx, posy, cote):
    if direction=="haut":
        posy -= cote
    elif direction=="bas":
        posy += cote
    elif direction=="gauche":
        posx -= cote
    elif direction=="droite":
        posx += cote
    return([posx,posy])

def fin_win(window, score):
    arial_30 = py.font.SysFont("arial", 30)
    dimension_text = arial_30.render("{}".format(" Vous avez gagné !! : - ))"), True, BLANC)
    score = arial_30.render("Score : " + str(score), False, BLANC) 
    window.blit(dimension_text, [150,200] )
    window.blit(score, [150, 300])
    py.display.flip()
    py.time.delay(2000)


def fin_loose(window, score):
    arial_30 = py.font.SysFont("arial", 30)
    dimension_text = arial_30.render("{}".format(" Vous avez perdu !! ; - ) "), True, BLANC)
    score = arial_30.render("Score : " + str(score), False, BLANC) 
    window.blit(dimension_text, [150,200] )
    window.blit(score, [150, 300])
    py.display.flip()
    py.time.delay(2000)

def aff_score(window,score) :
    py.draw.rect(window,NOIR,[0,540,540,100])
    arial_30 = py.font.SysFont("arial", 30)
    score = arial_30.render("Score : "+str(score), True, BLANC)
    window.blit(score, [100,560] )

def avance_fantome(fantom,cot) :
    for f in range(len(fantom)) :
        # un fantome à la fois
        for i in intersections :
            # on essaie si il se trouve à une intersection(en faisant chaque intersection)
            if [fantom[f][0] , fantom[f][1]] == [i[0],i[1]] :
                # si il se trouve sur une intersection
                test = True
                a = randint(0 , 3)
                c=0
                while test :
                    # on tire au hasard une direction et on essai si cette direction
                    # ne va pas faire aller dans un bors le fantome
                    part = 0
                    c+=1
                    for b in bors :
                        if direct_pos(direct[a],fantom[f][0],fantom[f][1],cot) == [b[0],b[1]] :
                            # si apres déplacement le fantome se trouverait sur un bors
                            # alors le compteur augmente
                            part += 1
                    if part == 0 and direct[a+2-4] != fantom[f][2]:
                        # le compteur doit être à zéro sinon on continue les essais 
                        fantom[f][2] = direct[a]
                        test = False
                        break
                    elif a==3:
                        a=0
                    else :
                        a+=1
                    if c>=5 :
                        a=direct.index(fantom[f][2])
                        fantom[f][2] = direct[a+2-4]
                        test = False
                        break

    for i in range(len(fantom)) :
        # avancer des fantomes :
        fantom[i][0],fantom[i][1] = direct_pos(fantom[i][2],fantom[i][0],fantom[i][1],cot)
            # [10] test téléportation sur les bors des fantomes ::
        if fantom[i][0] <= 0 :
            fantom[i][0] = LARGUEUR - cot
            fantom[i][2] = "gauche"
        if fantom[i][0] >= LARGUEUR :
            fantom[i][0] = 0
            fantom[i][2] = "droite"
    return(fantom)

def avance_pac(x,y,x_last,y_last,direction,direction_last,direction_next,direction_com,cot,touche):
    # si deplacment prend la valeur false ca veut dire que il n'y a 
    # plus de mouvement à faire (mouvement déjà fait ou 
    if verif_inter(intersections,x,y) :
    # si on est à une intersection
        if direction_com == "" :
        # et qu'il y a pas de commande
            # on avance avec la prédemande
            x , y = direct_pos(direction_next, x, y, int(cot))
            # on supprime la prédemande
            direction_next = ""
            # vérif colision
            if verif_inter(bors,x,y):
                x,y=x_last,y_last
        else  :
        # et qu'il y a une commande
            # alors on suit la commande
            x , y = direct_pos(direction, x, y, int(cot))
            # verif colision
            if verif_inter(bors,x,y):
                x,y=x_last,y_last

    else :
    # si on est pas à une intersection
        if direction_com == "" :
        # si il n'y a pas de commande
            # ne rien faire et juste continuer à avancer dans la même direction
            x,y = direct_pos(direction, x, y, int(cot))
            # pas de verif de colision

        else :
        # si il y a une commmande
            # on suit la commande
            x,y = direct_pos(direction_com, x, y, int(cot))

            # vérif de colision
            if verif_inter(bors,x,y):
                # si on se prend un mur
                # on change la direction next
                x,y=x_last,y_last
                direction_next = direction_com
    # clean
    # test téléportation sur les bors du plateau de pac man:
    if x <= 0 :
        x = LARGUEUR - cot
        direction = "gauche"
    if x >= LARGUEUR :
        x = 0
        direction = "droite"

    return(x,y,direction,direction_last,direction_next,direction_com)


def verif_inter(list,x,y):
    z = 0
    for i in range(len(list)):
        if list[i] == [x,y] :
            z += 1
            break
    if z == 0 :
        # si il n'y a pas d'intersection
        return(False)
    if z == 1 :
        # si il y a au moins une intersection
        return(True)