import pygame
import random

from src.player import Player
from src.gun import Gun
from src.enemy import Enemy
from src.sprites import *
from pytmx.util_pygame import load_pygame
from src.groups import AllSprites

from os.path import join
from os import walk

class Controller():
    def __init__(self):
        """""
        Initialize all of the important aspects of this controller class.
        """""
        pygame.init()
        WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivors Type Game")
        self.clock = pygame.time.Clock()
        self.running = True

        #Groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        
        #Timer to shoot gun
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_reload = 100

        #Timer to load enemies at a random starting position
        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, 300)
        self.spawn_positions = []

        self.load_image()
        self.setup()

    #Set up images in my controller that will need to be instantiated
    def load_image(self):
        """""
        Sets up images to be used later
        """""
        self.bullet_surface = pygame.image.load("assets/Gun/bullet.png").convert_alpha()

            # Load enemy frames from assets/EnemyWalk/
        self.enemy_frames = []
        enemy_folder_path = join('assets', 'EnemyWalk')

        for _, _, file_names in walk(enemy_folder_path):
            for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                if file_name.endswith('.png'):  # Ensure only PNG files are loaded
                    full_path = join(enemy_folder_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.enemy_frames.append(surf)
    def input(self):
        """""
        Checks for when player inputs a command on their keyboard
        """""
        if pygame.mouse.get_pressed()[0] and self.can_shoot: #Left mouse button is index 0
            pos = self.gun.rect.center + self.gun.player_direction * 50
            Bullet(self.bullet_surface, pos, self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()


    def gun_reload_timer(self):
        """""
        Makes sure you can't just spam bullets and lag out the game
        """""
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_reload:
                self.can_shoot = True

    def setup(self):
        """""
        Sets up the tilemap
        """""
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
            else:
                self.spawn_positions.append((obj.x, obj.y))

    def bullet_collision(self):
        """""
        Checks if bullets collide with enemies and deletes the enemy if there is a collision
        """""
        for bullet in self.bullet_sprites:
            if bullet.active:
                # Check collision with each enemy
                for enemy in self.enemy_sprites:
                    if pygame.sprite.collide_rect(bullet, enemy):  # Check if the bullet collides with the enemy
                        bullet.deactivate()
                        enemy.destroy()
                        break

    # Game loop
    def mainloop(self):
        """""
        Runs throughout the whole game
        """""
        while self.running:
         # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == self.enemy_event:
                    if self.spawn_positions and self.enemy_frames:
                        Enemy(
                            random.choice(self.spawn_positions),
                            self.enemy_frames,  # Pass the list of frames
                            (self.all_sprites, self.enemy_sprites),
                            self.player,
                            self.collision_sprites,
                        )
            delta_time = self.clock.tick() / 1000
        
            # Clear the screen (green background)
            self.screen.fill((0, 255, 0))

            # Update the game
            self.gun_reload_timer()
            self.input()
            self.all_sprites.update(delta_time)
            self.bullet_collision()

            # Draw all sprites to the screen
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()


    # Quit pygame
    pygame.quit()