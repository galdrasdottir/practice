
#Map bits

class Scene(object):

	def enter_message(self):
		pass


class MapEngine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def move(self):
		current_scene = self.scene_map.opening_scene()
		next_scene = current_scene.enter_message()


class Shinies(Scene):
#
	def enter_message(self):
		print("A crow is proudly guarding a large assortment of shiny things. \n" +
		"It eyes you curiously as you approach and croaks a greeting. Do \n" + 
		"you have anything to offer?")
		return 

	def return_message(self):
		print("The crow remembers you.")
		return


class Stalls(Scene):

	def enter_message(self):
		print("While business is winding down, there are still a number of open stalls. \n" +
		"Enticing smells waft your way from a squirrel-run bakery, next to which a goat \n" +
		"is grazing. The caws of a crow among a pile of assorted shiny oddities and the \n" +
		"calls of a gnome dwarfed by the crates of vegetables around him vie for your \n" +
		"attention. A twinkle of magic alerts you to a large toad sat on a leaf in the \n" +
		"shade next to a puddle. \nWhich vendor are you interested in?")
		return


class Map(object):

	scenes = {
	"stalls": Stalls(), "vendors": Stalls(), 
#	"squirrel": bakery, "bakery": bakery, 
	"crow": Shinies(), "shinies": Shinies(), "shiny": Shinies(), "oddities": Shinies(),
#	"gnome": vegetables, "vegetables": vegetables,
#	"toad": toad, "magic": toad, "puddle": toad, "leaf": toad,
#	"goat": goat
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)


print("""
		You find yourself on the corner of a sleepy market,
		with your shopping list in hand and a few things to barter with
		in your pocket. A small number of stalls is still open.
		""")
print("Where do you want to go?")
next = input("> ")
a_map = Map(next)
a_game = MapEngine(a_map)
a_game.move()
