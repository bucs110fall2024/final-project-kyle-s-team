import pygame

class Gun(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        self.player = player
        self.distance = 140
        self.player_direction = pygame.Vector2(1, 0)

        super().__init__(groups)
        self.gun_surface = pygame.image.load("assets/Gun/gun.png").convert_alpha()
        self.image = self.gun_surface
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(center = self.player.rect.center + self.player_direction * self.distance)


    def update(self, _):
        self.rect.center = self.player.rect.center + self.player_direction * self.distance

    def bullet(self):
        """
        Bullet moves in a straight line in a while loop until it collides 
        with a object. Collision with the player wouldn't count, as
        then the bullet would be deleted as soon because it
        spawns within the player's hitbox.
        """

    def rotate(self):
        """
        Rotate gun based on direction needed to shoot
        """