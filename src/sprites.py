import pygame

class SpriteCollision(pygame.sprite.Sprite):
    def __init__(self, pos, surface, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surface, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)

# class Gun(pygame.sprite.Sprite):
#     def __init__(self, player, groups):
#         self.player = player
#         self.distance = 140
#         self.player_direction = pygame.Vector2(1, 0)

#         super().__init__(groups)
#         self.gun_surface = pygame.image.load("assets/Gun/gun.png").convert_alpha()
#         self.image = self.gun_surface
#         self.rect = self.image.get_rect(center = self.player.rect.center + self.player_direction * self.distance)