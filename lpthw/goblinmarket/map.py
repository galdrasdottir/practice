
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
		


class Stalls(Scene):

	def enter_message(self):
		print("While business is winding down, there are still a number of open stalls. \n" +
		"Enticing smells waft your way from a squirrel-run bakery, next to which a goat \n" +
		"is grazing. The caws of a crow among a pile of assorted shiny oddities and the \n" +
		"calls of a gnome dwarfed by the crates of vegetables around him vie for your \n" +
		"attention. A twinkle of magic alerts you to a large toad sat on a leaf in the \n" +
		"shade next to a puddle. \nWhich vendor are you interested in?")


class Bakery(Scene):

	def enter_message(self):
		print("A red squirrel flits back and forth between tasks around its stall.\n" +
		"There is a frantic air about it, and you see no items currently for sale.\n" +
		"As you approach, the squirrel stops its nervous work and welcomes you.\n" +
		"While wiping its front paws on its apron, it apologises for the empty\n" + 
		"display. 'The awful goat over there stole all my goods while I was \n" +
		"unloading more flour. It'll be a few hours till the next lot is done \n" +
		"I'm afraid.'\nWhat do you do?")
		next = input("> ")


class Shinies(Scene):
#
	def enter_message(self):
		print("A crow is proudly guarding a large assortment of shiny things. \n" +
		"It eyes you curiously as you approach and croaks a greeting. Do \n" + 
		"you have anything to offer?")
 

	def return_message(self):
		print("The crow remembers you.")
		return


class Vegetables(Scene):
	
	def enter_message(self):
		print("A red-cheeked gnome, almost invisible amongst large crates of veg, hails \n" +
		"you. They gesture excitedly at their display.\nDo you have anything to offer?")



class Toad(Scene):

	def enter_message(self):
		print("A large toad, unmoving on a huge lead, hovers gently just off the ground.\n" +
		"It is wearing rings on every finger, with more jewellery peeking out from \n" +
		"under its belly.\nIt does not respond to any call or salutation.")



class Goat(Scene):

	def enter_message(self):
		print("The goat grazes nonchalantly on an empty grassy patch. You can see crumbs\n" +
		"all around it. Its yellow glare concentrates on you as you come closer, and you\n" +
		"get the questionable pleasure of seeing its square pupils stay firmly in place\n" +
		"while it lifts its head.\nDo you have anything to offer?")



class Map(object):

	scenes = {
	"stalls": Stalls(), "vendors": Stalls(), 
	"squirrel": Bakery(), "bakery": Bakery(), 
	"crow": Shinies(), "shinies": Shinies(), "shiny": Shinies(), "oddities": Shinies(),
	"gnome": Vegetables(), "vegetables": Vegetables(),
	"toad": Toad(), "magic": Toad(), "puddle": Toad(), "leaf": Toad(),
	"goat": Goat()
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
