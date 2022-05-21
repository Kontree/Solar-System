import pygame as pg
import math as mt
import Planets as Pl
import Globales as Gl

pg.init()


screen = pg.display.set_mode((Gl.WIDTH, Gl.HEIGHT))
pg.display.set_caption('Solar System')


def main():
    running = True
    clock = pg.time.Clock()

    sun = Pl.Planet(0, 0, 30, Gl.YELLOW, 1.98892 * 10**30)
    sun.isSun = True
    earth = Pl.Planet(-Gl.AU, 0, 10, Gl.BLUE, 5.9742 * 10**24)
    earth.yVel = 29.783 * 1000
    mars = Pl.Planet(-1.524 * Gl.AU, 0, 8, Gl.RED, 6.39 * 10**23)
    mars.yVel = 24.077 * 1000
    mercury = Pl.Planet(-0.387 * Gl.AU, 0, 5, Gl.DARK_GREY, 3.30 * 10**23)
    mercury.yVel = 47.4 * 1000
    venus = Pl.Planet(-0.723 * Gl.AU, 0, 9, Gl.WHITE, 4.8685 * 10**24)
    venus.yVel = 35.02 * 1000
    planets = [sun, earth, mars, mercury, venus]

    while running:
        clock.tick(Gl.FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(Gl.BLACK)
        for planet in planets:
            planet.update(planets)
            planet.draw(screen)
        pg.display.flip()

    pg.quit()
main()