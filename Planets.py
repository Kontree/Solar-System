import Globales as Gl
import pygame as pg
import math as mt


class Planet:
    def __init__(self, x, y, radius, color, mass, name='', yVel=0, xVel=0):
        self.pos = self.x, self.y = x, y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.isSun = False
        self.xVel = xVel
        self.yVel = yVel
        self.distanceToStar = 0
        self.orbit = []
        self.name = name

    def draw(self, window):
        x = self.x * Gl.SCALE + Gl.WIDTH / 2
        y = self.y * Gl.SCALE + Gl.HEIGHT / 2
        if len(self.orbit) > 2:
            updatedPoints = []
            pointsLimit = 80 * self.distanceToStar * 10**-11 * mt.pi
            for point in self.orbit:
                x, y = point
                x = x * Gl.SCALE + Gl.WIDTH / 2
                y = y * Gl.SCALE + Gl.HEIGHT / 2
                updatedPoints.append((x, y))
                if len(updatedPoints) >= pointsLimit:
                    updatedPoints.pop(0)
            for i in range(len(updatedPoints) - 1):
                fadingColor = (self.color[0] * i / pointsLimit,
                               self.color[1] * i / pointsLimit,
                               self.color[2] * i / pointsLimit)
                pg.draw.aaline(window, fadingColor, updatedPoints[i], updatedPoints[i + 1])

        if not self.isSun:
            distanceText = Gl.FONT.render(f"{round(self.distanceToStar / 1000)} km", 1, Gl.WHITE)
            window.blit(distanceText, (x, y + 20))
        pg.draw.circle(window, self.color, (x, y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = mt.sqrt(distance_x**2 + distance_y**2)

        if other.isSun:
            self.distanceToStar = distance

        force = Gl.G * self.mass * other.mass / distance**2
        theta = mt.atan2(distance_y, distance_x)
        forceX = mt.cos(theta) * force
        forceY = mt.sin(theta) * force
        return forceX, forceY

    def update(self, planets):
        totalForceY = totalForceX = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            totalForceX += fx
            totalForceY += fy

        self.xVel += totalForceX / self.mass * Gl.TIME_STEP
        self.yVel += totalForceY / self.mass * Gl.TIME_STEP

        self.x += self.xVel * Gl.TIME_STEP
        self.y += self.yVel * Gl.TIME_STEP
        self.orbit.append((self.x, self.y))
