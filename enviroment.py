import pygame as pg
import numpy as np
from constants import *

class Food():
    def __init__(self):
        self.energy = FOOD_ENERGY
        self.respawn()

    def respawn(self):
        self.position = pg.math.Vector2(np.random.random()*(DISPLAY_WIDTH-40)+20, np.random.random()*(DISPLAY_HEIGHT-40)+20)

    def draw(self, screen):
        pg.draw.circle(screen, (60,180,75), self.position, 4)
