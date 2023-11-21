import pygame
import pygame.freetype
from figur import Figur

class Spiller(Figur):
    def __init__(self, vindu_bredde: int, vindu_hoyde: int) -> None:
        super().__init__("Bilder/cigarette.png")
        self.ramme.centerx = vindu_bredde / 2
        self.ramme.top = vindu_hoyde * 0.9
        self.fart = 4
        self.poeng = 0
        self.font = pygame.freetype.SysFont("Consolas", 40)

    def tegn_spiller(self, vindu: pygame.Surface):
        vindu.blit(self.bilde, self.ramme)

    def tegn_poeng(self, vindu: pygame.Surface):
        self.font.render_to(vindu, (100,200), f"{self.poeng}","white")

    def flytt(self, dx: int):
        self.ramme.x += dx
        if self.ramme.left <= 0:
                self.ramme.x += self.fart
        if self.ramme.right >= 600:
                self.ramme.x -= self.fart

    

