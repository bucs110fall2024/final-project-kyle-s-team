import pygame
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, img_file):
        super().__init__()
        #self.image = pygame.image.load(f"assets/{name}.png")
        #self.rect = self.image.get_rect()
        """
        Initialize player:
        - x: int - starting x coordinate
        - y: int - starting y coordinate
        - img_file: str - path to img file
        """

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