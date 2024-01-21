from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random
class Wood:
    colors = (155, 143, 129)

    surfaces = (
        (0, 1, 2, 3),
        (0, 1, 5, 4), # prawa strona domu
        (0, 4, 7, 3), # nieistotna
        (4, 5, 6, 7), # gora
        (3, 2, 6, 7), # lewa strona domu
        (1, 5, 6, 2) # przod domu
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
    right=0
    yleft=0
    deep = 5

    
    
    def __init__(self, size, offsetx, offsety):
        self.size=size
        self.offsetx=offsetx
        self.offsety=offsety
        self.colors=(0.5, 0.35, 0.05)
        self.right=self.generateRandomPossition(0,10)/10
        self.left=self.generateRandomPossition(0,10)/10
        self.offsetz=-45

    def generateRandomPossition(self,lowerBound, upperBound):
        return random.randint(lowerBound, upperBound)
    
    def verticlesHause(self):
        x = 0.75
        vertices = (
            (self.size+self.offsetx,  -self.size+self.offsety,    -self.size+self.offsetz+self.right),
            (self.size+self.offsetx,  -self.size+self.offsety,    self.size+self.offsetz-x+self.right),
            (-self.size+self.offsetx, -self.size+self.offsety,    self.size+self.offsetz-x+self.left),
            (-self.size+self.offsetx, -self.size+self.offsety,    -self.size+self.offsetz+self.left),

            (self.size+self.offsetx,     self.size+self.offsety-0.9,  -self.size+self.offsetz+self.right),
            (self.size+self.offsetx,    self.size+self.offsety-0.9,  self.size+self.offsetz-x+self.right),
            (-self.size+self.offsetx,    self.size+self.offsety-0.9,  self.size+self.offsetz-x+self.left),
            (-self.size+self.offsetx,    self.size+self.offsety-0.9,  -self.size+self.offsetz+self.left)
        )
        return vertices


    def show_cube(self):
        verticles =self.verticlesHause()
        glBegin(GL_LINES)
        glColor3fv((0.5*1.1, 0.35*1.1, 0.05*1.1))
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(verticles[vertex])
        glEnd()

        glBegin(GL_QUADS)
        k = 0
        for surface in self.surfaces:
            wsp = 20/(self.deep)
            colorx = self.colors
            color2 = (colorx[0] * wsp, colorx[1] * wsp, colorx[2] * wsp)
            glColor3fv(color2)
            
            for i, vertex in enumerate(surface):
                glVertex3fv(verticles[vertex])
        
        
        glEnd()
        return 
    
    def returnFront(self):
        verticles =self.verticlesHause()
        return (verticles[1][2], verticles[2][0], verticles[0][0])

    def moveDeep(self, deep):
        self.offsetz=deep

    def moveTest(self, incrementer):
        self.offsetz+=incrementer  
        

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