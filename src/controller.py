import pygame
import random

from src.player import Player
from src import gun
from src import enemy
from src.sprites import *
from pytmx.util_pygame import load_pygame
from src.groups import AllSprites

class Controller():
    def __init__(self):
        pygame.init()
        WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivors Type Game")
        self.clock = pygame.time.Clock()
        self.running = True

        #Groups
        # self.all_sprites = pygame.sprite.Group()
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()
        
        #Sprites
        self.player = Player((300, 300), self.all_sprites, self.collision_sprites)


    def setup(self):
        TILE_SIZE = 48
        map = load_pygame("assets/world.tmx")
        
        #Ground/Background
        for x, y, image in map.get_layer_by_name("Tile Layer 1").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        #Walls
        for obj in map.get_layer_by_name("Object Layer 1"):
            SpriteCollision((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
    
    # Game loop
    def mainloop(self):
        while self.running:
         # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            delta_time = self.clock.tick() / 1000
        
            # Clear the screen (green background)
            self.screen.fill((0, 255, 0))

       
            self.all_sprites.update(delta_time)

            # Draw all sprites to the screen
            # self.all_sprites.draw(self.screen)
            self.all_sprites.draw(self.player.rect.center)

            # Update the display
            pygame.display.update()


    # Quit pygame
    pygame.quit()