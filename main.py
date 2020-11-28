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

def selctionsort(number, vari):
    global actions
    actions = 0
    numberoftries = 0
    buffer = vari[0]
    bufferid = 0
    small = 100000000000
    activelist = vari
    for x in range(0,2):
        small = activelist[0]
        for p in activelist:
            if(p.x == (bufferid*15)+50):
                buffer = p
        if(small != buffer):
            print("if")
            firstx = buffer.x
            secondx = small.x
            buffer.x = secondx
            small.x = firstx
            activelist.pop(activelist.index(small))





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
    mousexbubble = mouse[0] >0 and mouse[0] < 150
    mouseybubble = mouse[1] > 0 and mouse[1] < 40
    click = press[0] == 1


    font = pygame.font.SysFont('comicsans', 35)
    text = font.render("Bubble Sort", 1, (0, 0, 0))
    pygame.draw.rect(display,red, (0,0, 150, 40))
    display.blit(text, (0, 0))
    drawbox(display)
    if (mousexbubble and mouseybubble and click and clik == True):
        selctionsort(count, varaibles)
        clik = False

    pygame.display.update()
pygame.quit()
quit()