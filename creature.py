import pygame as pg
import numpy as np
import os
from constants import *
import math

class Creature():
    def __init__(self):
        self.energy_max = 100
        self.energy_curr = self.energy_max
        self.fatigue = 10

        self.health_max = 100
        self.health_curr = self.health_max
        self.armor = 10        
        self.type = None
        
        self.strength = 10
        
        self.vision = 300 # radius in px

        self.asexual = False

        self.fitness = 0
        self.speed = 20
        self.size = 1

        self.imgs = list()
        self.img = None # current image
        self.position = pg.math.Vector2(np.random.random()*700+50, np.random.random()*500+50)

        self.animation_tick = 300
        self.animation_last = 0
        self.animation_frame = 0

    def update(self, screen, dt):
        if pg.time.get_ticks() > self.animation_last + self.animation_tick:
            self.animation_frame += 1
            self.animation_last = pg.time.get_ticks() + np.random.random()*50
            self.img = self.imgs[self.animation_frame % len(self.imgs)]

        screen.blit(self.img, self.position)
        self.move(pg.math.Vector2(np.random.random()*2-1, np.random.random()*2-1), dt)

    def move(self, direction, dt):
        if direction.magnitude() > 0:
            self.position += direction * self.speed * dt
    

    def eat(self, amount):
        self.energy_curr += amount
        
        if self.energy_curr > self.energy_max:
            self.energy_curr = self.energy_max
        

class Sprinter(Creature):
    def __init__(self):
        super().__init__()
        self.fatigue *= 1.5
        self.vision *= 1.1
        self.speed *= 2

        self.type = SPRINTER
        self.imgs = [
            pg.image.load(os.path.join('assets', 'creatures', f'sprinter_{i}.png')).convert_alpha() for i in range(6)
        ]
        self.img = pg.image.load(os.path.join('assets', 'creatures', 'sprinter_0.png')).convert_alpha()


    
        

        