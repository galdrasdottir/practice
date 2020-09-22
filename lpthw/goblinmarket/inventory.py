
pockets = ["bead", "rock", "seeds"]

class Item(object):

	def trade_message(self):
		pass


class TradeEngine(object):

	def __init__(self, in_inventory):
		self.in_inventory = in_inventory

	def trade(self):
		current_item = self.in_inventory.transfer_item()
		pockets.remove(current_item.named_item())
		swapped_item = current_item.trade_message()
		pockets.append(swapped_item)


class Bead(Item):
#	
	def named_item(self):
		return "bead"

	def trade_message(self):
		print("The crow hops excitedly as you offer your bead.It rummages around its \n" +
			"wares and eventually drops a piece of amber in front of you. Encased in \n" +
			"its orange glow you see a fly.")
		return "amber"


class Amber(Item):
#	
	def trade_message(self):
		print("You trade the amber for a bead.")


class Inventory(object):

	items = {
		"bead": Bead(),
		"amber": Amber()
	}

	def __init__(self, start_item):
		self.start_item = start_item
		
	def get_item(self, item_name):
		return Inventory.items.get(item_name)

	def transfer_item(self):
		return self.get_item(self.start_item)




print(pockets)

in_inventory = Inventory("bead")
an_item = TradeEngine(in_inventory)
an_item.trade()

print(pockets)