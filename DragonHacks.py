from direct.showbase.ShowBase import ShowBase
from math import pi,sin,cos
from direct.task import Task
import time

class Chemplay(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        #Uncomment once this function is finished.
        self.accept('time-a',self.CallspinCB)

    def CallspinCB(self,when):
        print "repeat a"
        taskMgr.add(self.spinCB, "spin")


    def spinCB(self,task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.scene.setHpr(angleDegrees, 0, 0)
        return Task.cont



app = Chemplay()
app.run()
