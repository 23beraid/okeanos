#Inventory = ["Miner's Pick", "Copper", "Silver", "Gold"]
def ConvertCuToAg(Inventory):
	if "Copper" in Inventory:
		if "Miner's Pick" in Inventory:
			Inventory.remove("Copper")
			Inventory.append("Silver")
			return "Your Copper has successfuly been converted into Silver!"
		else:
			return "You don't have the Miner's Pick!"
	else:
		return "You don't have any Copper!"
def ConvertAgToAu(Inventory):
	if "Silver" in Inventory:
		if "Miner's Pick" in Inventory:
			Inventory.remove("Silver")
			Inventory.append("Gold")
			return "Your Silver has successfuly been converted into Gold!"
		else:
			return "You don't have the Miner's Pick!"
	else:
		return "You don't have any Silver!"			
#ConvertCuToAg()
#ConvertAgToAu()
