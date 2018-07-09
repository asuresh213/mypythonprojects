import pygame
import math
import random

pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Fractal Tree")

screen = pygame.display.get_surface()
screen.fill((255, 255, 255))


def draw_tree(x1, y1, angle, length, level, thickness, r, g, b):
    if level > 0:
        if(thickness == 0):
            thickness = 2
        x2 = x1 + (math.cos(angle)*length*7)
        y2 = y1 + (math.sin(angle)*length*7)
        #hr, hg, hb = rgb_to_hsv(r, g, b)
        pygame.draw.line(screen, (r, g, b), (x1, y1), (x2, y2), thickness)
        draw_tree(x2, y2, angle - 0.30, length - 1, level - 1, thickness-1, r+21, g+21, b+21)
        draw_tree(x2, y2, angle + 0.30, length - 1, level - 1, thickness-1, r+21, g+21, b+21)


def input(event):
    if event.type == pygame.QUIT:
        exit(0)


draw_tree(400, 750, (-math.pi/2), 12, 12, 10, 0, 0, 0)
pygame.display.flip()
while True:
    input(pygame.event.wait())
