class Gun:

    def __init__(self, x, y, img_file):
        """
        Initialize player:
        - x: int - starting x coordinate (depending on where player shoots)
        - y: int - starting y coordinate (depending on where player shoots)
        - img_file: str - path to img file
        """

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