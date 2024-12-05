import pygame

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        """
        Initialize all information about the sprites.
        """
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

        #Level boundaries
        self.level_width = 1440
        self.level_height = 960
    
    #Camera
    def draw(self, target_pos):
        """
        Includes the math for the camera. Includes camera limits using offset.
        """
        WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)

        self.offset.x = max(min(self.offset.x, 0), -(self.level_width - WINDOW_WIDTH))
        self.offset.y = max(min(self.offset.y, 0), -(self.level_height - WINDOW_HEIGHT))

        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)