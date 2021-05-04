import pygame
from pygame_functions import *
import random
pygame.init()
screen = pygame.display.set_mode((480, 480))
win_width, win_height = pygame.display.get_surface().get_size()
"""layer1 = pygame.surface.Surface((win_width, win_height))
layer2 = pygame.surface.Surface((win_width, win_height))
layer3 = pygame.surface.Surface((win_width, win_height))
layer4 = pygame.surface.Surface((win_width, win_height))
layer5 = pygame.surface.Surface((win_width, win_height))"""


def redraw_screen():
    pygame.display.update()


def main():

    time_day = 0
    running = True
    tick = pygame.time.Clock()

    game_map = [[], [], ] #first two are city
    entity_dict = {'car0': {}, 'car1': {}, } #first 2 are cars
    left_right = ['l', 'r']

    def collision_test(rect, tiles):
        collisions = []
        for tile in tiles:
            if pygame.rect.colliderect(tiles):
                collisions.append(tile)
        return collisions

    def car_layer(dict_name):
        for f in range(car_amount):
            screen.blit(pygame.image.load("sprites\\car.png"), (dict_name['car', f][0], dict_name['car', f][1]))
            if dict_name['car', f][2] == 'r':
                if dict_name['car', f][0] > 484:
                    dict_name['car', f][0] = 0
                    dict_name['car', f][1] = random.randint(250, 270)
                else:
                    dict_name['car', f][0] += .5

            if dict_name['car', f][2] == 'l':
                if dict_name['car', f][0] < 0:
                    dict_name['car', f][0] = 480
                    dict_name['car', f][1] = random.randint(250, 270)
                else:
                    dict_name['car', f][0] -= .5

    def blit_if(requirement, sprite, sprite_list, x, y):
        if requirement: # if True: appent sprite to perm data
            sprite_list.append(sprite)
        screen.blit(pygame.image.load(sprite_list[i - 1]), (x, y))

    while running:

        win_width, win_height = pygame.display.get_surface().get_size()

        tick.tick(50)
        time_day += 1
        tile_amount = 15
        car_amount = 20

        for i in range(tile_amount):

            blit_if(requirement=len(game_map[0]) < tile_amount,
                    sprite=f"sprites\\skyline{random.randint(1,2)}.png",
                    sprite_list=game_map[0],
                    x=(480-(32*(i+1))), y=240)

            blit_if(requirement=len(game_map[1]) < tile_amount,
                    sprite=f"sprites\\subcity{random.randint(1,5)}.png",
                    sprite_list=game_map[1],
                    x=480-(32*(i+1)), y=272)

            if car_amount > len(entity_dict['car0']):
                for g in range(car_amount):
                    entity_dict['car0']['car', g] = [random.randint(0, 480),
                                               random.randint(250, 280), random.choice(left_right)]
                    entity_dict['car1']['car', g] = [random.randint(0, 480),
                                          random.randint(250, 270), random.choice(left_right)]

        car_layer(entity_dict['car1'])

        for i in range(tile_amount):

            screen.blit(pygame.image.load(f"sprites\\front_skyline1.png"), (480-(32*(i+1)), 240))

        car_layer(entity_dict['car0'])
        redraw_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                pass


main()
