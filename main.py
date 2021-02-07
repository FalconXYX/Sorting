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
        self.color = white

    def draw(self,win):
        pygame.draw.rect(display, white, (self.x, self.y, self.w, self.h))
def makevariables(xpos, lengths, numberofblocks, vari):
    for x in range(0,numberofblocks):
        l = (x*15)+50
        xposition = (x * 15) + 50
        xpos.append(xposition)
        lengths.append(l)
        vari.append(box(xposition,l,display))
makevariables(xofblock, heightofblock, count, varaibles)
class button():
    def __init__(self,x,win, type):
        self.x = x
        self.type = type
        self.clickedon = False



    def draw(self,win):
        pygame.draw.rect(display, red, (self.x, 0, 140, 40))
        font = pygame.font.SysFont('comicsans', 35)
        if (self.type == "b" ):
            text = font.render("Bubble Sort", 1, (0, 0, 0))
        if (self.type == "s"):
            text = font.render("Selection", 1, (0, 0, 0))
        if (self.type == "h"):
            text = font.render("Heap", 1, (0, 0, 0))
        display.blit(text, (self.x, 0))
    def hit(self, c, v):
        if(self.clickedon == False):
            pygame.event.get()
            mouse = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            press = pygame.mouse.get_pressed()
            mousexbubble = mouse[0] > 0 and mouse[0] < 150
            mousexheap = mouse[0] > 400 and mouse[0] < 550
            mousexselection = mouse[0] > 200 and mouse[0] < 350
            mouseybubble = mouse[1] > 0 and mouse[1] < 40
            click = press[0] == 1
            if(self.type == "b" and mousexbubble and mouseybubble and click):
                self.clickedon = True
                bubblesort(c, v)
            if (self.type == "h" and mousexheap and mouseybubble and click):
                self.clickedon = True
                heapsort(v)
            if(self.type == "s" and mousexselection and mouseybubble and click):
                selctionsort(c, v)
                self.clickedon = True

def makevariables(xpos, lengths, numberofblocks, vari):
    for x in range(0,numberofblocks):
        l = (x*15)+50
        xposition = (x * 15) + 50
        xpos.append(xposition)
        lengths.append(l)
        vari.append(box(xposition,l,display))
def radomize_order():
    random.shuffle(xofblock)
    for p in range(0, count):
        varaibles[p].x = xofblock[p]

def drawbox(win):
    for x in range(0, count):

        varaibles[x].color = (255,255,255)
        varaibles[x].draw(win)

def mixpos(varaible, numbers):
    for x in range(1,1000):
        rnum = random.randint(0, numbers-1)
        rnum2 = random.randint(0, numbers-1)
        temp = varaible[rnum]
        varaible[rnum] = varaible[rnum2]
        varaible[rnum2] = temp

radomize_order()

pygame.display.set_caption("Sort")
pygame.init()
def bubblesort(number,vari):
    global  actions
    actions = 0
    now = time.time()
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
    print("It took: " + str(actions) + " actions to sort")
    timetook = round(1000 * (time.time() - now), 3)
    print("It took: " + str(timetook) + " milliseconds to sort ")
    avg = round(timetook / actions, 6)
    print("Each action took on average: " + str(avg) + " milliseconds")

    print(actions)

def selctionsort(number, vari):
    global actions

    actions = 0
    numberoftries = 0
    buffer = vari[0]
    banned = []
    small = box(1000,1000,display)
    mixpos(vari, number)
    now = time.time()
    activelist = vari.copy()
    for b in range(0,55):
        if(len(activelist) > 1):
            actions += 1
            for x in activelist:
                if(small.h > x.h):
                    small = x

            for p in activelist:
                if(p.x == (b*15)+50):
                    buffer = p
                    break


            firstx = buffer.x
            secondx = small.x

            buffer.x = secondx
            small.x = firstx
            activelist.pop(activelist.index(small))
            small = box(1000, 1000, display)


        else:
            print("It took: "+ str(actions)+" actions to sort")
            timetook = round(1000*(time.time()-now),3)
            print("It took: "+str(timetook) +" milliseconds to sort ")
            avg = round(timetook/actions,6)
            print("Each action took on average: "+ str(avg) +" milliseconds")
            break


def heapwithsort(vari, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if( l < heapsize and vari[largest].h < vari[l].h):
        largest = l


    if( r < heapsize and vari[largest].h < vari[r].h):
        largest = r


    if( largest != i):
        vari[i].h, vari[largest].h = vari[largest].h, vari[i].h  # swap

        heapwithsort(vari, i, largest)
def heapsort(vari):

    heapsize = len(vari)
    for i in range(heapsize // 2 - 1, -1, -1):
        heapwithsort(vari, heapsize, i)

        # One by one extract elements
    for i in range(heapsize - 1, 0, -1):
        vari[i].h, vari[0].h = vari[0].h, vari[i].h  # swap
        heapwithsort(vari, i, 0)










run = True
clik = True
bbutton = button(0,display,"b")
sbutton = button(200,display,"s")
hbutton = button(400,display,"h")
while run:
    display.fill((black))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run  = False




    drawbox(display)
    bbutton.hit(count, varaibles)
    hbutton.hit(1, varaibles)
    sbutton.hit(count, varaibles)
    bbutton.draw(display)
    hbutton.draw(display)
    sbutton.draw(display)


    pygame.display.update()
pygame.quit()
quit()