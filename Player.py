import Planets as Pl
import Globales as Gl


class Player:
    def __init__(self, mass, color, radius, name):
        self.mass = mass
        self.color = color
        self.radius = radius
        self.name = name

    def create_planet(self, pos_down, pos_up):
        distance_x = pos_down[0] - pos_up[0]
        distance_y = pos_down[1] - pos_up[1]
        x_vel = distance_x * Gl.AU * Gl.SCALE
        y_vel = distance_y * Gl.AU * Gl.SCALE
        x, y = (pos_down[0] - Gl.WIDTH / 2) / Gl.SCALE, (pos_down[1] - Gl.HEIGHT / 2) / Gl.SCALE
        planet = Pl.Planet(x, y, self.radius, self.color, self.mass, self.name, y_vel, x_vel)
        return planet
