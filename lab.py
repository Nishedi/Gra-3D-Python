import pygame
from pygame.locals import *
from math import cos, sin, radians
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
from Hause import Hause
from Wood import Wood
from Rock import Rock
import random

def generateRandomPossition(lowerBound, upperBound):
    return random.randint(lowerBound, upperBound)

def light():
    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 0)) # źródło światła left, top, front

    # Ustawienie koloru światła otoczenia
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1.0, 0.0, 0.0, 1.0))

    # Ustawienie koloru światła rozproszonego
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.0, 0.0, 1.0, 1.0))

    # Ustawienie koloru światła wypukłego
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 1.0, 0.0, 1.0))
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE )

def chechCollision(list, cubeMini):
    for item in list:
        if cubeMini.checkCollision(item.cube.returnFront())==True:
            return True
    return False

def draw_grass(offset):
    glBegin(GL_QUADS)

    glColor3f(0.522, 0.984, 0.1)  # Kolor trawy
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
   

   
    cubeMini = Cube(0.1, side, -0.6,1, 1)
    
    objList = []
    objList.append(Hause(distanceWidth,distanceDeep))
    objList.append(Hause(-distanceWidth,distanceDeep))
    timetowait = 10
    glRotatef(15, 3, 0, 0)
    wood = Rock(0.1,0,-0.7,0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    side += 0.5
                if event.key == pygame.K_LEFT:
                    side -= 0.5
                if event.key == pygame.K_DOWN:
                    distanceDeep-=1
                    zebra += -1
                if event.key == pygame.K_UP:
                    distanceDeep+=1
                    zebra += 1

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
    
        glClearColor(0, 0.6, 1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_grass(zebra)
        cubeMini.moveWidth(side)
        cubeMini.show_cube()
        wood.moveDeep(distanceDeep+46)
        for hause in objList:
            hause.move(distanceDeep)
            hause.showHouse()
        wood.show_cube()
        light()
        collision = chechCollision(objList, cubeMini)
        wood.checkCollision
        if collision == False:
            distanceDeep += incrementer
            zebra += incrementer
            #incrementer += 0.001

            
        if distanceDeep >= 6:
            distanceDeep = -45
            points+=10*(6-distanceWidth)
            print(points)
            distanceWidth = generateRandomPossition(4,5)
            for hause in objList:
                hause.crashWindow()
            objList.clear()
            objList.append(Hause(distanceWidth,distanceDeep))
            objList.append(Hause(-distanceWidth,distanceDeep))
        pygame.display.flip()
        pygame.time.wait(timetowait)

main()