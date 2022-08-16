
# test github



# coding: utf8

# taille fenetre :
"""
cd Documents\Perso\Python\Pac_man
"""
import pygame as py
import module_pm as m

# initialisation de pygame
py.init()

# Initialisation de la fenetre graphique avec son nom
# | py.RESIZABLE
fenetre = py.display.set_mode((m.LARGUEUR,m.HAUTEUR), py.DOUBLEBUF | py.HWSURFACE )
py.display.set_caption("PAC MAN P.A.")

# Vérif des paramètres d'affichage dans le terminal :
print(py.display.Info())


# [1] afichage logo et démarrage :
fenetre.blit(m.logo,[0,0])
py.display.flip()
A = True
FIN = True
while A :
    for event in py.event.get() :
        if event.type == py.QUIT :
            A = False
            FIN = False
            break
        if event.type == py.KEYDOWN :
            if event.key == py.K_SPACE :
                A = False
                break


# [2] premier dessin à l'arrêt :
fenetre.blit(m.fond,[0,0])
fenetre.blit(m.pac_g,[m.Xpm,m.Ypm])
for i in m.fantome :
    fenetre.blit(m.fant,[i[0],i[1]])
py.display.flip()
A = True
while A and FIN:
    for event in py.event.get() :
        if event.type == py.QUIT :
            A = False
            FIN = False
            break
        if event.type == py.KEYDOWN :
            if event.key == py.K_SPACE :
                A = False
                break
        elif event.type == py.MOUSEBUTTONDOWN :
            if event.button == 3 :
                A = False
                break


lancement = True
# [3] Coeur du programme
while lancement and FIN :
    # [1] variable de boucle
    m.DIRECTION_com = ""
    touche = False

    # [2] effacement dernière image : (dernier pac_man et fantomes)
    py.draw.rect(fenetre, m.C_FOND, [m.Xpm, m.Ypm, m.cote, m.cote])
    ### pas fini
    for i in m.fantome :
        for j in m.bonbon :
            b =  0
            if  i[0] == j[0] and i[1] == j[1] :
                b += 1
                break
        if b >= 1 :
            fenetre.blit(m.boule_j,[i[0],i[1]])
        else :
            py.draw.rect(fenetre,m.C_FOND,[i[0],i[1],m.cote,m.cote])

    # [3] Obtention avant actualisation des
    # coordonnées de pac man last frame
    m.Xpm_last, m.Ypm_last, m.DIRECTION_last = m.Xpm, m.Ypm, m.DIRECTION

    # [4] verif colision avec les bonbons :
    for i in range(len(m.bonbon)) :
        b =  0
        if  m.bonbon[i]==[m.Xpm,m.Ypm]  :
            b = i
            m.score += 1
            del m.bonbon[b]
            break

    # [5] receptionnaire des touches du clavier
    # changement de direction sans test : sera corriger si
    # colision à [6]
    for event in py.event.get() :
        if event.type == py.QUIT :
            lancement = False
        elif event.type == py.KEYDOWN  :
            if event.key == py.K_UP and m.DIRECTION != "haut" :
                m.DIRECTION_com = "haut"
                touche = True
            elif event.key == py.K_DOWN and m.DIRECTION != "bas":
                m.DIRECTION_com = "bas"
                touche = True
            elif  event.key == py.K_LEFT and m.DIRECTION != "gauche":
                m.DIRECTION_com = "gauche"
                touche = True
            elif event.key == py.K_RIGHT and m.DIRECTION != "droite":
                m.DIRECTION_com = "droite"
                touche = True
    # [6] avancé de pac man en fonction de tt
    m.Xpm,m.Ypm,m.DIRECTION,m.DIRECTION_last,m.DIRECTION_next,m.DIRECTION_com=m.avance_pac(m.Xpm,m.Ypm,m.Xpm_last,m.Ypm_last,m.DIRECTION,m.DIRECTION_last,m.DIRECTION_next,m.DIRECTION_com,m.cote,touche)
    # [8] avancé de ts les fantomes en fonction de si
    # ils sont sur une intersection, les déplacement sont aléatoires
    # et prennent en compte les bors
    m.fantome = m.avance_fantome(m.fantome,int(m.cote))

    # [11] verif de colision avec fantome (fin de jeu loose):
    for i in m.fantome :
        if  i[0] == m.Xpm and i[1] == m.Ypm :
            m.fin_loose(fenetre, m.score)
            lancement = False

    # [12] test de fin de jeu (fin de jeu win) :
    if m.score == 200 :
        m.fin_win(fenetre, m.score)
        lancement = False

    # [13] actualisation de l'affichage :
    fenetre.blit(m.pac[m.direct.index(m.DIRECTION)], [ m.Xpm, m.Ypm ])
    for i in m.fantome :
        fenetre.blit(m.fant, [i[0], i[1]])

    m.compteur += 1
    py.time.delay(m.speed)
    py.display.flip()