from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
class Roof:
    offsetx = 0
    offsety = 0
    offsetz = 0
    def __init__(self, offsetx, offsety, offsetz):
        self.offsetx = offsetx
        self.offsety = offsety
        self.offsetz = offsetz

    def verticlesRoof(self, offsetx, offsety, offsetz):
        verticlesForTriangle2 = (
            (1+self.offsetx,1+self.offsety,-1+self.offsetz), #0
            (0+self.offsetx,0+self.offsety,0+self.offsetz), #1
            (0+self.offsetx,2+self.offsety,0+self.offsetz), #2
            (1+self.offsetx,1+self.offsety,1+self.offsetz),  #3
            (-1+self.offsetx,1+self.offsety,-1+self.offsetz), #4
            (-1+self.offsetx,1+self.offsety,1+self.offsetz) #5
        )
        return verticlesForTriangle2

    def edgesRoof(self):
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

    colorsForTriangle = (
        (1,0,0),
        (1,0,0),
        (1,0,0),
        (1,0,0)
    )
    def show_triangle(self):
        glBegin(GL_LINES)
        for edge in self.edgesRoof():
            for vertex in edge:
                glVertex3fv(self.verticlesRoof(self.offsetx, self.offsety, self.offsetz)[vertex])
        glEnd()
        
        glBegin(GL_TRIANGLES)
        for surface in self.surfacesForTriangle:
            for i, vertex in enumerate(surface):
                glColor3fv(self.colorsForTriangle[i])
                glVertex3fv(self.verticlesRoof(self.offsetx, self.offsety, self.offsetz)[vertex])
        glEnd()

    def moveDeep(self, deep):
        self.offsetz=deep 

    def moveWidth(self, width):
        self.offsetx=width
