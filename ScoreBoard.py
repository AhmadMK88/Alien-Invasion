import pygame.font 
from pygame.sprite import Group
from Ship import Ship_ob 

class ScoreBoard_ob():
    def __init__(self , gsettings , screen , stats ) :
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.gsettings = gsettings
        self.stats = stats

        self.init_ships()

        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        self.init_score()
    

    def init_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.gsettings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.ships.draw(self.screen)

    def init_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship_ob (self.gsettings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)





