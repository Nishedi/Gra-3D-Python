import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0.1,  -0.1,    -0.1),
    (0.1,  -0.1,    0.1),
    (-0.1, -0.1,    0.1),
    (-0.1, -0.1,    -0.1),

    (0.1,     0.1,  -0.1),
    (0.1,     0.1,  0.1),
    (-0.1,    0.1,  0.1),
    (-0.1,    0.1,  -0.1)
)
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

surfaces = (
    (0, 1, 2, 3),
    (0, 1, 5, 4),
    (0, 4, 7, 3),
    (4, 5, 6, 7),
    (3, 2, 6, 7),
    (1, 5, 6, 2)
)

colors = (
    #(1, 0, 0),
    #(1, 1, 0),
    #(1, 0, 1),
    #(0, 0, 1),
    #(0, 1, 1),
    #(0, 1, 0)
    (0, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0)
)

def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for surface in surfaces:
        for i, vertex in enumerate(surface):
            glColor3fv(colors[i])
            # glColor3fv((1.0, 1.0, 1.0))
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_DEPTH_TEST)

    x_rotation = 0
    y_rotation = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            y_rotation += 0.1
        if keys[pygame.K_RIGHT]:
            y_rotation -= 0.1
        if keys[pygame.K_UP]:
            x_rotation += 0.1
        if keys[pygame.K_DOWN]:
            x_rotation -= 0.1
        if keys[pygame.K_r]:
            x_rotation = 0
            y_rotation = 0

        glRotatef(x_rotation, 1, 0, 0)
        glRotatef(y_rotation, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
