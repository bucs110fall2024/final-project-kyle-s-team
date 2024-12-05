import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("assets/PlayerIdle/idle_0.png")
        #self.image = pygame.image.load("assets/PlayerIdle/test.png")

        #Animation setup
        self.walk_cycle = [
            pygame.image.load("assets/PlayerWalk/walk_3.png").convert_alpha(), 
            pygame.image.load("assets/PlayerWalk/walk_5.png").convert_alpha(),
            pygame.transform.scale(pygame.image.load("assets/PlayerWalk/walk_3.png").convert_alpha(), (200, 200)),
            pygame.transform.scale(pygame.image.load("assets/PlayerWalk/walk_5.png").convert_alpha(), (200, 200)),
        ]

        self.frame_index = 0
        self.frame_delay = 100
        self.animation_speed = 100
        self.last_update = pygame.time.get_ticks()

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
        self.flipped = False

    def input(self):
        #Player control
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] - int(keys[pygame.K_LEFT]))
        self.direction.y = int(keys[pygame.K_DOWN] - int(keys[pygame.K_UP]))
        #Fix diagonal speed
        if self.direction.length() != 0:
            self.direction = self.direction.normalize()
        #Flip sprite
        if self.direction.x < 0 and not self.flipped:
            self.flipped = True
        elif self.direction.x > 0 and self.flipped:
            self.flipped = False

    def move(self, dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision("vertical")
        self.rect.center = self.hitbox_rect.center

    def animate(self, dt):
        now = pygame.time.get_ticks()
        if self.direction.length() > 0:
            if now - self.last_update > self.frame_delay:
                if self.frame_index <= 2:
                    self.frame_index += 1
                else:
                    self.frame_index = 1
                self.frame_index %= len(self.walk_cycle)
                if self.frame_index != 1:
                    self.image = self.walk_cycle[self.frame_index]
                    if self.flipped:
                        self.image = pygame.transform.flip(self.image, True, False)
                    self.last_update = now
        
    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
        
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
  