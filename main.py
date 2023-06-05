########################
# IMPORTS
########################

import pygame
from assets import (
    dir_path,
    window,
    running,
    fps,
    clock,
    utils,
#    favicon
)

########################
# SCENES
########################

scene = None

class game:
    def handle():
        window.fill((50,50,50))

########################
# GAME LOOP
########################

scene = game

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    clock.tick(fps)
    scene.handle()
    pygame.display.update()

pygame.quit