'''
Camera controller for Panda3D
https://github.com/cmdtvt/Panda3DFPScamera


'''
from math import pi, sin, cos

class FPScamera():
    def __init__(self,map,base):
        
        self.debug = True
        self.mouseInUse = True #### If false releases the mouse so it can be moved freely
        self.cameraSpeed = 30
        self.testlockx = 0
        self.testlocky = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.sensitivity = 20

        #### Camera positioning system ####
        self.current_camera = 0
        self.cameras = {'testingcamera': {'position': [0.0, 0.0, 0.0], 'roatation': 'allowed'}}
        if self.debug == True:
            self.print("Saved camera positions: "+str(self.cameras))
        
        #################################################################################
        #### All allowed keys are stored in dictionary                               ####
        #### If you need to add things to FPS camera you must first add it to keyMap ####
        #################################################################################
        self.keyMap = {"w" : False, "s" : False, "a" : False, "d" : False,"lalt": False,"lshift": False,"space": False, "n" : False, "m" : False, "b" : False}
        self.map = map

        self.print(self.map.get_mapped_button("space"))
        self.w_button = self.map.get_mapped_button("w")
        self.a_button = self.map.get_mapped_button("a")
        self.s_button = self.map.get_mapped_button("s")
        self.d_button = self.map.get_mapped_button("d")
        self.b_button = self.map.get_mapped_button("b")
        self.lalt_button = self.map.get_mapped_button("lalt")
        self.lshift_button = self.map.get_mapped_button("lshift")
        self.space_button = self.map.get_mapped_button("space")

        self.windowXsize = base.win.getXSize()
        self.windowYSize = base.win.getYSize()

    def checkKeyPressed(self,button,key):
        #### Toggles value in self.keyMap to true or false depending if key is pressed down.
        if base.mouseWatcherNode.is_button_down(button):
            self.setKey(key,True)
        else:
            self.setKey(key,False)
        
    #### Keyboard checks ####
    def checkButton(self,base):
        if base.mouseWatcherNode.is_button_down(self.w_button):
            if self.debug == True:
                self.print("Button: "+str(self.w_button)+" is pressed")

        if base.mouseWatcherNode.is_button_down("mouse1"):
            self.speedControl("more")
            
        if base.mouseWatcherNode.is_button_down("mouse3"):
            self.speedControl("less")

        ### Run key checks and toggles ####
        self.checkKeyPressed(self.w_button,"w")
        self.checkKeyPressed(self.a_button,"a")
        self.checkKeyPressed(self.s_button,"s")
        self.checkKeyPressed(self.d_button,"d")

        self.checkKeyPressed(self.lshift_button,"lshift")
        self.checkKeyPressed(self.space_button,"space")

        self.checkKeyPressed(self.lalt_button,"lalt")

                    
    def print(self,text):
        print("[FPScamera]: "+str(text))

    #### This changes keys value in self.keyMap ####
    def setKey(self, key, value):
        self.keyMap[key] = value

    #### Well this controls the speed + and - ####
    def speedControl(self,mole):
        speedamount = 10
        if mole == "more":
            self.cameraSpeed += speedamount
            if self.debug == True:
                self.print("More Speed!")
                
        elif mole == "less":
            self.cameraSpeed -= speedamount
            if self.debug == True:
                self.print("Less Speed!")
        else:
            if self.debug == True:
                self.print("Error in SpeedControl!")

        if self.cameraSpeed < 0:
            self.cameraSpeed = 0

    #### This is the actual camera ####
    def cameraControl(self,):
        dt = globalClock.getDt()
        self.windowXsize = base.win.getXSize()
        self.windowYSize = base.win.getYSize()

        if (self.keyMap["lalt"] == True):
            self.mouseInUse = False
        else:
            base.win.movePointer(0, int(self.windowXsize/2) , int(self.windowYSize/2))
            self.mouseInUse = True

            
        #### This stuff is executed if mouse is on screen i think ####
        if(base.mouseWatcherNode.hasMouse() == True):
            mpos = base.mouseWatcherNode.getMouse()
            base.mouseWatcherNode.set_effects


            if self.mouseInUse == True:
                base.win.movePointer(0, int(self.windowXsize/2) , int(self.windowYSize/2))
                #### Checks if camera is moving left or right ####
                if mpos[0] <= 0.0000 or mpos[0] >= 0.0000:
                    self.testlockx -= (mpos[0]*self.sensitivity)
                    base.camera.setH(self.testlockx)

                #### Checks up and down movement ####
                if mpos[1] <= 0 or mpos[1] >= 0:
                    self.testlocky += (mpos[1]*self.sensitivity)
                    base.camera.setP(self.testlocky)

            
        if(self.keyMap["w"] == True):
            base.camera.setY(base.camera, self.cameraSpeed * dt)
            if self.debug == True:
                self.print("camera moving forward")
        
        if(self.keyMap["s"] == True):
            base.camera.setY(base.camera, -self.cameraSpeed * dt)
            if self.debug == True:
                self.print("camera moving backwards")
        
        if(self.keyMap["a"] == True):
            base.camera.setX(base.camera, -self.cameraSpeed * dt)
            if self.debug == True:
                self.print("camera moving left")
        
        if(self.keyMap["d"] == True):
            base.camera.setX(base.camera, self.cameraSpeed * dt)
            if self.debug == True:
                self.print("camera moving right")
                
        if(self.keyMap["lshift"] == True):
            base.camera.setZ(base.camera, -self.cameraSpeed * dt)
            if self.debug == True:
                self.print("camera moving down")

        if(self.keyMap["space"] == True):
            base.camera.setZ(base.camera, self.cameraSpeed * dt)
            if self.debug == True:
                self.print("camera moving up")
                

    def saveCamera(self,name):
        self.cameras[name] = {"position" : [base.camera.getX(),base.camera.getY(),base.camera.getZ()],"roatation":"allowed"}
        print(self.cameras)

    def loadCamera(self,name):
        cameraInfo = self.cameras[name]
        base.camera.setX(base.camera,cameraInfo["position"][0])
        base.camera.setY(base.camera,cameraInfo["position"][1])
        base.camera.setZ(base.camera,cameraInfo["position"][2])
        if self.debug == True:
            self.print("Camera: "+name+" loaded!")
        
    
    def toggleDebug(self,):
        if self.debug == False:
            self.debug = True
        else:
            self.debug = False
        self.print("Toggled debug to: "+str(self.debug))

    def freeMouse(self,):
        if self.mouseInUse == False:
            self.mouseInUse = True
            self.print("Mouse is free.")
        else:
            self.mouseInUse = False
            self.print("Mouse Locked.")
        
        



    


            



