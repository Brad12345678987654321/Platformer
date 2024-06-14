import pygame 
from spritesheet import spritesheet
from Gameobject import Gameobject
from player import Player
class Game:
    def __init__(self):     
        pygame.init()
        self.width = 900
        self.height= 600
        player_image = pygame.image.load("ZombieToast.png")
        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((900, 600))
        self.walking = spritesheet(player_image, 25)
        self.toast = Player((0,0), 15, 15, player_image, self, self.walking)


    def run(self):
        while True:
            self.screen.fill((0,0,0))
            self.clock.tick(60)
            self.toast.handle_input(pygame.key.get_pressed())
            self.toast.update()
            self.toast.render()
            pygame.display.update()
            for events in pygame.event.get():
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_ESCAPE:
                        pygame.quit()
                       
game = Game()
game.run()
