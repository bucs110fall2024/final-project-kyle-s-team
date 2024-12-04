import pygame

class SpriteCollision(pygame.sprite.Sprite):
    def __init__(self, pos, surface, groups):
        super().__init__(groups)
        # self.image = pygame.Surface(size)
        # self.image.fill("blue")
        self.image = surface
        self.rect = self.image.get_rect(center = pos)
        pygame.draw.rect(self.image, (255, 0, 0), self.rect, 2)