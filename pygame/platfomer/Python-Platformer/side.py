import pygame
import random
import time
import math
from os import listdir
from os.path import isfile, join

#Global Vairaibles
width, height = 1000, 800
bg_color = (255, 255, 255)
fps = 60


pygame.init()
pygame.display.set_caption("Platformer")
window = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
    COLOR = (255,0,0)
    PLAYER_VELOCITY = 5

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = None

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, velocity):
        self.x_velocity = -velocity
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, velocity):
        self.y_velocity = velocity
        if self.direction != "rigth":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_velocity, self.y_velocity)

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)


def get_background(name):
    image = pygame.image.load(join('assets', 'Background', name))
    _, _, tile_width, tile_height = image.get_rect()
    tiles = []
    for i in range (width // tile_width +1):
        for j in range (height // tile_height + 1):
            pos  = (i* tile_width, j* tile_height)
            tiles.append(pos)
    return tiles, image

def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)
        player.draw(window)
    pygame.display.update()

def handle_move():
    key = pygame.key.get_pressed()
    
    

def main(window):
    run = True
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")
    player1 = Player(100, 100, 50, 50)
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window, background, bg_image, player1)

    pygame.QUIT()
    quit()

if __name__ == "__main__":
    main(window)