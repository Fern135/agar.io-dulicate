import random

def rnd(min, max):
    return random.randint(min, max)

COLOR = {
    "white":        (255, 255, 255),
    "black":        (0, 0, 0),
    "blue":         (0, 0, 255),
    "green":        (0, 255, 0),
    "red":          (255, 0, 0),
    "rand":         (rnd(0,255), rnd(0, 255), rnd(0, 255)), 
    "yellow":       (255, 255, 0),
    "cyan":         (0, 255, 255),
    "silver":       (192, 192, 192)
}