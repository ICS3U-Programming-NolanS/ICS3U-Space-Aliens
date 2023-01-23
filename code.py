#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: Jan 2023
# This program is for space alien in the PyBadge

import stage
import ugame
import time
import random

import constants


def splash_scene():
    # This function is the main game game_scene

    # Get the sound ready
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # Image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Set the background image to 0 in the image bank
    # and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_mt_background, 10, 8)

    # used this program to split the image into tile:
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white

    # Create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Set the layers of all sprites, items show up in order
    game.layers = [background]
    # Render all sprites
    # most likely you will only render the background once per game_scene
    game.render_block()

    # this is the main game game_scene

    # repeat forever game loop
    while True:

        time.sleep(2.0)
        menu_scene()


def menu_scene():
    # This function is the main game game_scene

    # Image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.NEW_PALETTE)
    text1.move(20, 10)
    text1.text("MT Games Studio")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.NEW_PALETTE)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # Set the background image to 0 in the image bank
    # and size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # Create a stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
    # Set the layers of all sprites, items show up in order
    game.layers = text + [background]
    # Render all sprites
    # most likely you will only render the background once per game_scene
    game.render_block()

    # this is the main game game_scene

    # repeat forever game loop
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        # Redraw sprites
        game.tick()

        def game_scene():
            # This function is the main game game_scene

            # Image banks for CircuitPython
            image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
            image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

            # Buttons that you want to keep state information on
            a_button = constants.button_state["button_up"]
            b_button = constants.button_state["button_up"]
            start_button = constants.button_state["button_up"]
            select_button = constants.button_state["button_up"]

            # Get sound ready
            pew_sound = open("pew.wav", "rb")
            sound = ugame.audio
            sound.stop()
            sound.mute(False)

            # Set the background image to 0 in the image bank
            # and size (10x8 tiles of size 16x16)
            background = stage.Grid(image_bank_background, 10, 8)

            for x_location in range(constants.SCREEN_GRID_X):
                for y_location in range(constants.SCREEN_GRID_Y):
                    tile_picked = random.randint(1, 3)
                    background.tile(x_location, y_location, tile_picked)
            # a sprite that will be updated every frame
            ship = stage.Sprite(
                image_bank_sprites,
                5,
                75,
                constants.SCREEN_Y - (2 * constants.SPRITE_SIZE),
            )
            alien = stage.Sprite(
                image_bank_sprites,
                9,
                int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
                16,
            )
            # Create a stage for the background to show up on
            # and set the frame rate to 60fps
            game = stage.Stage(ugame.display, constants.FPS)
            # Set the layers of all sprites, items show up in order
            game.layers = [ship] + [alien] + [background]
            # Render all sprites
            # most likely you will only render the background once per game_scene
            game.render_block()

            # this is the main game game_scene

            # repeat forever game loop
            while True:
                # Get user input
                keys = ugame.buttons.get_pressed()

                # A button to fire
                if keys & ugame.K_X != 0:
                    if b_button == constants.button_state["button_up"]:
                        b_button = constants.button_state["button_just_pressed"]
                    elif b_button == constants.button_state["button_just_pressed"]:
                        b_button = constants.button_state["button_still_pressed"]
                else:
                    if b_button == constants.button_state["button_still_pressed"]:
                        b_button = constants.button_state["button_released"]
                    else:
                        b_button = constants.button_state["button_up"]
                # B button
                if keys & ugame.K_O:
                    pass
                if keys & ugame.K_START:
                    print("Start")
                if keys & ugame.K_SELECT:
                    print("Select")
                if keys & ugame.K_RIGHT:
                    if ship.x <= constants.SCREEN_X - 16:
                        ship.move(ship.x + 1, ship.y)
                    else:
                        ship.move(constants.SCREEN_X - 16, ship.y)
                if keys & ugame.K_LEFT:
                    if ship.x >= 0:
                        ship.move(ship.x - 1, ship.y)
                    else:
                        ship.move(0, ship.y)
                if keys & ugame.K_UP:
                    pass
                if keys & ugame.K_DOWN:
                    pass

                # Update game logic
                if b_button == constants.button_state["button_just_pressed"]:
                    sound.play(pew_sound)

                # Redraw sprites
                game.render_sprites([ship] + [alien])
                game.tick()


if __name__ == "__main__":
    menu_scene()
