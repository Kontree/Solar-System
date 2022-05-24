import pygame as pg
import math as mt
import Planets as Pl
import Globales as Gl
import Player as Plr
pg.init()


screen = pg.display.set_mode((Gl.WIDTH, Gl.HEIGHT))
pg.display.set_caption('Solar System')


def main():
    running = True
    clock = pg.time.Clock()
    player = Plr.Player(5 * 10**22, Gl.NEUTRAL, 8, '')
    sun = Pl.Planet(0, 0, 30, Gl.YELLOW, 1.98892 * 10**30, 'Sun')
    sun.isSun = True
    earth = Pl.Planet(-Gl.AU, 0, 10, Gl.BLUE, 5.9742 * 10**24, 'Earth', 29.783 * 1000)
    mars = Pl.Planet(-1.524 * Gl.AU, 0, 8, Gl.RED, 6.39 * 10**23, 'Mars', 24.077 * 1000)
    mercury = Pl.Planet(-0.387 * Gl.AU, 0, 5, Gl.DARK_GREY, 3.30 * 10**23, 'Mercury', 47.4 * 1000)
    venus = Pl.Planet(-0.723 * Gl.AU, 0, 9, Gl.WHITE, 4.8685 * 10**24, 'Venus', 35.02 * 1000)
    Gl.planets = [sun, earth, mars, mercury, venus]

    while running:
        clock.tick(Gl.FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos_down = pg.mouse.get_pos()
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                pos_up = pg.mouse.get_pos()
                planet = player.create_planet(pos_down, pos_up)
                Gl.planets.append(planet)
        screen.fill(Gl.BLACK)
        for planet in Gl.planets:
            planet.update(Gl.planets)
            planet.draw(screen)
        pg.display.flip()

    pg.quit()


main()
