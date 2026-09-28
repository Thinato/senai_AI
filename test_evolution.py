# Headless check: evolution should beat random brains. Run: python test_evolution.py
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'
import random
import numpy as np
import pygame as pg
from constants import *
import creature
from enviroment import Food

np.random.seed(0)
random.seed(0)
pg.display.set_mode((1, 1))

dt = 1 / 30
creatures = [creature.Sprinter() for _ in range(GENERATION_SIZE)]
foods = [Food() for _ in range(FOOD_COUNT)]
means = []
for gen in range(12):
    t = 0
    while t < GENERATION_TIME and any(c.alive for c in creatures):
        for c in creatures:
            c.update(foods, dt)
        t += dt
    means.append(np.mean([c.fitness for c in creatures]))
    print(f"gen {gen}: mean food {means[-1]:.2f}, best {max(c.fitness for c in creatures)}")
    creatures = creature.next_generation(creatures)

assert np.mean(means[-3:]) > 1.5 * means[0], means
print("ok")
