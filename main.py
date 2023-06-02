import pygame as pg
import creature
from constants import *

screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pg.time.Clock()

creatures = [creature.Sprinter() for _ in range(20)]

def label(text:str, position) -> None:
    screen.blit(FONT.render(str(text), 1, (0,0,0)), position)

while True:
    dt = clock.tick() / 1000
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    screen.fill((255,255,255))
    for creature in creatures:
        creature.update(screen, dt)

    label(round(clock.get_fps(),3), (10,10))
    label("newest gen: xxx", (10,28))
    pg.display.flip()