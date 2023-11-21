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

            if self.ball.ramme.colliderect(self.spiller.ramme):
                self.ball.fart_x, self.ball.fart_y = self.ball.fart(self.ball.ramme.centerx,self.ball.ramme.centery,self.spiller.ramme.centerx,self.spiller.ramme.centery)
                self.spiller.poeng += 1

            if self.ball.ramme.bottom >= self.hoyde:
                self.reset_game()

            
            taster = pygame.key.get_pressed()
            if taster[pygame.K_r]:
                self.reset_game()
            if taster[pygame.K_ESCAPE]:
                self.avslutt()
            if taster[pygame.K_LEFT]:
                self.spiller.flytt(-self.spiller.fart)
            if taster[pygame.K_RIGHT]:
                self.spiller.flytt(self.spiller.fart)

            self.ball.flytt()

            self.vindu.fill("black")
            self.spiller.tegn_poeng(self.vindu)
            self.spiller.tegn_spiller(self.vindu)
            self.ball.tegn(self.vindu)
            pygame.display.flip()
            self.klokke.tick(self.fps)

    def reset_game(self):
        self.spiller = Spiller(self.bredde, self.hoyde)
        self.ball = Ball(self.bredde, self.hoyde)

spill_vindu = Vindu()
spill_vindu.kjør()