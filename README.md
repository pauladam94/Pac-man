# Pac-man
programmation du jeu Pac man en python via le module  pygame


Ce jeu est surement le plus compliqué de ceux que j'ai programmé. En effet beaucoup de problèmes
intéressant interviennent dans la programmation d'un Pac Man :

- dessiner la carte et l'intégrer dans le jeu était assez long, j'ai pour cela crée une interface
graphique qui permettait de rentre les localisations de murs à la souris point par point.

- gérer les volontés de déplacement n'était pas simple non plus. En effet (contrairement au Snake)
certains mouvements sont interdit dans ce jeu car il y a des murs. 

- de plus il faut garder dans une liste d'attente les mouvements souhaités en utilisant une
structure de file.

- gérer les mouvements des fantômes qui suivent partiellement Pac Man. La programmation orienté
objet m'a permis de faire bouger plus facilement les fantômes en leur créant une classe associée aux fantômes.
