import direct.directbase.DirectStart
from direct.showbase.DirectObject import DirectObject

#### Import camera controller ####
from cameraController import *

class Game(DirectObject):
    def __init__(self):


        self.map = base.win.get_keyboard_map() #### Get keymap
        self.test_camera = FPScamera(self.map,base) #### Initialize camera and pass keymap to it
    
        taskMgr.add(self.cameraLoop, "CameraLoop")


    def cameraLoop(self,task):

        self.test_camera.checkButton(base) #### Run keyboard checks for camera
        self.test_camera.cameraControl() #### Thing that moves the camera mouse and keybaord.
        
        return task.cont

        
g = Game()
run()
