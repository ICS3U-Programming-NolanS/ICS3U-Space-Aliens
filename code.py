#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: January 9th 2023
# This CPT program is the same program
# as the "Space Aliens" program on the pyBadge!

import ugame
import stage


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

    # repeat forever, game loop
    while True:
        pass  # for now it's just a placeholder


if __name__ == "__main__":
    game_scene()
