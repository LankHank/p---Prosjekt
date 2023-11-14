import pygame

class Ball():
    def __init__(self, vindu_bredde: int, vindu_hoyde: int, ) -> None:
        self.radius = 20
        self.x = vindu_bredde / 2
        self.bottom = vindu_hoyde * 0.5
        self.farge = "white"
        self.fart_y = 6
        self.fart_x = 0
        self.ramme = pygame.Rect(self.x,self.bottom,self.radius, self.radius)
        

    def tegn(self, vindu: pygame.Surface):
        pygame.draw.circle(vindu, self.farge, [self.x, self.bottom], self.radius)

    def flytt(self):
        self.bottom += self.fart_y
        self.ramme.bottom += self.fart_y
        self.x += self.fart_x
        self.ramme.x += self.fart_x
        if (self.bottom-20) <= 0:
            self.fart_y = self.fart_y * -1 
        if (self.ramme.centerx+20) <= 0 or (self.ramme.centerx-20) >= 600:
            self.fart_x = self.fart_x * -1

    def kollisjon(self):
        pass
    
        
