# importing pygame module
import pygame
from renderer import *
import soft_body_parts

# importing sys module
import sys

vertex = soft_body_parts.vertex(100, 100)

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((500, 500))

# creating a running loop
while True:
    # creating a loop to check events that
    # are occuring
    renderer.render(display, vertex)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
            # if keydown event happened
            # than printing a string to output
            print("A key has been pressed")
    pygame.display.update()
