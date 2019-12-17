# Panda3DFPScamera
This is a FPS camera class for Panda3D. It is designed to be easily imported so it can be used in many projects.

# Installing and importing
Download and copy the cameraController.py to your device.
First import the class with `from cameraController import *`.
Camera needs keymap to be supplied to it `self.map = base.win.get_keyboard_map()`.
After this initialize the camera `self.test_camera = FPScamera(self.map,base)`

To run the camera run these functions in a loop.
`self.test_camera.checkButton(base)` and `self.test_camera.cameraControl()`
# Example Program
```python
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
``` 
Example file is provied also. It has no objects to show camera easily but it works. If moving the camera keeps spazzing it's view weirdly check if you have dissabled Panda3D's own debug camera by using `base.disableMouse()`. Having this option on can cause problems in some cases.

# Controls
- w, a, s and d to move
- holding left alt releases the mouse from middle of the screen

# Function list

- `__init__()`: initializes the code
- `checkButton(base)`: Checks pressed buttons and changes their value in the list that is read later to move camera
- `print(text)`: Classed print command to print stuff with ####FPScamera: prefix
- `setKey(key,value)`: Changes Keys value. Is it pressed or not?
- `speedControl(mole)`: Changes camera movement speed with keyboard. Supply more or less string as a variable to change speed.
- `cameraControl()`: Manages the rotation of the camera also moves the camera if Key value is True so if wanted key is pressed.
- `toggleDebug()`: Toggles camera debug info printing.
- ´freeMouse()´: Toggles if mouse can be moved freely in the program window. When this is active `cameraControl()` dissables the movement of the camera (the view) at the same time.
