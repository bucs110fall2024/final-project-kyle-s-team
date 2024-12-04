import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("assets/PlayerIdle/idle_0.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = pos  # Position the player sprite



    def move(self):
        """
        Get whatever key is pressed and determine the direction to move
        based on that key. Direction stored in a variable.
        """

    def collision(self, direction):
        """
        See if player's hitbox collides with another object, like a wall
        or an enemy. Use direction variable so you move in the correct
        direction when a collision occurs.
        """

    def shoot(self):
        """
        Creates a bullet object and returns Bullet
        """