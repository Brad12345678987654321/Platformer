import pygame
class Gameobject:
    def __init__(self, pos, width, height, animations, game, action="idle"):
        self.pos = list(pos)
        self.width = width
        self.height = height
        self.animations = animations
        self.game = game
        self.action = action
        self.xvelocity = 0
        self.yvelocity = 0


    def render(self):
        #self.game.screen.blit(self.animations[self.action][frame], self.pos)\
        img = pygame.Surface.subsurface(self.animations, (0,0, self.animations.get_width()//25, self.animations.get_height()))
        self.game.screen.blit(img, self.pos)


    def update(self):
        self.pos[0] += self.xvelocity
        self.pos[1] += self.yvelocity