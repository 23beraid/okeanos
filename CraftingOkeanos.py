#Adventurescrown: 1 Ruby, 1 Aquamarine, 1 Amethyst
#Magesrobe: 1 Emerald, 1 Diamond, 1 Topaz
#CraftWarriorshelm: 1 Amethyst, 1 Emerald, 1 Ruby
#Alchemistsbeaker: 1 Topaz, 1 Aquamarine, 1 Diamond
#Minerspick: 1 Diamond, 1 Emerald, 1 Ruby
inventory=db['inv'+str(message.author.id)]
UI=[]
CI=[]
def UniqueGen(UI):
	for x in Inventory:
		if x not in UI:
			UI.append(x)
def CraftAdventurerscrown(Inventory):
	UniqueGen(UI)
	if "Ruby" in Inventory:
		CI.append("Ruby")
		i=0
		for x in UI:
			if x=="Aquamarine":
				CI.append(x)
			elif x=="Amethyst":
				CI.append(x)
		if len(CI)<3:
			return "You lack the necessary minerals"
		else:
			for x in CI:
				Inventory.remove(x)
			return "You have sucessfuly crafted an Adventurers Crown"
			Inventory.append("Adventurers Crown")
			CI.clear()
	else:
		return "You lack a Ruby"
def CraftMagesrobe(Inventory):
	UniqueGen(UI)
	if "Emerald" in Inventory:
		CI.append("Emerald")
		i=0
		for x in UI:
			if x=="Diamond":
				CI.append(x)
			elif x=="Topaz":
				CI.append(x)
		if len(CI)<3:
			return "You lack the necessary minerals"
		else:
			for x in CI:
				Inventory.remove(x)
			return "You have sucessfuly crafted a Mages robe"
			Inventory.append("Mages robe")
			CI.clear()
	else:
		return "You lack an Emerald"
def CraftWarriorshelm(Inventory):
	UniqueGen(UI)
	if "Amethyst" in Inventory:
		CI.append("Amethyst")
		i=0
		for x in UI:
			if x=="Emerald":
				CI.append(x)
			elif x=="Ruby":
				CI.append(x)
		if len(CI)<3:
			return "You lack the necessary minerals"
		else:
			for x in CI:
				Inventory.remove(x)
			return "You have sucessfuly crafted a Mages robe"
			Inventory.append("Warriors helm")
			CI.clear()
	else:
		return "You lack an Amethyst"
def CraftAlchemistsbeaker(Inventory):
	UniqueGen(UI)
	for x in UI:
		if x=="Topaz":
			CI.append(x)
		elif x=="Aquamarine":
			CI.append(x)
		elif x=="Diamond":
			CI.append(x)
	if len(CI)<3:
		return "You lack the necessary minerals"
	else:
		for x in CI:
			Inventory.remove(x)
		return "You have sucessfuly crafted an Alchemists Beaker"
		Inventory.append("Alchemists Beaker")
		CI.clear()
def CraftMinerspick(Inventory):
	UniqueGen(UI)
	for x in UI:
		if x=="Diamond":
			CI.append(x)
		elif x=="Emerald":
			CI.append(x)
		elif x=="Ruby":
			CI.append(x)
	if len(CI)<3:
		return "You lack the necessary minerals"
	else:
		for x in CI:
			Inventory.remove(x)
		return "You have sucessfuly crafted a Miners Pick"
		Inventory.append("Miners Pick")
		CI.clear()
#CraftAdventurerscrown(Inventory)
#CraftMagesrobe(Inventory)
#CraftWarriorshelm(Inventory)
#CraftAlchemistsbeaker(Inventory)
#CraftMinerspick(Inventory)
