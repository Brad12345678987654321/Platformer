
from Gameobject import Gameobject
import pygame
class Player(Gameobject):
    def __init__(self, pos, width, height, animations, game, spritesheet):
        super().__init__(pos, width, height, animations, game,)
        self.spritesheet = spritesheet
        self.speed = 10
        self.direction = 5
        self.xvelocity = 0
        self.yvelocity = 0
    def handle_input(self, keys):
        if keys[pygame.K_a]:
            self.xvelocity = -self.speed
            self.direction = -1
        elif keys[pygame.K_d]:
            self.xvelocity = self.speed
            self.direction = 1
        elif keys[pygame.K_w]:
            self.yvelocity = -self.speed
        elif keys[pygame.K_s]:
            self.yvelocity = self.speed
        else:
            self.xvelocity = 0
            self.yvelocity = 0

    def render(self):
        #self.game.screen.blit(self.animations[self.action][frame], self.pos)\
        img = pygame.Surface.subsurface(self.animations, (0,0, self.animations.get_width()//25, self.animations.get_height()))
        img = self.spritesheet.get_frame(10)
        
        if self.direction > 0:
            img = pygame.transform.flip(img, True, False)
        
        self.game.screen.blit(img, self.pos)


    def update(self):
        self.pos[0] += self.xvelocity
        self.pos[1] += self.yvelocity