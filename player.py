
from Gameobject import Gameobject
import pygame
class Player(Gameobject):
    def __init__(self, pos, width, height, animations, game, spritesheet):
        super().__init__(pos, width, height, animations, game,)
        self.spritesheet = spritesheet
        self.speed = 3
        self.direction = 5
        self.xvelocity = 0
        self.yvelocity = 0
        self.action = "idle"
        self.curr_time = 0
        self.frame = 0
    def handle_input(self, keys):
        if keys[pygame.K_a]:
            self.xvelocity = -self.speed
            self.direction = -1
            self.action = "walk"
        elif keys[pygame.K_d]:
            self.xvelocity = self.speed
            self.direction = 1
            self.action = "walk"
        elif keys[pygame.K_w]:
            self.yvelocity = -self.speed
            self.action = "walk"
        elif keys[pygame.K_s]:
            self.yvelocity = self.speed
            self.action = "walk"
        elif keys[pygame.K_p]:
            self.action = "death"
        elif keys[pygame.K_SPACE]:
            self.action = "jump"
            self.pos[1] -= 1

        else:
            self.xvelocity = 0
            self.yvelocity = 0
            self.action = "idle"

    def render(self, elapsed_time):
        if elapsed_time - self.curr_time > 100:
            self.frame += 1
            self.curr_time = elapsed_time
        if self.frame > self.animations[self.action].rows:
            self.frame = 0
            
        #self.game.screen.blit(self.animations[self.action][frame], self.pos)\
        img = self.animations[self.action].get_frame(self.frame)
        
        if self.direction > 0:
            img = pygame.transform.flip(img, True, False)
        
        self.game.screen.blit(img, self.pos)


    def update(self):
        self.pos[0] += self.xvelocity
        self.pos[1] += self.yvelocity