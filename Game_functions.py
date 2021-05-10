import pygame 
import sys 
from Ship import Ship_ob
from Settings import settings 
from Bullets import Bullet 
from Alien import Alien_ob
from time import sleep


def fire_bullets ( gsettings , screen , ship , bullets ) :
    if len(bullets) < gsettings.allowed_bullets :
            new_bullet = Bullet(gsettings,screen,ship) 
            bullets.add(new_bullet)

def check_keydown_events(event , gsettings , screen , ship , bullets ) :
    if event.key == pygame.K_RIGHT :
        ship.moving_right = True
    elif event.key == pygame.K_LEFT :
        ship.moving_left = True
    elif event.key == pygame.K_SPACE :
        fire_bullets(gsettings,screen,ship,bullets)
        


def check_keyup_events(event,ship) :
    if event.key == pygame.K_RIGHT :
        ship.moving_right = False 
    elif event.key == pygame.K_LEFT :
        ship.moving_left = False 


def check_events(gsettings,screen,aliens,ship,bullets,stats,play_button,sb) :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        elif event.type == pygame.KEYDOWN  :
            check_keydown_events(event,gsettings,screen,ship,bullets) 
        elif event.type == pygame.KEYUP :
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouseX, mouseY , gsettings , screen , ship , aliens , bullets , sb )

def check_play_button(stats, play_button, mouseX, mouseY , gsettings , screen , ship , aliens , bullets , sb ):
    clicked = play_button.rect.collidepoint(mouseX, mouseY)
    if clicked and not stats.game_active:
        sb.init_ships()
        gsettings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(gsettings,screen,aliens,ship);
        ship.center_ship()

def Game_update ( gsettings , screen , ship , aliens , bullets , stats , play_button , sb ) :
    screen.fill(gsettings.bg_color)
    for bullet in bullets.sprites() :
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

 

def update_bullets ( gsettings, screen, ship , bullets , aliens , stats , sb ) :
    bullets.update() 
    for bullet in bullets.copy() :
            if bullet.rect.bottom <= 0 :
                bullets.remove(bullet)
    check_collisions(gsettings, screen, ship, aliens, bullets,stats,sb)

def check_collisions(gsettings, screen, ship, aliens, bullets , stats , sb ) :
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        stats.score += gsettings.alien_points
        sb.init_score()
    if len(aliens) == 0:
        bullets.empty()
        gsettings.increase_speed()
        create_fleet(gsettings, screen , aliens , ship )

def update_aliens(aliens) :
    aliens.update()


def get_num_of_aliens ( gsettings , alien_width ) :
    available_space = gsettings.screen_width - 2 * alien_width
    num = int(available_space / (2 * alien_width))
    return num 



def get_num_of_rows ( gsettings , height , alien_height ) :
    available_space = ( gsettings.screen_height -(3 * alien_height) - height )
    rows_num = int(available_space / (2 * alien_height))
    return rows_num



def make_alien( gsettings, screen, aliens, nums , row_num ):
    
    alien = Alien_ob( gsettings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * nums
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
    aliens.add(alien)



def create_fleet ( gsettings , screen  , aliens , ship ) :
    
    alien = Alien_ob(gsettings,screen)
    aliens_number = get_num_of_aliens( gsettings, alien.rect.width )
    rows_number = get_num_of_rows( gsettings , ship.rect.height , alien.rect.height )
    for row_num in range(rows_number) :
        for alien_num in range(aliens_number):
            make_alien( gsettings, screen, aliens, alien_num,row_num)




def change_fleet_direction(gsettings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += gsettings.fleet_down_speed 
    gsettings.direction *= -1

def check_fleet_edges(gsettings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(gsettings, aliens)
            break

def check_aliens_bottom(gsettings, stats, screen, ship, aliens, bullets,sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(gsettings, stats, screen, ship, aliens, bullets,sb)
            break

def update_aliens(gsettings,ship,aliens,screen,stats,bullets,sb):
    check_fleet_edges(gsettings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(gsettings, stats, screen, ship, aliens, bullets,sb)
    check_aliens_bottom(gsettings, stats, screen, ship, aliens, bullets,sb)

def ship_hit(gsettings, stats, screen, ship, aliens, bullets,sb):
    if stats.ships_left> 0:
        stats.ships_left -= 1
        sb.init_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(gsettings, screen, aliens , ship )
        ship.center_ship()
        sleep(0.5)
    else :
        stats.game_active = False
        pygame.mouse.set_visible(False)