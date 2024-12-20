import pygame
import random
import json

from src.player import Player
from src.gun import Gun
from src.enemy import Enemy
from src.sprites import *
from pytmx.util_pygame import load_pygame
from src.groups import AllSprites

from os.path import join
from os import path
from os import walk

class Controller():
    def __init__(self):
        """
        Initialize all of the important aspects of this controller class.
        """
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
        pygame.time.set_timer(self.enemy_event, 400)
        self.spawn_positions = []

        #Audio
        self.collision_sound = pygame.mixer.Sound("assets/Sounds/Sound_Effect_1.wav")
        self.collision_sound.set_volume(0.1)
        self.select_sound = pygame.mixer.Sound("assets/Sounds/Sound_Effect_2.wav")
        self.select_sound.set_volume(0.5)
        self.shoot_sound = pygame.mixer.Sound("assets/Sounds/Sound_Effect_3.wav")
        self.shoot_sound.set_volume(0.2)
        self.death_sound = pygame.mixer.Sound("assets/Sounds/Sound_Effect_4.wav")
        self.death_sound.set_volume(0.8)
        self.music = pygame.mixer.Sound("assets/Sounds/Music.wav")
        self.music.set_volume(0.5)

        #Score
        self.score = 0
        self.high_score = self.load_high_score()
        self.font = pygame.font.SysFont("Arial", 30)

        self.load_image()
        self.setup()
        self.on_main = True
        
        
    def load_high_score(self):
        """
        Load the high score from a JSON file.
        """
        if path.exists("high_scores.json"):
            with open("high_scores.json", "r") as file:
                file_content = file.read().strip()  # Read and strip any extra whitespace

                if not file_content:  # If the file is empty, reset it with the default value
                    self.create_default_high_score()
                    return 0
                
                try:
                    data = json.loads(file_content)  # Load valid JSON data
                    return data.get("high_score", 0)
                except json.JSONDecodeError:
                    # If the file contains invalid JSON, reset it with the default value
                    self.create_default_high_score()
                    return 0
        else:
            # If the file doesn't exist, create it with a default high score
            self.create_default_high_score()
            return 0

    def create_default_high_score(self):
        """
        Create a default high score file.
        """
        data = {"high_score": 0}
        with open("high_scores.json", "w") as file:
            json.dump(data, file)

    def save_high_score(self):
        """
        Saves new high score to JSON file
        """
        with open("high_scores.json", "w") as file:
            json.dump({"high_score": self.score}, file)
    
    def update_high_score(self):
        """
        Update high score if current score is higher
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()  # Save the new high score to the JSON file


    #Set up images in my controller that will need to be instantiated
    def load_image(self):
        """
        Sets up images to be used later
        """
        self.bullet_surface = pygame.image.load("assets/Gun/bullet.png").convert_alpha()
        self.bullet_surface = pygame.transform.scale(self.bullet_surface, (30, 30))

            # Load enemy frames from assets/EnemyWalk/
        self.enemy_frames = []
        enemy_folder_path = join('assets', 'EnemyWalk')

        for _, _, file_names in walk(enemy_folder_path):
            for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                if file_name.endswith('.png'):  # Ensure only PNG files are loaded
                    full_path = join(enemy_folder_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.enemy_frames.append(surf)

    def main_menu(self):
        """
        Creates the main menu that you see when booting up the game.
        """
        WINDOW_WIDTH = 1280
        self.on_main = True

        menu_font = pygame.font.SysFont("Arial", 50)
        option_font = pygame.font.SysFont("Arial", 30)

        title_text = menu_font.render("Vampire Survivors", True, (255, 0, 0))
        instructions_text = option_font.render("Press P to Start | Press Q to Quit", True, (0, 0, 0))
        
        self.screen.fill((0, 0, 255))

        title_x = (WINDOW_WIDTH - title_text.get_width()) // 2
        title_y = 150
        self.screen.blit(title_text, (title_x, title_y))

        # Center the instructions text
        instructions_x = (WINDOW_WIDTH - instructions_text.get_width()) // 2
        instructions_y = 300
        self.screen.blit(instructions_text, (instructions_x, instructions_y))

        pygame.display.update()

        # Wait for user input to start or quit
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.select_sound.play() 
                        self.music.play(loops = -1)
                        self.on_main = False
                        return
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()


    def game_over_screen(self):
        """
        Creates the game over screen for when you die.
        """
        WINDOW_WIDTH = 1280

        game_over_font = pygame.font.SysFont("Arial", 50)
        restart_font = pygame.font.SysFont("Arial", 30)
        reset_font = pygame.font.SysFont("Arial", 30)

        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        score_text = self.font.render("High Score: " + str(self.score), True, (255, 0, 0))
        high_score_text = self.font.render("High Score: " + str(self.high_score), True, (255, 0, 0))
        restart_text = restart_font.render("Press R to Restart or Q to Quit", True, (0, 0, 0))
        reset_text = reset_font.render("Press X to Reset High Score and Restart", True, (0, 0, 0))

        self.screen.fill((255, 255, 255))

        # Blit the text to the screen
        self.screen.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, 150))
        self.screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 250))
        self.screen.blit(high_score_text, (WINDOW_WIDTH // 2 - high_score_text.get_width() // 2, 300))
        self.screen.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, 400))
        self.screen.blit(reset_text, (WINDOW_WIDTH // 2 - reset_text.get_width() // 2, 450))

        pygame.display.update()

        # Wait for user input to restart or quit
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.select_sound.play()  
                        self.restart_game()
                    elif event.key == pygame.K_q: 
                        self.select_sound.play() 
                        pygame.quit()
                    elif event.key == pygame.K_x:
                        self.select_sound.play() 
                        self.reset_high_score()

    def reset_high_score(self):
        """
        Reset high score if you want to during the game over screen.
        """
        self.high_score = 0
        self.save_high_score()
        self.restart_game()

    def restart_game(self):
        """
        Restart the game by emptying all of the current sprites.
        """
        self.score = 0
        self.running = True
        self.all_sprites.empty()
        self.enemy_sprites.empty()
        self.collision_sprites.empty()
        self.bullet_sprites.empty()

        # Reload the game setup
        self.setup()
        self.mainloop()  # Start the game loop again

    def input(self):
        """
        Checks for when player inputs a command on their keyboard.
        """
        if pygame.mouse.get_pressed()[0] and self.can_shoot: #Left mouse button is index 0
            self.shoot_sound.play()
            pos = self.gun.rect.center + self.gun.player_direction * 50
            Bullet(self.bullet_surface, pos, self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def gun_reload_timer(self):
        """
        Makes sure you can't just spam bullets and lag out the game.
        """
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_reload:
                self.can_shoot = True

    def setup(self):
        """
        Sets up the tilemap.
        """
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
        """
        Checks if bullets collide with enemies and deletes the enemy if there is a collision.
        """
        for bullet in self.bullet_sprites:
            #Check collision with each enemy
            for enemy in self.enemy_sprites:
                if not enemy.is_dead and pygame.sprite.collide_rect(bullet, enemy):  #Check if the bullet collides with the enemy
                    self.collision_sound.play()
                    enemy.destroy()
                    bullet.kill()
                    self.score += 1
                    break

    def player_collision(self):
        """
        Checks if player collide with enemies and sets up game over.
        """
        colliding_enemies = pygame.sprite.spritecollide(self.player, self.enemy_sprites, False, pygame.sprite.collide_mask)
        for enemy in colliding_enemies:
            if enemy.is_active:
                self.music.set_volume(0)
                self.death_sound.play()
                #Call the game over screen after a short delay
                pygame.time.delay(3000)
                self.music.set_volume(0.5)
                self.game_over_screen()

    #Game loop
    def mainloop(self):
        """
        Runs throughout the whole game.
        """
        while self.running:
            #Check if game started yet
            if self.on_main:
                self.main_menu()
                continue
            #Handle events
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
            self.player_collision()

            self.all_sprites.draw(self.player.rect.center)
            
            # Render the score
            self.update_high_score()
            score_text = self.font.render("Score: " + str(self.score), True, (255, 0, 255))
            self.screen.blit(score_text, (10, 10)) 
            high_score_text = self.font.render("High Score: " + str(self.high_score), True, (255, 0, 0))
            self.screen.blit(high_score_text, (10, 40))

            pygame.display.update()


    # Quit pygame
    pygame.quit()