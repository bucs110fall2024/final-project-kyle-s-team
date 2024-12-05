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
        self.hitbox_rect = self.rect.inflate(-20, -40)
        self.collision_sprites = collision_sprites
        self.direction = pygame.Vector2()
        self.speed = 300

    def move(self):
        """
        Move enemy towards player
        Create player position and enemy position variables to get both,
        using vectors I'll determine which direction the enemy should move
        """