import random
#Adventurescrown: 1 Ruby, 1 Aquamarine, 1 Amythyst
#Magesrobe: 1 Emerald, 1 Diamond, 1 Topaz
#CraftWarriorshelm: 1 Amythyst, 1 Emerald, 1 Ruby
Inventory=["Ruby","Emerald", "Aquamarine", "Topaz","Diamond","Amythyst"]
UI=[]
CI=[]
def UniqueGen():
	for x in Inventory:
		if x not in UI:
			UI.append(x)
def CraftAdventurerscrown():
	UniqueGen()
	if "Ruby" in Inventory:
		CI.append("Ruby")
		i=0
		for x in UI:
			if x=="Aquamarine":
				CI.append(x)
			elif x=="Amythyst":
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
def CraftMagesrobe():
	UniqueGen()
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
def CraftWarriorshelm():
	UniqueGen()
	if "Amythyst" in Inventory:
		CI.append("Amythyst")
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
		return "You lack an Amythyst"
#CraftAdventurerscrown()
#CraftMagesrobe()
#CraftWarriorshelm()


