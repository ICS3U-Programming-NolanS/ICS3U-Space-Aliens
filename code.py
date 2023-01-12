#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: Jan 2023
# This program is for space alien in the PyBadge

import stage
import ugame


def game_scene():
    # This function is the main game game_scene

    # Image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # Set the background image to 0 in the image bank
    # and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # Create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # Set the layers of all sprites, items show up in order
    game.layers = [background]
    # Render all sprites
    # most likely you will only render the background once per game_scene
    game.render_block()

    # this is the main game game_scene

    # image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image 0 in the image bank
    # and the size
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # create a stage for the background to show up on
    # set the frame rate to 60 fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all the sprites, items show up in order
    game.layers = [ship] + [background]

    # # render all sprites
    game.render_block()

    # repeat forever game loop
    while True:
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
