# Fenêtre de jeu de Going bomb
import pygame
import game_mode_facile
import game_mode_medium
import game_mode_hard

# Définition des couleurs et initialisation de Pygame
COULEUR_FOND = (255, 255, 255)
ORANGE = (237, 127, 16)
RED = (198, 0, 0)
BLUE = (0, 123, 198)
WHITE = (255, 255, 255)
pygame.init()
pygame.mixer.init()

# Chargement des images et dimensions de la fenêtre
fond = pygame.image.load("fond.jpg")
LARGEUR, HAUTEUR = fond.get_size()
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("GOING BOOM!")
fen.fill(COULEUR_FOND)
fond = fond.convert()

LARGEUR_REC_BEGIN_WIN_OVER = 120
HAUTEUR_REC_BEGIN_WIN_OVER = 50
LARGEUR_REC_CHOICE = 300
HAUTEUR_REC_CHOICE = 60


# Textes pour les différentes difficultés
police_choice = pygame.font.Font("police.ttf", 20)
msg_easy = police_choice.render("Easy", True, WHITE)
msg_medium = police_choice.render("Medium", True, WHITE)
msg_hard = police_choice.render("Hard", True, WHITE)


police_begin = pygame.font.Font("police.ttf", 16)
msg_clic = police_begin.render("Clique ici", True, WHITE)
msg_replay = police_begin.render("REPLAY", True, WHITE)


joueur = pygame.image.load("joueur.png").convert()
petit_joueur = pygame.transform.scale(joueur, (joueur.get_width() // 16, joueur.get_height() // 16))
petit_joueur = petit_joueur.convert_alpha()

homerdoh = pygame.image.load("doh.png").convert()
petit_homerdoh = pygame.transform.scale(homerdoh, (homerdoh.get_width() // 1.7, homerdoh.get_height() // 1.7))
petit_homerdoh = petit_homerdoh.convert()

regles = pygame.image.load("regles.png").convert()
petit_regles = pygame.transform.scale(regles, (regles.get_width() // 1.6, regles.get_height() // 1.6))
petit_regles = petit_regles.convert_alpha()

presentateur = pygame.image.load("presentateur.png").convert()
presentateur.set_colorkey((0, 0, 0))
petit_presentateur = pygame.transform.scale(presentateur, (presentateur.get_width() // 20, presentateur.get_height() // 20))
petit_presentateur = petit_presentateur.convert_alpha()

# Initialisation des rectangles
rect_blue_choice = pygame.Rect(156, 60, LARGEUR_REC_CHOICE, HAUTEUR_REC_CHOICE)
rect_orange_choice = pygame.Rect(156, 160, LARGEUR_REC_CHOICE, HAUTEUR_REC_CHOICE)
rect_red_choice = pygame.Rect(156, 260, LARGEUR_REC_CHOICE, HAUTEUR_REC_CHOICE)
rect_orange = pygame.draw.rect(fen, ORANGE, [246, 40, LARGEUR_REC_BEGIN_WIN_OVER, HAUTEUR_REC_BEGIN_WIN_OVER])

victory = pygame.image.load("victory.png").convert()
petit_victory = pygame.transform.scale(victory, (victory.get_width() // 1.3, victory.get_height() // 1.3))
petit_victory = petit_victory.convert_alpha()

homerwinleft = pygame.image.load("winhl.png").convert()
petit_homerwinleft = pygame.transform.scale(homerwinleft, (homerwinleft.get_width() // 1.2, homerwinleft.get_height() // 1.2))
petit_homerwinleft = petit_homerwinleft.convert_alpha()
homerwinright = pygame.image.load("winhr.png").convert()
petit_homerwinright = pygame.transform.scale(homerwinright, (homerwinright.get_width() // 1.2, homerwinright.get_height() // 1.2))
petit_homerwinright = petit_homerwinright.convert_alpha()

explo = pygame.image.load("explosion.gif").convert()
petit_explo = pygame.transform.scale(explo, (explo.get_width() // 5, explo.get_height() // 5))
petit_explo = petit_explo.convert_alpha()

game_over = pygame.image.load("game_over.png").convert()
petit_game_over = pygame.transform.scale(game_over, (game_over.get_width() // 1.3, game_over.get_height() // 1.3))
petit_game_over = petit_game_over.convert_alpha()

def afficher_elements_begin():
    fen.blit(petit_joueur, (420, 20))
    fen.blit(petit_regles, (40, 140))
    fen.blit(petit_presentateur, (120, 20))
    pygame.draw.rect(fen, ORANGE, [246, 40, LARGEUR_REC_BEGIN_WIN_OVER, HAUTEUR_REC_BEGIN_WIN_OVER])  
    fen.blit(msg_clic, (255, 55))

def afficher_elements_win():
    fen.blit(petit_joueur, (420, 20))
    fen.blit(petit_homerwinleft, (460, 140))
    fen.blit(petit_victory, (195, 140))
    fen.blit(petit_presentateur, (120, 20))
    fen.blit(petit_homerwinright, (20, 140))
    pygame.draw.rect(fen, ORANGE, rect_orange)
    fen.blit(msg_replay, (272, 57))
    
def afficher_elements_game_over():
    fen.blit(petit_joueur, (420, 20))
    fen.blit(petit_explo, (420, 140))
    fen.blit(petit_homerdoh, (250, 280))
    fen.blit(petit_game_over, (195, 140))
    fen.blit(petit_presentateur, (120, 20))
    fen.blit(petit_explo, (50, 140))
    pygame.draw.rect(fen, ORANGE, rect_orange)
    fen.blit(msg_replay, (272, 57))
    
def afficher_elements_choice():
    fen.blit(petit_joueur, (520, 150))
    fen.blit(petit_presentateur, (20, 150))
    pygame.draw.rect(fen, BLUE, rect_blue_choice)
    pygame.draw.rect(fen, ORANGE, rect_orange_choice)
    pygame.draw.rect(fen, RED, rect_red_choice)
    fen.blit(msg_easy, (280, 80))
    fen.blit(msg_medium, (270, 180))
    fen.blit(msg_hard, (280, 280))
    
# Démarrer l'état du jeu
# Super variable (début, choix_difficultes, en_cours, win, game_over) :
etat_jeu = "debut"
continuer = True
    
# Boucle du jeu :
while continuer:
     
# Option quitter par la croix :
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False


# Partie affichage :pygame.mixer.music.stop()
    fen.blit(fond, (0, 0))
    if etat_jeu == "debut" :
        afficher_elements_begin()
    elif etat_jeu == "choix_difficultes" :
        afficher_elements_choice()
    elif etat_jeu == "en_cours_easy" :
        resultat = game_mode_facile.going_boom_facile()
        if resultat == False:
            etat_jeu = "game_over"
        else:
            etat_jeu = "win"
    elif etat_jeu == "en_cours_medium" :
        resultat = game_mode_medium.going_boom_medium()
        if resultat == False:
            etat_jeu = "game_over"
        else:
            etat_jeu = "win"
    elif etat_jeu == "en_cours_hard" :
        # Affichage joueur de la partie
        resultat = game_mode_hard.going_boom_hard()
        if resultat == False:
            etat_jeu = "game_over"
        else:
            etat_jeu = "win"
    elif etat_jeu == "win" :
        afficher_elements_win()
    elif etat_jeu == "game_over" :
        afficher_elements_game_over()
        
        
# Partie fonctionnelle :

    if etat_jeu == "debut" :
        pygame.mixer.music.load("suspend-sound.mp3")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if rect_orange.collidepoint(event.pos):
                    pygame.mixer.music.play()
                    etat_jeu = "choix_difficultes"
                    
    elif etat_jeu == "choix_difficultes" :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if rect_blue_choice.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("punch-a-rock.mp3")
                    pygame.mixer.music.play()
                    etat_jeu = "en_cours_easy"
                    
                elif rect_orange_choice.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("punch-a-rock.mp3")
                    pygame.mixer.music.play()
                    etat_jeu = "en_cours_medium"
                   
                elif rect_red_choice.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("punch-a-rock.mp3")
                    pygame.mixer.music.play()
                    etat_jeu = "en_cours_hard"
                                               

    if etat_jeu == "win" :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if rect_orange.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("transition-base.mp3")
                    pygame.mixer.music.play()
                    etat_jeu = "choix_difficultes"
                    
    elif etat_jeu == "game_over" :
        for event in pygame.event.get():
            pygame.mixer.music.stop()
            pygame.mixer.music.load("explosion.mp3")
            pygame.mixer.music.play()
            if event.type == pygame.MOUSEBUTTONUP:               
                if rect_orange.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("transition-base.mp3")
                    pygame.mixer.music.play()
                    etat_jeu = "choix_difficultes"
           
    # Mettre à jour l'affichage    
    pygame.display.flip()

pygame.quit()       
        
        
        
        
        