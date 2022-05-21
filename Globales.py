import pygame as pg

# Simulation settings
AU = 149.6e6 * 1000
G = 6.67428e-11
SCALE = 150 / AU
TIME_STEP = 60 * 60 * 24

# Window settings
WIDTH, HEIGHT = 1080, 720
FPS = 60

# Colors settings
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 191, 255)
RED = (188, 39, 50)
DARK_GREY = (80, 80, 80)
WHITE = (255, 255, 255)

# Text settings
pg.init()
FONT = pg.font.SysFont('comicsans', 16)