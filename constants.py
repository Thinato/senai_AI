import pygame as pg
pg.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

FONT_SIZE = 18
FONT = pg.font.SysFont('Cascadia Code', FONT_SIZE)

GENERATION_SIZE = 60

NNET_INPUTS = 2
NNET_HIDDEN = 5
NNET_OUTPUTS = 1

JUMP_CHANCE = 0.5

# MAX_Y_DIFF = DISPLAY_H - PIPE_MIN - PIPE_GAP_SIZE/2
# MIN_Y_DIFF = PIPE_GAP_SIZE/2 - PIPE_MAX
# Y_SHIFT = abs(MIN_Y_DIFF)
# NORMALIZER = abs(MIN_Y_DIFF) + MAX_Y_DIFF

MUTATION_WEIGHT_MODIFY_CHANCE = 0.2
MUTATION_ARRAY_MIX_PERC = 0.5
MUTATION_CUT_OFF = 0.4
MUTATION_BAD_TO_KEEP = 0.2
MUTATION_MODIFY_CHANCE_LIMIT = 0.4

SPRINTER = 1
HEAVY = 2