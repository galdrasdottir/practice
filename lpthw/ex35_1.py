pockets = ["bead", "rock", "seeds"]


def shinies_stall():
	print("A crow is proudly guarding a large assortment of shiny things.")
	print("It eyes you curiously as you approach and croaks a greeting.")
	print("Do you have anything to offer?")

	next = input("> ")

	if "bead" in next:
		tradebead()
		market()
	elif "rock" in next:
		if "rock" in pockets:
			print("The crow pecks at the rock a few times and then stops to think.")
			print("Eventually it appears to accept it and adds it to its stash.")
			print("In return it tosses you a sweet wrapped in a crinkly foil.")
			pockets.remove("rock")
			pockets.insert(1, "sweet")
			return pockets
			market()
		else:
			print("You don't have", next, "in your pockets.")
			market()

	else:
		fail("The crow is no longer interested in you.")
		market()


def tradebead():
	if "bead" in pockets:
		print("The crow hops excitedly as you offer your bead.")
		print("It rummages around its wares and eventually drops a piece of amber in front of you.")
		print("Encased in its orange glow you see a fly.")
		pockets.remove("bead")
		pockets.insert(0, "amber")
		return pockets
	else:
		print("You can't trade with this.")



def checkpocket(passed_pocket):
	print("You have", passed_pocket, "in your pocket.")

def change_pockets():
	local_pocket = 
	checkpocket(local_pocket)

print(pockets)
shinies_stall()

