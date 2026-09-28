import pygame as pg
import numpy as np
import os
from constants import *
import random
from neural_network import Nnet

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
        self.speed = 60
        self.size = 1

        self.imgs = list()
        self.img = None # current image
        self.position = pg.math.Vector2(np.random.random()*700+50, np.random.random()*500+50)

        self.animation_tick = 300
        self.animation_last = 0
        self.animation_frame = 0

        self.brain = Nnet(NNET_INPUTS, NNET_HIDDEN, NNET_OUTPUTS)

    @property
    def alive(self):
        return self.energy_curr > 0

    def update(self, foods, dt):
        if not self.alive:
            return
        self.energy_curr -= self.fatigue * dt

        # brain sees the vector to the nearest food in vision range, answers with a direction
        food = min(foods, key=lambda f: self.position.distance_squared_to(f.position))
        to_food = food.position - self.position
        if to_food.length() > self.vision:
            return
        if to_food.length() < EAT_RADIUS:
            self.eat(food.energy)
            self.fitness += 1
            food.respawn()
        self.move(pg.math.Vector2(*self.brain.get_outputs(to_food / self.vision).flatten()), dt)

    def draw(self, screen):
        if not self.alive:
            return
        if pg.time.get_ticks() > self.animation_last + self.animation_tick:
            self.animation_frame += 1
            self.animation_last = pg.time.get_ticks() + np.random.random()*50
            self.img = self.imgs[self.animation_frame % len(self.imgs)]
        screen.blit(self.img, self.position - pg.math.Vector2(self.img.get_size())/2)

    def move(self, direction, dt):
        if direction.magnitude() > 0:
            self.position += direction.normalize() * self.speed * dt
            self.position.x = min(max(self.position.x, 0), DISPLAY_WIDTH)
            self.position.y = min(max(self.position.y, 0), DISPLAY_HEIGHT)
    

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


def next_generation(old):
    old = sorted(old, key=lambda c: c.fitness, reverse=True)
    cut = int(len(old) * MUTATION_CUT_OFF)
    parents = old[:cut] + [c for c in old[cut:] if np.random.random() < MUTATION_BAD_TO_KEEP]

    new = []
    for p in parents: # survivors keep their brain, get a fresh body
        c = Sprinter()
        c.brain = p.brain
        new.append(c)
    while len(new) < GENERATION_SIZE:
        a, b = random.sample(parents, 2)
        c = Sprinter()
        c.brain.create_mixed_weights(a.brain, b.brain)
        c.brain.modify_weights()
        new.append(c)
    return new
