from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
from Roof import Roof
from Door import Door
from Window import Window
import random
class Hause:
    windowList= []
    cube = Cube(0,0,0,0,0)
    offsetz = -45
    def __init__(self, distanceWidth, distanceDeep):
        self.cube = Cube(1,distanceWidth,0,self.offsetz, self.generateRandomPossition(0, 4))
        self.roof = Roof(distanceWidth,0,self.offsetz)
        self.door = Door(distanceWidth,0,self.offsetz)
        self.windowList.append(Window(distanceWidth,0,self.offsetz, 0.65, 0, 0,0))
        self.windowList.append(Window(distanceWidth,0,self.offsetz, -0.65, 0,0,0))
        self.windowList.append(Window(distanceWidth,0,self.offsetz, 0.65, 1, 0,-0.3))
        self.windowList.append(Window(distanceWidth,0,self.offsetz, -0.65, 1, 0.3,0))
    
    def generateRandomPossition(self,lowerBound, upperBound):
        return random.randint(lowerBound, upperBound)

    def move(self, deep, incrementer):
        self.offsetz += incrementer
        self.cube.moveDeep(self.offsetz)
        self.roof.moveDeep(self.offsetz)
        self.door.moveDeep(self.offsetz)
        for window in self.windowList:
            window.moveDeep(self.offsetz)
    
    def crashWindow(self):
        self.windowList.clear()


    def showHouse(self):
        self.door.show_cube()
        self.cube.show_cube()
        self.roof.show_triangle()
        for window in self.windowList:
            window.show_cube()
