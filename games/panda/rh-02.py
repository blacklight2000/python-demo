import direct.directbase.DirectStart
from direct.showbase.ShowBase import ShowBase
from panda3d.core import GeoMipTerrain, Filename
from direct.task import Task

class Application(ShowBase):
        def __init__(self):
               	ShowBase.__init__(self)
               	self.terrain = GeoMipTerrain("terrain")
               	self.terrain.setHeightfield("/Developer/Panda3D/models/maps/envir-reeds.png")
                self.terrain.setColorMap("/Developer/Panda3D/models/maps/envir-ground.jpg")
                self.terrain.setBlockSize(32)
		self.terrain.setNear(40)
		self.terrain.setFar(100)
		# self.terrain.setBruteForce(1)
               	self.terrain.getRoot().setSz(200)
		self.terrain.getRoot().setScale(0.025)
               	self.terrain.getRoot().reparentTo(self.render)
               	self.terrain.generate()
               	# z = self.terrain.getElevation(256, 256) * 40
               	# self.camera.setPos(256, 256, z)
               	# self.terrain.setFocalPoint(self.camera)
               	# self.taskMgr.add(self.updateTerrain, "update terrain")

	def updateTerrain(self, task):
    		self.terrain.update()
    		return task.cont

MyApp = Application()
MyApp.run()
