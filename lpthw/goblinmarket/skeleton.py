
pockets = ["bead", "rock", "seeds"]
#Map bits
class Map(object):
#What do I want all places to have in common?
	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass

	def enter(self, enter_message):
		print(enter_message)


#Inventory bits
class Inventory(object):

	def enter(self):
		pass

class Item(Inventory):

	def __init__(self, desc, connected_item, connected_place):
		self.item = item

	def trade():
		if item in pockets:
			item.print(trade_message)
			pockets.remove(item)
			pockets.insert(0, connected_item)
		else:
			print("error")
			exit()


#example child classes

class Shinies(Map):
#
	enter_message = ("A crow is proudly guarding a large assortment of shiny things. \n" +
		"It eyes you curiously as you approach and croaks a greeting. Do \n" + 
		"you have anything to offer?")


class Bead(Item):
#	
	trade_message = "You trade the bead for amber."
	connected_item = "amber"

class Amber(Item):
#	
	trade_message = "You trade the amber for a bead."
	connected_item = "bead"


a_map = Map("Shinies")
a_map.enter()
