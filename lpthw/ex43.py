from sys import exit


"""
play method looks at a_game, which leads to the Engine function and takes self and
a_map as arguments. a_map creates an instance of the class Map, init'ed with Forest as
second argument. In Engine __init__, a_map is assigned the variable scene_map. 
The play executes, and looks up scene_map's opening_scene method. Map.opening_scene
uses Map.next_scene, which takes self and "Forest", and returns the connected class
Forest() to Map.opening_scene through use of the dictionary in Map(). This then 
returns Forest to play(), which executes the print command, calls enter() in the
child class Forest()

"""
class Scene(object):

	def enter(self):
		pass


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print("\n-------")
			next_scene_name = current_scene.enter()
			print("where is this")
			current_scene = self.scene_map.next_scene(next_scene_name)
			print(current_scene)

class Forest(Scene):

	def enter(self):
		print("You're in a forest.")
		return "Field"

class Field(Scene):

	def enter(self):
		print("You're in a field")
		exit(0)


class Map(object):

	scenes = {
		"Forest": Forest(),
		"Field": Field()
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)

#Object of Map is going to be second arg (start_scene in init)
a_map = Map("Forest")
#Object is second arg (scene_map)
a_game = Engine(a_map)
a_game.play()


