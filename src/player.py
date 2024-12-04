import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("assets/PlayerIdle/idle_0.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.direction = pygame.Vector2(1, 0)
        self.speed = 400



    def input(self):
        #Player control
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] - int(keys[pygame.K_LEFT]))
        self.direction.y = int(keys[pygame.K_DOWN] - int(keys[pygame.K_UP]))
        #Fix diagonal speed
        if self.direction:
            self.direction = self.direction.normalize()


    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)

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