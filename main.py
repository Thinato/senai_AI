import pygame as pg
import creature
from enviroment import Food
from constants import *

screen = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pg.time.Clock()

creatures = [creature.Sprinter() for _ in range(GENERATION_SIZE)]
foods = [Food() for _ in range(FOOD_COUNT)]
generation = 0
generation_time = 0
last_best = 0

def label(text:str, position) -> None:
    screen.blit(FONT.render(str(text), 1, (0,0,0)), position)

while True:
    dt = min(clock.tick(60) / 1000, 0.05) # cap so a stalled frame doesn't teleport anyone
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    for c in creatures:
        c.update(foods, dt)
    generation_time += dt
    if generation_time > GENERATION_TIME or not any(c.alive for c in creatures):
        last_best = max(c.fitness for c in creatures)
        creatures = creature.next_generation(creatures)
        generation += 1
        generation_time = 0

    screen.fill((255,255,255))
    for f in foods:
        f.draw(screen)
    for c in creatures:
        c.draw(screen)

    label(round(clock.get_fps(),3), (10,10))
    label(f"generation: {generation}  alive: {sum(c.alive for c in creatures)}  last best: {last_best}", (10,28))
    pg.display.flip()
