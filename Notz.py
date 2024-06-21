import pygame 
from spritesheet import spritesheet
from Gameobject import Gameobject
from player import Player
class Game:
    def __init__(self):     
        pygame.init()
        self.width = 900
        self.height= 600
        self.player_image = pygame.image.load("ZombieToast.png")
        self.background_image = pygame.transform.scale(pygame.image.load("Graveyard.png"), (900,600))

        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((900, 600))
        self.toast = Player((0,0), 15, 15, self.load_animations(), self, self.player_image )


    def run(self):
        while True:
            elapsed_time = pygame.time.get_ticks()
            self.screen.blit(self.background_image, (0,0))
            self.clock.tick(60)
            self.toast.handle_input(pygame.key.get_pressed())
            self.toast.update()
            self.toast.render(elapsed_time)
            pygame.display.update()
            for events in pygame.event.get():
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_ESCAPE:
                        pygame.quit()

    def load_animations(self):
        return {"idle": spritesheet(self.player_image,2,0),
                "walk": spritesheet(self.player_image, 4,2),
                "death": spritesheet(self.player_image, 9,15),
                "jump": spritesheet(self.player_image, 5,7)}
                       
game = Game()
game.run()
