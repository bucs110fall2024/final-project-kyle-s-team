Team members - None
Project Description - I'm gonna create a game in the style of a game called "Vampire Survivors" where your character automatically shoots at nearby enemies, so your goal is to run around and not get hit by the enemies.
Features - 1. Start menu 2. Enemies with collision 3. Movable player (topdown) 4. Gun that shoots bullets at enemies 5. Game over screen

Credit:

All artwork and animations (CC0) - https://rgsdev.itch.io/free-cc0-modular-animated-vector-characters-2d
Sound effects - Made by me with the software LabChirp
Music - Made by me with the software Famistudio

    Test Case 1: Player Movement

        Test Description: Verify that the player can move in all 4 directions.
        Test Steps:
            1. Start the game.
            2. Press the left arrow key.
            3. Verify that the player moves left.
            4. Press the right arrow key.
            5. Verify that the player moves right.
            6. Press the up arrow key.
            7. Verify that the player moves up.
            6. Press the down arrow key.
            7. Verify that the player moves down.
        Expected Outcome: The player's spaceship should move in one of four directions in response to the arrow key inputs.

    Test Case 2: Collision Detection - Bullets

        Test Description: Verify that the player can move in all 4 directions.
        Test Steps:
            1. Start the game.
            2. Fire a bullet towards an enemy.
            3. Verify that the bullet hits the enemy's hitbox.
            4. Fire a bullet that misses every enemy.
            5. Verify that no enemy collision is detected, although other collisions may occur, such as with a wall that causes the bullet to despawn.
        Expected Outcome: The bullets should collide with enemy's properly and destroy both the enemy and bullet objects.

    Test Case 3: Game Over Condition

        Test Description: Confirm that the game ends when the player loses all health.
        Test Steps:
            1. Start the game.
            2. Play until the player loses all health.
            3. Verify that the game displays a "Game Over" message.
        Expected Outcome: The game should display a "Game Over" message when the player loses all health.
    
    Test Case 4: Menu Navigation

        Test Description: Test the navigation through the game's main menu.
        Test Steps:
            1. Start the game.
            2. Navigate through the main menu options (Start Game, Quit).
            3. Verify that each option is selectable and leads to the expected actions.
        Expected Outcome: The main menu should allow the player to navigate through options and select them.

    Test Case 5: Collision - Player

        Test Description: Test how the player interacts with enemies and walls.
        Test Steps:
            1. Start the game.
            2. Get hit by an enemy.
            3. Verify that the player loses health.
            4. Run into a wall.
            5. Verify that the player stops moving forward (repeat for each direction).
            6. Verify the player can't collide with objects such as their own bullets.
        Expected Outcome: Player could only interact with specific objects and do so in specific ways.
