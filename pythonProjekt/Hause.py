from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
from Roof import Roof
from Door import Door
from Window import Window
class Hause:
    windowList= []
    cube = Cube(0,0,0,0,0)
    def __init__(self, distanceWidth, distanceDeep):
        self.cube = Cube(1,distanceWidth,0,distanceDeep, 0)
        self.roof = Roof(distanceWidth,0,distanceDeep)
        self.door = Door(distanceWidth,0,distanceDeep-1)
        self.windowList.append(Window(distanceWidth,0,distanceDeep-1, 0.65, 0, 0,0))
        self.windowList.append(Window(distanceWidth,0,distanceDeep-1, -0.65, 0,0,0))
        self.windowList.append(Window(distanceWidth,0,distanceDeep-1, 0.65, 1, 0,-0.3))
        self.windowList.append(Window(distanceWidth,0,distanceDeep-1, -0.65, 1, 0.3,0))
        

    def move(self, deep, incrementer):
        self.cube.moveDeep(deep, incrementer)
        self.roof.moveDeep(deep)
        self.door.moveDeep(deep)
        for window in self.windowList:
            window.moveDeep(deep)

    def showHouse(self):
        self.door.show_cube()
        self.cube.show_cube()
        self.roof.show_triangle()
        for window in self.windowList:
            window.show_cube()
