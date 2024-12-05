import pygame
from math import atan2, degrees

class Gun(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        self.player = player
        self.distance = 140
        self.player_direction = pygame.Vector2(0, 1)

        super().__init__(groups)
        self.gun_surface = pygame.image.load("assets/Gun/gun.png").convert_alpha()
        self.image = self.gun_surface
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(center = self.player.rect.center + self.player_direction * self.distance)
        self.current_angle = None
        #Adjust for sprite offsets
        self.offset = pygame.Vector2(15, 15)
        
    def rotate(self):
        """
        Rotate gun object based on direction needed to shoot
        """
        WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        #Vector math!
        direction = mouse_pos - player_pos
        self.player_direction = (mouse_pos - player_pos).normalize()
        if direction.length() != 0:
            self.direction = direction.normalize()
        else:
            self.direction = pygame.Vector2(0, 0)
        
    def rotate_sprite(self):
        """
        Rotate gun sprite based on direction needed to shoot
        Use trig to find how to properly rotate the sprite, must covert to degrees as it's in radians
        """

        angle = -degrees(atan2(self.player_direction.y, self.player_direction.x))
        
        # Update the sprite only if the angle has changed
        if angle != self.current_angle:
            self.current_angle = abs(angle)
            self.image = pygame.transform.rotozoom(self.gun_surface, angle, .1)
            self.rect = self.image.get_rect(center=self.player.rect.center + self.player_direction * self.distance + self.offset)

                                        
    def update(self, _):
        self.rotate()
        self.rotate_sprite()
        self.rect.center = self.player.rect.center + self.player_direction * self.distance

    def bullet(self):
        """
        Bullet moves in a straight line in a while loop until it collides 
        with a object. Collision with the player wouldn't count, as
        then the bullet would be deleted as soon because it
        spawns within the player's hitbox.
        """

