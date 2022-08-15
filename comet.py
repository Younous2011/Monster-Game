import pygame
import random
from monster import *

# creer une classe pour gérer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # définir l'image associé à cette comete
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # joueur le son
        self.comet_event.game.sound_manager.play('meteorite')

        # verifier si le nombre de comettes est de 0
        if len(self.comet_event.all_comets) == 0:
            print("L'evenement est fini")
            # remetttre la barre à 0
            self.comet_event.reset_percent()
            # apparaitre les 2 premiers monstres
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("Sol")
            # retirer la boule de feu
            self.remove()

            # si il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0:
                print("L'evenement est fini")
                # remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verfiier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print("Joueur touché !")
            # retirer la boule de feu
            self.remove()
            # subir 20 points de degats
            self.comet_event.game.player.damage(20)