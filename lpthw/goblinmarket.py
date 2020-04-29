from sys import exit

pockets = ["bead", "rock", "seeds"]
shopping = ['leeks', 'bread', 'enchanted ring']


def shinies_stall():
	print("A crow is proudly guarding a large assortment of shiny things.")
	print("It eyes you curiously as you approach and croaks a greeting.")
	print("Do you have anything to offer?")

	next = input("> ")

	if "bead" in next:
		tradebead()
	elif "rock" in next:
		traderock()
	else:
		print("The crow is no longer interested in you.")
		market()


def seed_stall():
	print("A red-cheeked gnome, almost invisible amongst large crates of veg, hails you.")
	print("They gesture excitedly at their display.")
	print("Do you have anything to offer?")

	next = input("> ")

	if "seeds" in next:
		tradeseeds()
	else:
		print("The gnome is no longer interested in you.")
		market()

def trinket_stall():
	print("A large toad, unmoving on a huge lead, hovers gently just off the ground.")
	print("It is wearing rings on every finger, with more jewellery peeking out from under its belly.")
	print("It does not respond to any call or salutation.")
	
	if "amber" in pockets:
		print("Suddenly, one of its eyes snaps open and fixes on you with a calculating stare.")
		print("What do you do?")
		next = input("> ")

		if "amber" in next:
			tradeamber()
		else:
			print("The eye closes again with what almost seems to be disappointment.")
			print("With a wave from its hand you're transported back to the rest of the market.")
			market()

	else:
		print("One eye opens and a low, threatening croak starts to build in the toad's throat.")
		print("One of its ringed fingers twitches and you find yourself lifted off the ground and deposited back in the market square.")
		market()

def bakery_stall():
	print("A red squirrel flits back and forth between tasks around its stall.")
	print("There is a frantic air about it, and you see no items currently for sale.")
	print("As you approach, the squirrel stops its nervous work and welcomes you.")
	print("While wiping its front paws on its apron, it apologises for the empty display.")
	print("'The awful goat over there stole all my goods while I was unloading more flour.")
	print("It'll be a few hours till the next lot is done I'm afraid.'")
	print("What do you do?")
	next = input("> ")

	if "goat" in next:
		goat()
	else:
		print("You return to the market.")
		market()

def goat():
	print("The goat grazes nonchalantly on an empty grassy patch. You can see crumbs all around it.")
	print("Its yellow glare concentrates on you as you come closer, and you get the questionable pleasure of seeing its square pupils stay firmly in place while it lifts its head.")
	print("Do you have anything to offer?")
	next = input("> ")

	if "sweet" in next:
		tradesweet()
	else:
		print("The goat sniffs your", next, "dismissively, then bites your hand hard. Maybe it's better to leave.")
		market()


def tradebead():
	if "bead" in pockets:
		print("The crow hops excitedly as you offer your bead.")
		print("It rummages around its wares and eventually drops a piece of amber in front of you.")
		print("Encased in its orange glow you see a fly.")
		pockets.remove("bead")
		pockets.insert(0, "amber")
		market()
	else:
		print("You can't trade with this.")
		market()


def tradeseeds():
	if "seeds" in pockets:
		print("The gnome nods sagely and takes your seeds.")
		print("You point at the leeks, he nods and packs a few up for you.")
		pockets.pop()
		pockets.append("leek")
		market()
	else:
		print("You can't trade with this.")
		market()


def traderock():
	if "rock" in pockets:
		print("The crow pecks at the rock a few times and then stops to think.")
		print("Eventually it appears to accept it and adds it to its stash.")
		print("In return it tosses you a sweet wrapped in a crinkly foil.")
		pockets.remove("rock")
		pockets.insert(1, "sweet")
		market()
	else:
		print("You can't trade with this.")
		market()


def tradeamber():
	print("As you touch your piece of amber, an excited shudder ripples all over the toad.")
	print("Before you can do anything else, it leaps up and paws at you until it has extracted the piece.")
	print("In its eagerness it does not notice that one of the rings has slipped off its fingers.")
	print("While the toad stares lovingly at the amber-encased fly, you pick up the ring. Seems only fair.")
	pockets.remove("amber")
	pockets.insert(0, "ring")
	market()

def tradesweet():
	if "sweet" in pockets:
		print("The goat's ears perk up as it hears the sound of the crinkly wrapper.")
		print("It can't get it fast enough out of your hand and gobbles the sweet, wrapper and all.")
		print("A second later it stops, makes a coughing sound and moves away.")
		print("You can now see that behind it a single whole loaf of bread remains.")
		print("As you pick it up, the goat coughs again and regurgitates the now empty wrapper. Apparently unharmed, it settles down to graze again.")
		pockets.remove("sweet")
		pockets.insert(1, "bread")
		market()
	else:
		print("You don't have this on you.")
		market()


def market():
	print("You're in the market square. What do you do?")

	next = input("> ")

	if "stall" in next:
		stalls()
	elif "pocket" in next:
		check_pockets()
	elif "list" in next:
		shopping_list()
	elif "shopping" in next:
		shopping_list()
	elif "gnome" in next:
		seed_stall()
	elif "crow" in next:
		shinies_stall()
	elif "squirrel" in next:
		bakery_stall()
	elif "toad" in next:
		trinket_stall()
	elif "goat" in next:
		goat()
	elif "exit" in next:
		print("Do you really want to go home before finishing your shopping? Y/N")
		next = input("> ")

		if "Y" in next:
			print("Alright! Time to go home.")
			exit()
		elif "N" in next:
			print("Okay. Back to the market.")
			stalls()
		else:
			print("I don't understand. Please try again.")
			stalls()
	else:
		print("Try something else.")
		stalls()


def stalls():
	print("While business is winding down, there are still a number of open stalls.")
	print("Enticing smells waft your way from a squirrel-run bakery, next to which a goat \nis grazing.")
	print("The caws of a crow among a pile of assorted shiny oddities and the calls of a gnome \ndwarfed by the crates of vegetables around him vie for your attention.")
	print("A twinkle of magic alerts you to a large toad sat on a leaf in the shade next to \na puddle.")
	print("Which vendor are you interested in?")
	next = input("> ")


	if "gnome" in next:
		seed_stall()
	elif "crow" in next:
		shinies_stall()
	elif "squirrel" in next:
		bakery_stall()
	elif "toad" in next:
		trinket_stall()
	elif "goat" in next:
		goat()
	elif "pocket" in next:
		check_pockets()
	elif "list" in next:
		shopping_list()
	elif "shopping" in next:
		shopping_list()
	else:
		print("That's not an option.")
		market()


def check_pockets():
	print("You have", pockets, "in your pocket.")
	market()

def shopping_list():
	print("Your shopping list reads:")

	for item in shopping:
		print("\t-%s" % item)

	if "ring" and "leek" and "bread" in pockets:
		print("Good job, you've completed your shopping!")
		exit(0)
	else: 
		print("You still have some things to buy.")
		market()	


print("""
		You find yourself on the corner of a sleepy market,
		with your shopping list in hand and a few things to barter with
		in your pocket. A small number of stalls is still open.
		""")
market()



