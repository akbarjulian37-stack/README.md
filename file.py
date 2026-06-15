import time
import os
import math

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def petal(angle, scale):
    x = scale * math.cos(angle)
    y = scale * math.sin(angle) * 0.5
    return int(x), int(y)

def heart(t):
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
    return x/20, y/20

for frame in range(60):
    clear()
    progress = frame / 60
    
    canvas = [[' ' for _ in range(40)] for _ in range(20)]
    
    if progress < 0.5:  # Fase bunga mekar
        scale = progress / 0.5 * 8
        for i in range(8):
            angle = 2 * math.pi * i / 8 + frame * 0.1
            px, py = petal(angle, scale)
            x, y = 20 + px, 10 + py
            if 0 <= x