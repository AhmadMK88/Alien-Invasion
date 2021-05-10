import sys
import pygame
from Ship import Ship_ob
from Settings import settings
import Game_functions as GF
from pygame.sprite import Group 
from Game_Stats import GameStats
from Button import Button_ob
from ScoreBoard import ScoreBoard_ob 

def run_game():
    pygame.init()
    game_settings = settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship_ob(game_settings,screen) 
    bullets = Group()
    aliens = Group()
    GF.create_fleet(game_settings , screen , aliens , ship )
    stats = GameStats(game_settings)
    play_button = Button_ob(game_settings, screen, "Play")
    sb = ScoreBoard_ob (game_settings, screen, stats)
    while True:
        GF.check_events(game_settings,screen,aliens,ship,bullets,stats,play_button,sb)
        if stats.game_active:
            ship.update()
            GF.update_bullets(game_settings,screen,ship,bullets,aliens,stats,sb)
            GF.update_aliens(game_settings,ship,aliens,screen,stats,bullets,sb)
        GF.Game_update(game_settings, screen, ship, aliens , bullets , stats , play_button , sb)
        


run_game()