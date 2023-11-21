import pygame
import math

class Ball():
    def __init__(self, vindu_bredde: int, vindu_hoyde: int, ) -> None:
        self.radius = 20
        self.x = vindu_bredde / 2
        self.bottom = vindu_hoyde * 0.5
        self.farge = "white"
        self.abs_fart = 9
        self.fart_y = 9
        self.fart_x = 0
        self.aks = 0.3
        self.ramme = pygame.Rect(self.x - self.radius,self.bottom - (2*self.radius),self.radius * 2, self.radius * 2)
        self.turned = False
        

    def tegn(self, vindu: pygame.Surface):
        pygame.draw.circle(vindu, self.farge, [self.ramme.centerx, self.ramme.centery], self.radius)

    def fart(self, x, y, brett_x, brett_y):
        vinkel = math.atan2(y-brett_y, x-brett_x)
        velx = math.cos(vinkel)*self.abs_fart
        vely = math.sin(vinkel)*self.abs_fart
        self.abs_fart += self.aks
        return velx, vely

    def flytt(self):
        self.bottom += self.fart_y
        self.ramme.bottom += self.fart_y
        self.x += self.fart_x
        self.ramme.x += self.fart_x
        if (self.ramme.top) <= 0:
            self.fart_y = self.fart_y * -1 
        if (self.ramme.left) <= 0 or (self.ramme.right) >= 600:
            self.fart_x = self.fart_x * -1
        
