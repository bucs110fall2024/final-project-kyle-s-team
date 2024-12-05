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
        self.spawn_timer = pygame.time.get_ticks()
        self.despawn_time = 1000

        self.direction = direction
        self.speed = 1000

        self.active = True #Bullet collision is being tracked

    def deactivate(self):
        """""
        Bullet has no more possible collisions after hitting an enemy
        """""
        self.active = False
        
    def update(self, dt):
        """""
        Move bullet object across the screen and then despawn
        """""
        self.rect.center += self.direction * self.speed * dt
        
        if pygame.time.get_ticks() - self.spawn_timer >= self.despawn_time:
            self.kill()