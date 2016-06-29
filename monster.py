class Monster:
    def __init__(self, hit_points, weapon, color, sound):
        self.hit_points = hit_points
        self.weapon = weapon
        self.color = color
        self.sound = sound

    def battlecry(self):
        return self.sound.upper()



