Inventory = ["Miner's Pick", "Copper", "Silver", "Gold"]
def ConvertCuToAg():
	if "Copper" in Inventory:
		if "Miner's Pick" in Inventory:
			Inventory.remove("Copper")
			Inventory.append("Silver")
			print("Your Copper has successfuly been converted into Silver!")
		else:
			print("You don't have the Miner's Pick!")
	else:
		print("You don't have any Copper!")
def ConvertAgToAu():
	if "Silver" in Inventory:
		if "Miner's Pick" in Inventory:
			Inventory.remove("Silver")
			Inventory.append("Gold")
			print("Your Silver has successfuly been converted into Gold!")
		else:
			print("You don't have the Miner's Pick!")
	else:
		print("You don't have any Silver!")			
#ConvertCuToAg()
#ConvertAgToAu()
