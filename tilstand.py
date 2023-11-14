import pygame

class Tilstand():
    def __init__(self, vindu_hoyde: int, vindu_bredde: int) -> None:
        self.overflate = pygame.Surface((vindu_bredde, vindu_hoyde))
        self.ramme = self.overflate.get_rect()
        self.ramme.x = 0
        self.ramme.y = 0