# Basic random ball bouncing simulation on PyGame 
# Just learning basics before using it for a bigger project

import random
import pygame
from draughts.consts import BLACK, BLUE, HEIGHT, WIDTH  # Personall library of constants

FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draughts AI")


def main():
    run = True
    clock = pygame.time.Clock()

    xpos = 300
    ypos = 400
    xChange = 3
    yChange = 3

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Game logic
        xpos += xChange
        ypos += yChange

        if xpos > 770 or xpos < 0:
            xChange = xChange * -(random.random() + 0.5)

        if ypos > 770 or ypos < 0:
            yChange = yChange * -(random.random() + 0.5)

        window.fill(BLACK)
        pygame.draw.ellipse(window, BLUE, [xpos, ypos, 30, 30])
        # This is where you draw the board

        pygame.display.flip()

    pygame.quit()


main()
