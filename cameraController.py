'''
Camera controller for Panda3D
https://github.com/cmdtvt/Panda3DFPScamera


'''
from math import pi, sin, cos
from panda3d.core import MeshDrawer, NodePath

class FPScamera():
    def __init__(self,map,base):

        
        self.debug = True
        self.cameraSpeed = 30
        self.testlockx = 0
        self.testlocky = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.sensitivity = 20
        #################################################################################
        #### All allowed keys are stored in dictionary                               ####
        #### If you need to add things to FPS camera you must first add it to keyMap ####
        #################################################################################
        self.keyMap = {"w" : False, "s" : False, "a" : False, "d" : False,}
        self.map = map

        print(self.map.get_mapped_button("w"))
        self.w_button = self.map.get_mapped_button("w")
        self.a_button = self.map.get_mapped_button("a")
        self.s_button = self.map.get_mapped_button("s")
        self.d_button = self.map.get_mapped_button("d")

        #### Because of some reason this is a camera object?!? ####


        self.windowXsize = base.win.getXSize()
        self.windowYSize = base.win.getYSize()
        
    #### Keyboard checks ####
    def checkButton(self,base):
        if base.mouseWatcherNode.is_button_down(self.w_button):
            if self.debug == True:
                self.print("Button: "+str(self.w_button)+" is pressed")


        #### Movement cheks if key is pressed move else dont move ####
        #### W ####
        if base.mouseWatcherNode.is_button_down(self.w_button):
            self.setKey("w", True)
        else:
            self.setKey("w", False)

        #### A ####
        if base.mouseWatcherNode.is_button_down(self.a_button):
            self.setKey("a", True)
        else:
            self.setKey("a", False)
            
        #### S ####
        if base.mouseWatcherNode.is_button_down(self.s_button):
            self.setKey("s", True)
        else:
            self.setKey("s", False)
            
        #### D ####
        if base.mouseWatcherNode.is_button_down(self.d_button):
            self.setKey("d", True)
        else:
            self.setKey("d", False)
        #print("controls run!")
            
    def print(self,text):
        print("####FPScamera: "+str(text))

    #### This changes keys value in self.keyMap ####
    def setKey(self, key, value):
        self.keyMap[key] = value

    #### Well this controls the speed + and - ####
    def speedControl(self,mole):
        speedamount = 10
        if mole == "more":
            self.speed += speedamount
            if self.debug == True:
                self.print("More Speed!")
                
        elif mole == "less":
            self.speed -= speedamount
            if self.debug == True:
                self.print("Less Speed!")
        else:
            self.print("Error in SpeedControl!")

    #### This is the actual camera ####
    def cameraControl(self,):
        dt = globalClock.getDt()
        self.windowXsize = base.win.getXSize()
        self.windowYSize = base.win.getYSize()

        
        #### This stuff is executed if mouse is on screen i think ####
        if(base.mouseWatcherNode.hasMouse() == True):
            mpos = base.mouseWatcherNode.getMouse()
            base.win.movePointer(0, int(self.windowXsize/2) , int(self.windowYSize/2))

            #### Checks if camera is moving left or right ####
            if mpos[0] <= 0.0000 or mpos[0] >= 0.0000:
                self.testlockx -= (mpos[0]*self.sensitivity)
                base.camera.setH(self.testlockx)

            #### Checks up and down movement ####
            if mpos[1] <= 0.0000 or mpos[1] >= 0.0000:
                print("Going Down")
                self.testlocky += (mpos[1]*self.sensitivity)
                base.camera.setP(self.testlocky)
            		
        if(self.keyMap["w"] == True):
            base.camera.setY(base.camera, self.cameraSpeed * dt)
            print("camera moving forward")
        
        elif(self.keyMap["s"] == True):
            base.camera.setY(base.camera, -self.cameraSpeed * dt)
            print("camera moving backwards")
        
        elif(self.keyMap["a"] == True):
            base.camera.setX(base.camera, -self.cameraSpeed * dt)
            print("camera moving left")
        
        elif(self.keyMap["d"] == True):
            base.camera.setX(base.camera, self.cameraSpeed * dt)
            print("camera moving right")

    def drawGUI(self,base):
        pass;



    


            



