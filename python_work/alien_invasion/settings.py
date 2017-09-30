class Settings():
    def __init__(self):
        # screen
        self.screen_width = 800
        self.screen_height = 680
        self.bg_color = (230, 230, 230)
        # ships
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # bullets
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # alien
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 20
        self.fleet_direction = 1
        
        
