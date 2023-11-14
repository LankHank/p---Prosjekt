import pygame

class Ball():
    def __init__(self, vindu_bredde: int, vindu_hoyde: int) -> None:
        self.radius = 20
        self.x = vindu_bredde / 2
        self.bottom = vindu_hoyde * 0.9
        self.farge = "white"
        self.fart = 4
        self.ramme = pygame.Rect(0,0,self.radius, self.radius)
        

    def tegn(self, vindu: pygame.Surface):
        pygame.draw.circle(vindu, self.farge, [self.x, self.bottom], self.radius)

    def flytt(self):
        self.bottom += self.fart
        if (self.bottom-20) <= 0:
            self.fart = self.fart * -1

    def kollisjon(self):
        pass
        
