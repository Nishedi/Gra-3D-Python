import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Cube import Cube
from Hause import Hause
from Wood import Wood
from Rock import Rock
import random
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18, glutBitmapCharacter


def generateRandomPossition(lowerBound, upperBound):
    return random.randint(lowerBound, upperBound)

def renderString(x, y, string):
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(x, y)
    for c in string:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))
        
def light():
    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 0)) # źródło światła left, top, front

    # Ustawienie koloru światła otoczenia
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1.0, 0.0, 0.0, 1.0))

    # Ustawienie koloru światła rozproszonego
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.0, 0.0, 1.0, 1.0))

    # Ustawienie koloru światła wypukłego
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 1.0, 0.0, 1.0))
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE )


def chechCollision2(list, cubeMini):
    for item in list:
        if cubeMini.checkCollision(item.returnFront())==True:
            print("kolizja")
            return True
    return False

def draw_grass(offset):
    glBegin(GL_QUADS)
    glColor3f(0.522*0.8, 0.984*0.8, 0.1*0.8)  # Kolor trawy
    glVertex3f(-100, -1, -50)
    glVertex3f(100, -1, -50)
    glVertex3f(100, -1, 10)
    glVertex3f(-100, -1, 10)

    glColor3f(0, 0, 0)  # Kolor trawy
    glVertex3f(-2, -0.9, -100)
    glVertex3f(2, -0.9, -100)
    glVertex3f(2, -0.9, 10)
    glVertex3f(-2, -0.9, 10)

    x=10
    offset = offset % 45
    for i in range(0, 10):
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(-0.1, -0.88, x+offset+45)
        glVertex3f(0.1, -0.88, x+offset+45)
        glVertex3f(0.1, -0.88, x-10+offset+45)
        glVertex3f(-0.1, -0.88, x-10+offset+45)
        x = x - 15
    glEnd()  



def main():
    points = 0
    zebra = 0
    glutInit()
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

   
    # glEnable(GL_LIGHTING)
    # glEnable(GL_LIGHT0)
    # glEnable(GL_COLOR_MATERIAL)

    glEnable(GL_DEPTH_TEST)
    side = 0
    distanceDeep = -45
    distanceWidth = generateRandomPossition(4,5)
    incrementer = 0.001
    incrementer = 0.05
   

   
    cubeMini = Cube(0.1, side, -0.6,1, 1)
    
    objList = []
    objList.append(Hause(distanceWidth,distanceDeep))
    objList.append(Hause(-distanceWidth,distanceDeep))

    blockades = []
    timetowait = 10
    glRotatef(15, 3, 0, 0)
    movement = True
    probability = 500000
    blockProbability = 200
    start = True
    stop = False   
        
    while True:
        if start:
            glClearColor(0, 0.6, 1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            renderString(-1.5,1,"Witaj w grze! Twoim zadaniem jest unikanie przeszkod!")
            renderString(-1,0.5,"Nacisnij spacje aby rozpoczac gre!")
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start= False
            pygame.display.flip()
            pygame.time.wait(timetowait)
            continue
        if stop:
            glClearColor(0, 0.6, 1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            renderString(-0.4,1,"Koniec gry!")
            renderString(-0.49,0.5,"Twoj wynik: "+str(points))
            renderString(-1.05,0,"Nacisnij spacje aby zakonczyc gre!")
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return
            pygame.display.flip()
            pygame.time.wait(timetowait)
            continue
        
        glClearColor(0, 0.6, 1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if side < 2:
                        side += 0.5
                if event.key == pygame.K_LEFT:
                    if side > -2:
                        side -= 0.5
                if event.key == pygame.K_DOWN:
                    distanceDeep-=1
                    zebra += -1
                    incrementer -= 0.01
                if event.key == pygame.K_UP:
                    distanceDeep+=1
                    zebra += 1
                    incrementer += 0.01

                if event.key == pygame.K_d:
                    glRotatef(5, 0, 1, 0) 
                if event.key == pygame.K_a:
                    glRotatef(-5, 0, 1, 0) 
                if event.key == pygame.K_s:
                    glRotatef(5, 1, 0, 0) 
                if event.key == pygame.K_w:
                    glRotatef(-5, 1, 0, 0) 
                if event.key == pygame.K_r:
                    glRotatef(5, 0, 0, 1) 
                if event.key == pygame.K_f:
                    glRotatef(-5, 0, 0, 1) 
                if event.key == pygame.K_c: # wylaczenie aplikacje klawiszem C
                    return
        renderString(-2.5,1.8,"Twoj wynik: "+str(points))
        draw_grass(zebra)
        cubeMini.moveWidth(side)
        cubeMini.show_cube()
        for hause in objList:
            if movement == True:
                hause.move(distanceDeep, incrementer)
            hause.showHouse()
        for blockade in blockades:
            if movement == True:
                blockade.moveTest(incrementer)
            blockade.show_cube()
            
        
        light()
        collision2 = chechCollision2(blockades, cubeMini)
        if  collision2 == False:
            movement = True
            distanceDeep += incrementer
            zebra += incrementer
            #incrementer += 0.001
        else:
            stop = True

        for blockade in blockades:
            if blockade.offsetz>=6:
                if(blockProbability>10):
                    blockProbability-=5
                blockades.remove(blockade)
                points+=10
                incrementer += 0.02


        if distanceDeep >= 6:
            for hause in objList:
                hause.crashWindow()
            objList.clear()
            distanceDeep = -55
            objList.append(Hause(distanceWidth,distanceDeep))
            objList.append(Hause(-distanceWidth,distanceDeep))
    
        if generateRandomPossition(0,probability)==1:
            objList.append(Hause(distanceWidth,distanceDeep))
            objList.append(Hause(-distanceWidth,distanceDeep))

        if generateRandomPossition(0,blockProbability)==1:
            WoodOrRock = generateRandomPossition(0,2)
            possition = generateRandomPossition(0,10)/5
            sign = generateRandomPossition(0,2)
            if sign == 0:
                possition = -possition

            if WoodOrRock == 1:
                blockades.append(Rock(0.1,possition,-0.7))
            if WoodOrRock == 0:
                blockades.append(Wood(0.5,possition,-0.3))

        pygame.display.flip()
        pygame.time.wait(timetowait)

main()