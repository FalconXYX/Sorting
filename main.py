import pygame
from pygame.locals import *
import os
import sys
import time
import pyinputplus as pyip
import random
import sorting
global varaibles
global display
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
display_width = 1000
display_height =900
display= pygame.display.set_mode((display_width, display_height))
count = pyip.inputNum("Enter a number with a between 5 and 55", min=5, max=55)
heightofblock  = []
xofblock = []
varaibles = []


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
class box():
    def __init__(self,x,l,win):
        self.x = x
        self.y = 50
        self.h = l
        self.w = 10
        self.color = red

    def draw(self,win):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))
def makevariables(xpos, lengths, numberofblocks, vari):
    for x in range(0,numberofblocks):
        l = (x*15)+50
        xposition = (x * 15) + 50
        xpos.append(xposition)
        lengths.append(l)
        vari.append(box(xposition,l,display))
makevariables(xofblock, heightofblock, count, varaibles)
def radomize_order():
    random.shuffle(xofblock)
    for p in range(0, count):
        varaibles[p].x = xofblock[p]

def drawbox(win):
    for x in range(0, count):

        varaibles[x].color = (255,255,255)
        varaibles[x].draw(win)


radomize_order()

pygame.display.set_caption("Sort")
pygame.init()
def bubblesort(number,vari):
    global  actions
    actions = 0
    numberoftries = 0
    for p in range (1,number):
        if (numberoftries == number):
            break
        numberoftries = 0
        for cords in range(0, len(vari)):
            try:
                actions += 1
                first = varaibles[cords]
                second = varaibles[cords+1]
                firstx = first.x
                secondx  = second.x
                if(first.x > second.x):
                    first.x = secondx
                    second.x = firstx

                else:

                    if (numberoftries == number):
                        break
                    numberoftries +=1

            except:
                break
    print(actions)
run = True
clik = True
keys = pygame.key.get_pressed()
while run:
    display.fill((black))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run  = False
    pygame.event.get()
    mouse = pygame.mouse.get_pos()
    press = pygame.mouse.get_pressed()
    mousex = mouse[0] >0 and mouse[0] < 50
    mousey = mouse[1] > 0 and mouse[1] < 50
    click = press[0] == 1

    if(mousex and mousey and click and clik == True):
        bubblesort(count, varaibles)
        clik = False

    pygame.draw.rect(display,red, (0,0, 50, 50))
    drawbox(display)

    pygame.display.update()
pygame.quit()
quit()