import pygame
from src.player import Player
from src import gun
from src import enemy


def Controller():
    # Initialize pygame
    pygame.init()

    # Setup window
    WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Vampire Survivors Type Game")

    # Setup clock for controlling frame rate
    clock = pygame.time.Clock()

    # Create sprite group
    all_sprites = pygame.sprite.Group()

    # Create player instance at position (400, 300) and add to sprite group
    player_instance = Player((400, 300), all_sprites)

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen (black background)
        screen.fill((0, 0, 0))

        # Update all sprites (not needed in this simple case, but can be useful)
        all_sprites.update()

        # Draw all sprites to the screen
        all_sprites.draw(screen)

        # Update the display
        pygame.display.update()

        # Control frame rate (60 FPS)
        clock.tick(60)

    # Quit pygame
    pygame.quit()