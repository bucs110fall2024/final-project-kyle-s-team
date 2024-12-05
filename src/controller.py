import pygame
import random

from src.player import Player
from src.gun import Gun
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
        self.load_image()

        #Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()

        self.setup()
        
        #Timer to shoot gun
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_reload = 100

    #Set up images in my controller that will need to be instantiated
    def load_image(self):
        self.bullet_surface = pygame.image.load("assets/Gun/bullet.png").convert_alpha()
        

    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot: #Left mouse button is index 0
            pos = self.gun.rect.center + self.gun.player_direction * 50
            Bullet(self.bullet_surface, pos, self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()


    def gun_reload_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_reload:
                self.can_shoot = True

    def setup(self):
        TILE_SIZE = 48
        map = load_pygame("assets/world.tmx")
        
        #Ground/Background
        for x, y, image in map.get_layer_by_name("Tile Layer 1").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        #Walls
        for obj in map.get_layer_by_name("Object Layer 1"):
            SpriteCollision((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
    
        #Spawn points
        for obj in map.get_layer_by_name("Object Layer 2"):
            if obj.name == "Player":
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
                self.gun = Gun(self.player, self.all_sprites)

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

            # Update the game
            self.gun_reload_timer()
            self.input()
            self.all_sprites.update(delta_time)

            # Draw all sprites to the screen
            self.all_sprites.draw(self.player.rect.center)

            # Update the display
            pygame.display.update()


    # Quit pygame
    pygame.quit()