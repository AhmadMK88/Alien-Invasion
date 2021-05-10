class settings () :
    def __init__(self) :
        self.ship_speed_factor = 1.5 
        self.screen_width = 1200 ;
        self.screen_height = 500 
        self.bg_color = (0,0,0)
        self.bullet_speed_factor = 3
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_color  = 255 , 69 , 0 
        self.allowed_bullets = 100 
        self.alien_speed = 1 
        self.fleet_down_speed = 1 
        self.direction = 1 
        self.ship_lives = 3 
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
 
    def initialize_dynamic_settings(self) :
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed = 1
        self.direction = 1
        self.alien_points = 50 
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale