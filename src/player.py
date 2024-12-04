import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups, collision_sprites):

        super().__init__(groups)
        self.image = pygame.image.load("assets/PlayerIdle/idle_0.png")
        #self.image = pygame.image.load("assets/PlayerIdle/test.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = pos

        #Create new hitbox to fix broken sprite collisions
        self.hitbox_rect = self.rect.inflate(-150, -50)
        #self.hitbox_rect = self.rect.inflate(0, 0)

        #Player movement
        self.direction = pygame.Vector2(1, 0)
        self.speed = 400
        self.collision_sprites = collision_sprites

    def input(self):
        #Player control
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] - int(keys[pygame.K_LEFT]))
        self.direction.y = int(keys[pygame.K_DOWN] - int(keys[pygame.K_UP]))
        #Fix diagonal speed
        if self.direction:
            self.direction = self.direction.normalize()

    def move(self, dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision("vertical")
        self.rect.center = self.hitbox_rect.center

    def update(self, dt):
        self.input()
        self.move(dt)
        
    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == "horizontal":
                    if self.direction.x > 0:
                        self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.hitbox_rect.left = sprite.rect.right
                elif direction == "vertical":
                    if self.direction.y > 0:
                        self.hitbox_rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.hitbox_rect.top = sprite.rect.bottom
    def shoot(self):
        """
        Creates a bullet object and returns Bullet
        """