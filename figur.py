import pygame

class Figur():
    def __init__(self, bildesti: str, ) -> None:
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.bilde = pygame.transform.scale_by(self.bilde, 0.6)
        self.ramme = self.bilde.get_rect()