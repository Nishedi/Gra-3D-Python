from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from Cords import Cords
class Cube:
    colors = (155, 143, 129)

    surfaces = (
        (0, 1, 2, 3),
        (0, 1, 5, 4),
        (0, 4, 7, 3),
        (4, 5, 6, 7),
        (3, 2, 6, 7),
        (1, 5, 6, 2)
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
    size = 0
    offsetx=0
    offsety=0
    offsetz=0

    def __init__(self, size, offsetx, offsety, offsetz, color):
        self.size=size
        self.offsetx=offsetx
        self.offsety=offsety
        self.offsetz=offsetz
        self.colors=color

    def verticlesHause(self):
        
        vertices = (
            (self.size+self.offsetx,  -self.size+self.offsety,    -self.size+self.offsetz),
            (self.size+self.offsetx,  -self.size+self.offsety,    self.size+self.offsetz),
            (-self.size+self.offsetx, -self.size+self.offsety,    self.size+self.offsetz),
            (-self.size+self.offsetx, -self.size+self.offsety,    -self.size+self.offsetz),

            (self.size+self.offsetx,     self.size+self.offsety,  -self.size+self.offsetz),
            (self.size+self.offsetx,     self.size+self.offsety,  self.size+self.offsetz),
            (-self.size+self.offsetx,    self.size+self.offsety,  self.size+self.offsetz),
            (-self.size+self.offsetx,    self.size+self.offsety,  -self.size+self.offsetz)
        )
        return vertices


    def show_cube(self):
        verticles =self.verticlesHause()
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(verticles[vertex])
        glEnd()

        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for i, vertex in enumerate(surface):
                glColor3fv(self.colors)
                glVertex3fv(verticles[vertex])
        glEnd()
        return 
    
    def returnFront(self):
        verticles =self.verticlesHause()
        return (verticles[1][2], verticles[2][0], verticles[0][0])

    def moveDeep(self, deep):
        self.offsetz=deep  

    def moveWidth(self, width):
        self.offsetx=width

    def checkCollision(self, zone):
        verticles =self.verticlesHause()
        if zone[0] >= 0.9:
            if verticles[2][0]<=zone[2]:
                if verticles[2][0]>=zone[1]:
                    return True
            if verticles[0][0]>=zone[1]:
                if verticles[0][0]<=zone[2]:
                    return True
        return False