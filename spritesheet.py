import pygame
class spritesheet:
    def __init__ (self, image, rows, start):
        print(image.get_width())
        print(image.get_height())
        self.image = image
        self.start = start
        self.rows = rows
        self.tile_width = 64
    def get_frame(self, frame):
        return pygame.Surface.subsurface(self.image, (frame+self.start)*self.tile_width,0, self.tile_width, self.tile_width)
        

