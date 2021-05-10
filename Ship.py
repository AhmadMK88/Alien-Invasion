import pygame
from Settings import settings 
from pygame.sprite import Sprite

class Ship_ob (Sprite):
    
    def __init__ ( self , gsettings , screen ) :
        super(Ship_ob, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r'C:\Users\ASUS\Pictures\Spaceship-PNG-File_70x80.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moving_right = False 
        self.moving_left = False
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom
    
    def update ( self ) :
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.rect.centerx += 1 
        elif self.moving_left and self.rect.left > 0 :
            self.rect.centerx -= 1 
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx