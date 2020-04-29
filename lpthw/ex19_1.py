def merchant_wares(mushrooms, moths, shiny_things):
	print("The merchant has %d mushrooms." % mushrooms)
	print("They also have %d fluttery moths." % moths)
	print("If you're very nice, they might also show you %d shiny things.\n" % shiny_things)

prompt = "> "

print("The merchant spreads out their wares for you.")
merchant_wares(14, 7, 8)

print("How many mushrooms would you like to buy?")
sold_mushrooms = input(prompt)
numbered_mushrooms = int(sold_mushrooms)

print("This is what is left:")
unsold_mushrooms = 14 - numbered_mushrooms
moths = 7
shiny_things = 8

merchant_wares(unsold_mushrooms, moths, shiny_things)


