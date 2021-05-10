class GameStats() :
    
    def __init__(self,gsettings) :
        self.gsettings = gsettings
        self.reset_stats()
        self.game_active = False
    
    def reset_stats(self):
        self.ships_left = self.gsettings.ship_lives
        self.score = 0 