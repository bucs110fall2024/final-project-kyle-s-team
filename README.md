# << Vampire Survivors Recreation >>
## CS110 Final Project  << Fall, 2024 >>

## Team Members

<< Kyle Godzki >>

***

## Project Description

<< I created a game in the style of a game called "Vampire Survivors" where your character automatically shoots at nearby enemies, so your goal is to run around and not get hit by the enemies. >>

***

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

### Features

1. << Start menu >>
2. << Enemies with collision >>
3. << Movable player (topdown) >>
4. << Gun that shoots bullets at enemies >>
5. << Game over screen >>

Credit:

pytmx - installed using pip
All artwork and animations (CC0) - https://rgsdev.itch.io/free-cc0-modular-animated-vector-characters-2d
Tileset (CC0)- https://monsteretro.itch.io/willibabs-free-leftovers (Used the software Tiled in order to create the map, using a tutorial to see how to implement it with Python using pytmx)
Sound effects - Made by me with the software LabChirp
Music - Made by me with the software Famistudio

## ATP
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
            2. Fire a bullet towards a wall
            3. Verify that the bullet doesn't collide with the wall.
        Expected Outcome: The bullets should have specific collision use cases.

    Test Case 3: Camera

        Test Description: Confirm that the camera follows the player.
        Test Steps:
            1. Start the game.
            2. Move around and verify the camera follows the player in all directions.
            3. Stop moving.
            4. Verify that the camer stays in place when the player stops moving.
        Expected Outcome: The camera should follow the player no matter where they move to. The camera must stop moving when the player does.
    
    Test Case 4: Tilemap setup

        Test Description: Test that the tilemap works properly.
        Test Steps:
            1. Start the game.
            2. Make sure player can collide with objects of certain layers and not with others.
            3. Make sure tilemap sprites are shwoing up properly.
            4. Make sure that the tileset's spawn points work for entities like the player.
        Expected Outcome: The tilemap used for the level should all for player interaction with ground to walk on as walls to block your way.

    Test Case 5: Collision - Player

        Test Description: Test how the player interacts with walls.
        Test Steps:
            1. Start the game.
            4. Run into a wall.
            5. Verify that the player stops moving forward (repeat for each direction).
            6. Verify the player can't collide with objects such as their own bullets.
        Expected Outcome: Player could only interact with specific objects and do so in specific ways.
