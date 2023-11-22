import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
from Roof import Roof
from Hause import Hause

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
        

def main():
    
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
    distanceDeep=-10
    distanceWidth = 2
   
    cube1 = Cube(1,distanceWidth,0,distanceDeep, (1, 0.91, 0.75))
    cube2 = Cube(1,-distanceWidth,0,distanceDeep, (1, 0.91, 0.75))
    cubeMini = Cube(0.1, side, -0.5, 1, (0, 1, 0))
    roof1 = Roof(distanceWidth,0,distanceDeep)
    roof2 = Roof(-distanceWidth,0,distanceDeep)
    hause1 = Hause(cube1, roof1)
    hause2 = Hause(cube2, roof2)
    objList = []
    objList.append(hause1)
    objList.append(hause2)
    timetowait = 10
    glRotatef(15, 3, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    side += 0.1
                if event.key == pygame.K_LEFT:
                    side -= 0.1
                if event.key == pygame.K_DOWN:
                    distanceDeep-=1
                if event.key == pygame.K_UP:
                    distanceDeep+=1

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
           

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cubeMini.moveWidth(side)
        cubeMini.show_cube()
        
        for hause in objList:
            hause.move(distanceDeep)
            hause.showHouse()
        
        light()
        collision = chechCollision(objList, cubeMini)
        if collision == False:
            distanceDeep += 0.01
        if distanceDeep >= 6:
            distanceDeep = -45
        pygame.display.flip()
        pygame.time.wait(timetowait)

main()
