import pygame as pg
import time
import math
import random


pg.init()
width = 640
height = 480
fps = 30
clock = pg.time.Clock()
win = pg.display.set_mode((width, height))
pg.display.set_caption('Collision study')

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
colors = [red, green, blue, pink, white]

# not working
class CircleHollow():
    def __init__(self, win):
        self.win = win
        # self.lines = [(10,10),(40,10),(10,40),(40,40)]
        self.len = 1
        self.x = [0, 270, 265]
        self.y = [0, 30, 30]
        self.degree = 0
        self.done = False



    def update(self):
        if self.degree < 364:
        # pg.draw.line(self.win, white, self.lines, 1)
            self.x[1] = self.x[2] + math.cos(math.radians(self.degree)) * self.len
            self.y[1] = self.y[2] + math.sin(math.radians(self.degree)) * self.len
            self.x[2] = self.x[1] + math.cos(math.radians(self.degree)) * self.len
            self.y[2] = self.y[1] + math.sin(math.radians(self.degree)) * self.len
            points =[(self.x[2],self.y[2]), (self.x[1],self.y[2])]
            pg.draw.lines(self.win, red, False, points, 1)
            self.degree+=5
        else:
            self.done = True


class Circle():
    def __init__(self, win):
        self.win = win
        self.len = 1
        self.degree = -90
        self.center = (266, 52)
        self.len = 15
        self.xy1 = [25, 25]
        # self.xy2 = [360, 40]
        # self.xy3 = [300, 50]
        # self.xy4 = [360, 50]
        self.done = False


    def update(self):
        if self.degree < 274:
            self.xy1[0] = self.center[0] + math.cos(math.radians(self.degree)) * self.len
            self.xy1[1] = self.center[1] + math.sin(math.radians(self.degree)) * self.len

            # self.xy2[0] = self.center[0] + math.cos(math.radians(self.degree)) * self.len
            # self.xy2[1] = self.center[1] + math.sin(math.radians(self.degree)) * self.len
            #
            # self.xy3[0] = self.center[0] + math.cos(math.radians(self.degree)) * self.len
            # self.xy3[1] = self.center[1] + math.sin(math.radians(self.degree)) * self.len
            #
            # self.xy4[0] = self.center[0] + math.cos(math.radians(self.degree)) * self.len
            # self.xy4[1] = self.center[1] + math.sin(math.radians(self.degree)) * self.len

            pg.draw.line(self.win, random.choice(colors), self.center, self.xy1, 1)
            # pg.draw.line(self.win, white, self.center, self.xy2, 1)
            # pg.draw.line(self.win, green, self.center, self.xy3, 1)
            # pg.draw.line(self.win, pink, self.center, self.xy4, 1)
            self.degree+=5
        else:
            self.done = True


class ProgressBarColor():
    def __init__(self, win):
        self.win = win
        self.a = 255
        self.b = 0
        self.i = 0
        self.x = 10
        self.y = 50
        self.done = False

    def update(self):
        if self.a > 0 and self.b < 255:
            pg.draw.line(win, (self.a, self.b, 0),
                         (self.x, self.y), (self.x, self.y+5), 1)
            self.i += 1
            self.x += 3
            self.a -= 3.5
            self.b += 2
        else:
            print(self.x)
            print(self.y)
            self.done = True


def step():
    circle_hollow = CircleHollow(win)
    progress_bar_color = ProgressBarColor(win)
    circle = Circle(win)
    run = True

    while run:
        clock.tick(fps)
        for i in pg.event.get():
            if i.type == pg.QUIT: exit()

        if not progress_bar_color.done:
            progress_bar_color.update()
        elif not circle_hollow.done:
            circle_hollow.update()
        elif not circle.done:
            circle.update()

        # circle.update()
        # circle_hollow.update()
        # progress_bar_color.update()
        pg.display.update()





step()
pg.quit()
