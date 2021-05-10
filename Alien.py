import pygame
from pygame.sprite import Sprite

class Alien_ob(Sprite):
    
    def __init__(self, gsettings, screen) :
        super(Alien_ob, self).__init__()
        self.screen = screen
        self.gsettings = gsettings
        self.image = pygame.image.load(r'C:\Users\ASUS\Pictures\pngarea-com_alien-png-aliens-4.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
       screen_rect = self.screen.get_rect()
       if self.rect.right >= screen_rect.right:
           return True
       elif self.rect.left <= 0:
           return True
    
    def update(self) :
        self.x += (self.gsettings.alien_speed*self.gsettings.direction)
        self.rect.x = self.x
  
