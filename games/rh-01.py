from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import Vec3
       
class Application(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		self.environ = self.loader.loadModel("models/environment")
		self.environ.reparentTo(self.render)
		self.environ.setPos(-5, 0, 0)
		self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
		self.pandaActor.reparentTo(self.render)
		self.pandaActor.setPos(Vec3(5, 0, 0))
		self.pandaActor.loop("walk")
                self.environ.setScale(5.0, 5.0, 5.0)
		self.camera.setPos(-15, -30, 6)

app = Application()
app.run()

