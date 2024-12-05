import pygame

class SpriteCollision(pygame.sprite.Sprite):
    def __init__(self, pos, surface, groups):
        """
        Initialize all information about the general sprite collisions throughout the game.
        """
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surface, groups):
        """
        Initialize all information about the general sprites throughout the game.
        """
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, surface, pos, direction, groups):
        """
        Initialize all information about the bullet that shoots out of the gun.
        Class is small enough that it feels justified to put it with these other two.
        """
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(center = pos)
        self.spawn_timer = pygame.time.get_ticks()
        self.despawn_time = 1000

        self.direction = direction
        self.speed = 1000
        
    def update(self, dt):
        """
        Move bullet object across the screen and then despawn.
        """
        self.rect.center += self.direction * self.speed * dt
        
        if pygame.time.get_ticks() - self.spawn_timer >= self.despawn_time:
            self.kill()
            self.active = True