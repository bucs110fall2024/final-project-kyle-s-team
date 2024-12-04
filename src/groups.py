import pygame

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()
    
    def draw(self, target_pos):
        WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
        self.offset.x = -(target_pos[0] - WINDOW_HEIGHT / 2)
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)