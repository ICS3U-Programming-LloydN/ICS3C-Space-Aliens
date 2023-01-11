#!/usr/bin/env python3
# Created by: Lloyd Najac
# Created on: Jan 2023

import stage
import ugame
 
 
def game_scene():
   
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
   
   #set the background to image 0 in the image bank
   #and the size (10x8 tiles of size 16x16)
    backgound = stage.Grid (image_bank_background, 10, 8)
   #create a stage for the background to show up on
   #and set frame to 60fps
    game = stage.Stage(ugame.display,60)
   #set the layers of all sprites, items in order
    game.layers = [backgound]
   #render all sprites
   # most likely you will render thee background once per game
    game.render_block()
    # repeat forever game loop
    while True:
        pass  # A placeholder for now
if __name__ == "__main__":
    game_scene()
