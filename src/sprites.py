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

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surface, pos, direction, groups):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(center = pos)
        