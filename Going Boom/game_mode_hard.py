import pygame

def going_boom_hard():    # Couleurs qui seront utilisées dans le jeu
    WHITE = (255, 255, 255)
    COULEUR_COMPTEUR = (53, 200, 23)
    COULEUR_FOND = (255, 255, 255)

    # FPS = frame per second (images par seconde)
    FPS = 60
    compteur_frame = 0
    timer = 60

    # Appel des fonctions de pygame
    pygame.init()

    # Font utilisée dans le jeu
    police = pygame.font.Font("AAhaWow-2O1K8.ttf", 30)

    # Appel du temps par la fonction time de pygame
    horloge = pygame.time.Clock()

    # Chargement de l'image du fond
    fondjeu = pygame.image.load("fond.jpg")
    #print("Dimension de l'image de fond", fondjeu.get_size())
    fondjeu.set_alpha(200)

    # Les dimensions de la fenêtre sont celles de l'image du fond
    LARGEUR, HAUTEUR = fondjeu.get_size()
    # Dimensions du rectangle de questions/réponses
    LARGEUR_REC = 572
    HAUTEUR_REC = 80
    
    largeur_rec_restart = 40
    hauteur_rec_restart = 40
    
    # Initialisation de la fenêtre pygame
    fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Projet")
    fen.fill(COULEUR_FOND)

    # Préparation de l'image du bambou à son utilisation dans pygame
    fondjeu = fondjeu.convert()

    # Chargement et préparation des sprites utilisés
    joueur = pygame.image.load("joueur.png").convert()
    #print("Dimension de l'image du joueur", joueur.get_size())
    
    croix = pygame.image.load("croix_difficulte.png").convert()
    petite_croix = pygame.transform.scale(croix, (croix.get_width() // 5, croix.get_height() // 5))
    
    petit_joueur = pygame.transform.scale(joueur, (joueur.get_width() // 9, joueur.get_height() // 9))
    petit_joueur = petit_joueur.convert_alpha()

    presentateur = pygame.image.load("presentateur.png").convert()
    presentateur.set_colorkey((0, 0, 0))  # Remplace la couleur (0, 0, 0) - Noir en transparence

    petit_presentateur = pygame.transform.scale(presentateur, (presentateur.get_width() // 13, presentateur.get_height() // 13))
    petit_presentateur = petit_presentateur.convert_alpha()
    print("Dimension de l'image du presentateur", presentateur.get_size())

    bomb_images = [pygame.image.load(f"bombe_{i}.svg").convert_alpha() for i in range(1, 11)]
    reduced_bomb_images = [pygame.transform.scale(image, (image.get_width() // 3, image.get_height() // 3)) for image in
                          bomb_images]

    question_index = 0
    reponse = ""
    # Nos questions
    questions = [
        "Quel Chateau de l'oise peut on visiter le musee Conde?",
        "Quel est le nom d'une bouteille de champagne de 12L",
        "Quelle est la longueur d'un marathon ? en km",
        "Quel fruit fait la fierté de la ville de Marmande ?",
        "Quel fils de Zeus est le protecteurs des marchands des voyageurs et des voleurs ?",
        "Quel est le nom de la femelle du sanglier ?",
        "Quel est le chef-lieu de la region Bourgogne ?",
        "Quel est l'os le plus petit du corps humain ?",
        "Quel film est traduit au Quebec 'Brillantine' ?",
        "Dans quel jeu de cartes existe 'l'excuse' ?",
        "Sur quoi repose le test de Rorschach ?",
    ]
    # Nos réponses
    reponses = ["chateau de Chantilly", "un Balthazar", "42","la tomate","Hermes","la Laie","Dijon" ,"l'etrier","Grease","le tarot","les taches d'encre"]
    # Choix de la taille de caractère et la font du texte écrit dans l'interface
    font = pygame.font.Font("AAhaWow-2O1K8.ttf", 12)
    # Variable pour que la question s'affiche dans l'interface
    texte_question = font.render(questions[question_index], True, (255, 11, 11))
    # Définition de la position du rectangle dans lequel la question apparaîtra
    rect_question = texte_question.get_rect(center=(220, 320))
    rect_restart = pygame.Rect(10, 10, largeur_rec_restart, hauteur_rec_restart)
    message_feedback = ""  # Initialisez un message de feedback vide
    message_duration = 60  # Durée en nombre de frames (environ 1 seconde à 60 FPS)
    message_frame = 0  # Initialisation du compteur de frames pour le message
    continuer = True
    victoire = False
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    reponse = reponse[:-1]
                elif event.key == pygame.K_RETURN:
                    if reponse.lower() == reponses[question_index].lower():
                        message_feedback = "Bonne reponse"
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("bicycle-bell.mp3")
                        pygame.mixer.music.play()
                        question_index += 1
                    else:
                        message_feedback = "Mauvaise reponse"
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("error.mp3")
                        pygame.mixer.music.play()
                        timer -= 8
                    reponse = ""
                    if question_index < len(questions):
                        texte_question = font.render(questions[question_index], True, (255, 11, 11))
                    else:
                        print("Toutes les questions sont terminées.")
                        victoire = True
                        continuer = False
                elif event.unicode != '':
                    reponse += event.unicode

        if timer <= 0:
            victoire = False
            continuer = False

        fen.blit(fondjeu, (0, 0))
        fen.blit(petit_joueur, (350, 100))
        fen.blit(petit_presentateur, (150, 120))

        pygame.draw.rect(fen, WHITE, [20, HAUTEUR - HAUTEUR_REC, LARGEUR_REC, HAUTEUR_REC])
        index_image = max(0, (timer - 1) // 12)
        fen.blit(reduced_bomb_images[index_image], (270, 220))
        msg_compteur = police.render(f"{timer:02d}", True, COULEUR_COMPTEUR)
        fen.blit(msg_compteur, (270, 20))
        fen.blit(texte_question, rect_question)

        texte_reponse = font.render(reponse, True, (0, 0, 0))
        rect_reponse = texte_reponse.get_rect(center=(300, 350))
        fen.blit(texte_reponse, rect_reponse.topleft)
        pygame.draw.rect(fen, WHITE, rect_restart)
        fen.blit(petite_croix, (10,10))
        
        if message_frame < message_duration:
            if message_feedback == "Mauvaise reponse":
                couleur = (255, 0, 0)  # Rouge pour "Mauvaise réponse"
            else:
                couleur = (0, 255, 0)  # Vert pour "Bonne réponse"
            message_surface = font.render(message_feedback, True, couleur)
            if message_feedback:
                message_rect = message_surface.get_rect(center=(290, 100))
                fen.blit(message_surface, message_rect)
            message_frame += 1
        else:
            message_feedback = ""  # Effacer le message après la durée spécifiée
            message_frame = 0

        pygame.display.flip()
        compteur_frame += 1
        if compteur_frame == FPS:
            timer -= 1
            compteur_frame = 0

        horloge.tick(FPS)
    return victoire
    
if __name__ == "__main__":
    going_boom_facile()
    pygame.quit()