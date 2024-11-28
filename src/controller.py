import pygame
from src.player import Player
from src.gun import Gun
from src.enemy import Enemy

class Controller:

    def __init__(self):
        #self.clouds = pygame.sprite.Group() --> list that only holds sprites
        #self.enemy = pygame.sprite.Group()
        pygame.init()
        pygame.event.pump()
        self.screen = pygame.display.set_mode()

        """
        Setup all pygame stuff and initilizes objects
        """
    def mainloop(self):
        #pygame.sprite.spritecollide(player, self.enemy, True) --> return a list of all collisions, delete things that collide with it with True
        """
        Select state loop
        """
    # while(True):
    #     #1. Handle events
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             exit()

      #2. detect collisions and update models

      #3. Redraw next frame

      #4. Display next frame
        # pygame.display.flip()