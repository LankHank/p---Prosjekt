import pygame

class Spiller():
    def __init__(self, vindu_bredde: int, vindu_hoyde: int) -> None:
        self.bilde = pygame.image.load("Bilder/cigarette.png").convert_alpha()
        self.bilde = pygame.transform.scale_by(self.bilde, 0.6)
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = vindu_bredde / 2
        self.ramme.top = vindu_hoyde * 0.9
        self.fart = 4

    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.ramme)

    def flytt(self, dx: int):
        self.ramme.x += dx

    
