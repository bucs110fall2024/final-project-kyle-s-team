import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, player, collision_sprites, scale_factor=0.1):
        super().__init__(groups)
        self.image = pygame.image.load("assets/EnemyIdle/idle_0.png")
        self.player = player
        self.frames = [pygame.transform.scale(frame, 
                      (int(frame.get_width() * scale_factor), int(frame.get_height() * scale_factor))) 
                      for frame in frames]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.animation_speed = 6

        self.rect = self.image.get_rect(center = pos)
        self.hitbox_rect = self.rect.inflate(-50, -80)
        self.collision_sprites = collision_sprites
        self.direction = pygame.Vector2()
        self.speed = 200

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def move(self, dt):
        """""
        Moves the enemy, gets it direction and updates rect position
        Includes collision logic
        """""
        player_pos = pygame.Vector2(self.player.rect.center)
        enemy_pos = pygame.Vector2(self.rect.center)
        direction = player_pos - enemy_pos
        if direction.length() > 0:
            self.direction = direction.normalize()  #Vector math that allows for consitent movement
        else:
            self.direction = pygame.Vector2(0, 0)

        # self.rect.center += self.direction * self.speed * dt
        self.rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        self.rect.y += self.direction.y * self.speed * dt
        self.collision("vertical")

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                elif direction == "vertical":
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

    def destroy(self):
        self.kill()
    
    def update(self, dt):
        self.move(dt)
        self.animate(dt)