import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def verticlesHause(offsetx,offsety,offsetz):
    vertices = (
        (1+offsetx,  -1+offsety,    -1+offsetz),
        (1+offsetx,  -1+offsety,    1+offsetz),
        (-1+offsetx, -1+offsety,    1+offsetz),
        (-1+offsetx, -1+offsety,    -1+offsetz),

        (1+offsetx,     1+offsety,  -1+offsetz),
        (1+offsetx,     1+offsety,  1+offsetz),
        (-1+offsetx,    1+offsety,  1+offsetz),
        (-1+offsetx,    1+offsety,  -1+offsetz)
    )
    return vertices

def verticlesSmallHause(side):
    height = -0.5
    deep = 1
    vertices = (
        (0.1+side,  -0.1+height,    -0.1+deep),
        (0.1+side,  -0.1+height,    0.1+deep),
        (-0.1+side, -0.1+height,    0.1+deep),
        (-0.1+side, -0.1+height,    -0.1+deep),

        (0.1+side,     0.1+height,  -0.1+deep),
        (0.1+side,     0.1+height,  0.1+deep),
        (-0.1+side,    0.1+height,  0.1+deep),
        (-0.1+side,    0.1+height,  -0.1+deep)
    )
    return vertices


def verticlesRoof(offsetx, offsety, offsetz):
    verticlesForTriangle2 = (
        (1+offsetx,1+offsety,-1+offsetz), #0
        (0+offsetx,0+offsety,0+offsetz), #1
        (0+offsetx,2+offsety,0+offsetz), #2
        (1+offsetx,1+offsety,1+offsetz),  #3
        (-1+offsetx,1+offsety,-1+offsetz), #4
        (-1+offsetx,1+offsety,1+offsetz) #5
    )
    return verticlesForTriangle2

edges = (
    (0, 1),
    (0, 3),
    (0, 4),


    (2, 1),
    (2, 3),
    (2, 6),

    (4, 5),
    (4, 7),

    (6, 5),
    (6, 7),

    (3,7),
    (1,5)
)

def edgesRoof():
    edgesForTriangle = (
        (0,2),
        (0,4),
        (0,3),
        (2,3),
        (2,4),
        (2,5)
    )
    return edgesForTriangle

surfacesForTriangle = (
    (0,2,4),
    (0,2,3),
    (2,3,5),
    (2,4,5)
)

surfaces = (
    (0, 1, 2, 3),
    (0, 1, 5, 4),
    (0, 4, 7, 3),
    (4, 5, 6, 7),
    (3, 2, 6, 7),
    (1, 5, 6, 2)
)

colorsForTriangle = (
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0)
)

colors = (
    (155, 143, 129),
    (155, 143, 129),
    (155, 143, 129),
    (155, 143, 129),
    (155, 143, 129),
    (155, 143, 129)
)

def triangle2(offsetx, offsety, offsetz):
    glBegin(GL_LINES)
    for edge in edgesRoof():
        for vertex in edge:
            glVertex3fv(verticlesRoof(offsetx, offsety, offsetz)[vertex])
    glEnd()
    
    glBegin(GL_TRIANGLES)
    for surface in surfacesForTriangle:
        for i, vertex in enumerate(surface):
            glColor3fv(colorsForTriangle[i])
            glVertex3fv(verticlesRoof(offsetx, offsety, offsetz)[vertex])
    glEnd()

def cube(offsetx, offsety, offsetz, color):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticlesHause(offsetx, offsety, offsetz)[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        for i, vertex in enumerate(surface):
            glColor3fv(color)
            glVertex3fv(verticlesHause(offsetx, offsety, offsetz)[vertex])
    glEnd()
    return


def smallCube(color, side):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticlesSmallHause(side)[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        for i, vertex in enumerate(surface):
            glColor3fv(color)
            glVertex3fv(verticlesSmallHause(side)[vertex])
    glEnd()
    return


def light():
    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 0)) # źródło światła left, top, front

    # Ustawienie koloru światła otoczenia
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1.0, 0.0, 0.0, 1.0))

    # Ustawienie koloru światła rozproszonego
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.0, 0.0, 1.0, 1.0))

    # Ustawienie koloru światła wypukłego
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 1.0, 0.0, 1.0))
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE )

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)


    #glEnable(GL_LIGHTING)
    #glEnable(GL_LIGHT0)
    #glEnable(GL_COLOR_MATERIAL)

    glEnable(GL_DEPTH_TEST)
    side = 0
    distanceDeep = -45
    distanceWidth = 2
    left = 0
    right = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #glTranslatef(-0.5, 0, 0)
                    right += 0.5
                    side += 0.1
                if event.key == pygame.K_LEFT:
                    #glTranslatef(0.5, 0, 0)
                    left += 0.5
                    side -= 0.1
                if event.key == pygame.K_DOWN:
                    distanceDeep-=1
                if event.key == pygame.K_UP:
                    #glTranslatef(0, 0, 0.5)
                    distanceDeep+=1

                if event.key == pygame.K_d:
                    #glTranslatef(-2.5, 0, 0)
                    glRotatef(5, 0, 1, 0)  # Rotate the camera to the right around the y-axis
                if event.key == pygame.K_a:
                    #glTranslatef(2.5, 0, 0)
                    glRotatef(-5, 0, 1, 0)  # Rotate the camera to the left around the y-axis
                if event.key == pygame.K_s:
                    glRotatef(5, 1, 0, 0)  # Rotate the camera downward around the x-axis
                if event.key == pygame.K_w:
                    glRotatef(-5, 1, 0, 0)  # Rotate the camera upward around the x-axis
                if event.key == pygame.K_r:
                    glRotatef(5, 0, 0, 1)  # Rotate the camera clockwise around the z-axis
                if event.key == pygame.K_f:
                    glRotatef(-5, 0, 0, 1) 
           
        #glRotatef(1, 1, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube(distanceWidth,0,distanceDeep, (1, 0.91, 0.75))
        triangle2(distanceWidth,0,distanceDeep)
        cube(-distanceWidth,0,distanceDeep, (1, 0.91, 0.75))
        triangle2(-distanceWidth,0,distanceDeep)
        light()
        smallCube((0,1,0),side)
        
        if left == distanceWidth/2:
            left = 0.5
            #glTranslatef(-0.5, 0, 0)
        if right == distanceWidth/2:
            right = 0.5
            #glTranslatef(0.5, 0, 0)
        distanceDeep += 0.01
        if distanceDeep >= 6:
            distanceDeep = -45
        pygame.display.flip()
        pygame.time.wait(10)

main()
