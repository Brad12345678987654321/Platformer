import pygame
class spritesheet:
    def __init__ (self, image, rows):
        print(image.get_width())
        print(image.get_height())
        self.image = image
        self.rows = rows
        self.tile_width = 64
    def get_frame(self, frame):
        return pygame.Surface.subsurface(self.image, (frame*self.tile_width,0, self.tile_width, self.tile_width))
        

