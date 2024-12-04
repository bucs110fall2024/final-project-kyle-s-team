import pygame
from src.player import Player
from src import gun
from src import enemy


class Controller():
    def __init__(self):
        pygame.init()
        WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vampire Survivors Type Game")
        self.clock = pygame.time.Clock()
        self.running = True


        self.all_sprites = pygame.sprite.Group()
        self.player = Player((400, 300), self.all_sprites)

    # Game loop
    def mainloop(self):
        while self.running:
         # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            delta_time = self.clock.tick() / 1000
        
            # Clear the screen (green background)
            self.screen.fill((0, 255, 0))

       
            self.all_sprites.update(delta_time)

            # Draw all sprites to the screen
            self.all_sprites.draw(self.screen)

            # Update the display
            pygame.display.update()


    # Quit pygame
    pygame.quit()