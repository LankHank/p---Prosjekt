import pygame
from spiller import Spiller
from ball import Ball

class Vindu():
    def __init__(self) -> None:
        pygame.init()
        self.bredde = 600
        self.hoyde = 600
        self.vindu = pygame.display.set_mode((self.bredde, self.hoyde))
        self.klokke = pygame.time.Clock()
        self.fps = 60

        self.spiller = Spiller(self.bredde, self.hoyde)
        self.ball = Ball(self.bredde, self.hoyde)

    def vis_spill(self):
        self.tilstand = "spill"

    def viss_meny(self):
        self.tilstand = "meny"
    
    def avslutt(self):
        pygame.quit()
        raise SystemExit
    
    def kjør(self):
        while True:
            # Håndtere input
            hendelser = pygame.event.get()
            for hendelse in hendelser:
                if hendelse.type == pygame.QUIT:
                    self.avslutt()

            if self.spiller.ramme.left <= 0:
                self.spiller.ramme.x += self.spiller.fart
            if self.spiller.ramme.right >= 600:
                self.spiller.ramme.x -= self.spiller.fart
            
            taster = pygame.key.get_pressed()
            if taster[pygame.K_ESCAPE]:
                self.avslutt()
            if taster[pygame.K_LEFT]:
                self.spiller.flytt(-self.spiller.fart)
            if taster[pygame.K_RIGHT]:
                self.spiller.flytt(self.spiller.fart)

            self.ball.flytt()

            self.vindu.fill("black")
            self.spiller.tegn(self.vindu)
            self.ball.tegn(self.vindu)
            
            pygame.display.flip()
            self.klokke.tick(self.fps)

spill_vindu = Vindu()
spill_vindu.kjør()