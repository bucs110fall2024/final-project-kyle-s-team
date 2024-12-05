import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, player, collision_sprites, scale_factor=0.08):
        super().__init__(groups)
        self.image = pygame.image.load("assets/EnemyIdle/idle.png")
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
        self.speed = 150

        #Death Timer
        self.death_time = 0
        self.death_duration = 400

        #Delay collision detection to avoid instakills
        self.spawn_time = pygame.time.get_ticks()
        self.delay_time = 800

    def animate(self, dt):
        if pygame.time.get_ticks() - self.spawn_time >= self.delay_time:
            self.frame_index += self.animation_speed * dt
            self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def move(self, dt):
        """""
        Moves the enemy, gets it direction and updates rect position
        Includes collision logic
        """""
        if pygame.time.get_ticks() - self.spawn_time >= self.delay_time: 
            player_pos = pygame.Vector2(self.player.rect.center)
            enemy_pos = pygame.Vector2(self.rect.center)
            direction = player_pos - enemy_pos
            if direction.length() > 0:
                self.direction = direction.normalize()  #Vector math that allows for consitent movement
            else:
                self.direction = pygame.Vector2(0, 0)

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
        self.death_time = pygame.time.get_ticks()
        surface = pygame.mask.from_surface(self.frames[0]).to_surface()
        surface.set_colorkey("black")
        self.image = surface

    def death_timer(self):
        if pygame.time.get_ticks() - self.death_time >= self.death_duration:
            self.kill()
    
    def update(self, dt):
        if self.death_time == 0:
            self.move(dt)
            self.animate(dt)
        else:
            self.death_timer()