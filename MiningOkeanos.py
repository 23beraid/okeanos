Inventory = ["Miner's Pick", "Copper", "Silver", "Gold"]
def ConvertCuToAg():
	if "Copper" in Inventory:
		if "Miner's Pick" in Inventory:
			Inventory.remove("Copper")
			Inventory.append("Silver")
def ConvertAgToAu():
	if "Silver" in Inventory:
		if "Miner's Pick" in Inventory:
			Inventory.remove("Silver")
			Inventory.append("Gold")
#ConvertCuToAg()
#ConvertAgToAu()

