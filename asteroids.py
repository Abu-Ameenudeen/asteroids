import pygame

from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.pos_x, self.pos_y), self.radius, 2)
        
    def update(self, dt):
        self.velocity += self.velocity * dt
        