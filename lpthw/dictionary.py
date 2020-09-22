# input options to call the relevant methods. In the future.



class Map(object):
#What do I want all places to have in common?
	def enter()

class Place(Map):

	def __init__(self, room):
		self.room = room

class Shinies(Place):

	print("A crow is proudly guarding a large assortment of shiny things. \n" +
		"It eyes you curiously as you approach and croaks a greeting. Do \n" + 
		"you have anything to offer?")

def vegetables():
	print("A red-cheeked gnome, almost invisible amongst large crates of veg, hails you.")

def toad():
	print("A large toad, unmoving on a huge lead, hovers gently just off the ground.")

def bakery():
	print("A red squirrel flits back and forth between tasks around its stall.")

def goat():
	print("The goat grazes nonchalantly on an empty grassy patch. You can see crumbs all around it.")

def stalls():
	print("While business is winding down, there are still a number of open stalls.")

def shopping_list():
	print("Your shopping list reads:")

def check_pockets():
	print("You check your pockets.")

options = {
	"stalls": stalls, "vendors": stalls, 
	"squirrel": bakery, "bakery": bakery, 
	"crow": shinies, "shinies": shinies, "shiny": shinies, "oddities": shinies,
	"gnome": vegetables, "vegetables": vegetables,
	"toad": toad, "magic": toad, "puddle": toad, "leaf": toad,
	"pockets": check_pockets, "barter": check_pockets,
	"shopping": shopping_list, "list": shopping_list,
	"goat": goat
	}







	

def test_dic():
	print("What do you want out of the dictionary?")
	next = input("> ")
#call method with variable options, then
	if next in options.keys():
		next_action = options[next]
		places.next_action()
	else:
		print("That didn't work.")

test_dic()

