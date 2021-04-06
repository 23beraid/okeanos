#Inventory = ["Miner's Pick", "Copper", "Silver", "Gold", "Copper"]
def Convert1AgTo2Cu(Inventory):
	if "Silver" in Inventory:
		Inventory.remove("Silver")
		for x in range (0,2):
			Inventory.append("Copper")
		return "Your Silver has successfuly been converted into 2 Copper!"
	else:
		return "You don't have any Silver!"
def Convert1AuTo3Cu(Inventory):
	if "Gold" in Inventory:
		Inventory.remove("Gold")
		for x in range (0,3):
			Inventory.append("Copper")
		return "Your Gold has successfuly been converted into 3 Copper!"
	else:
		return "You don't have any Gold!"	
#Convert1AgTo2Cu()
#Convert1AuTo3Cu()

