Inventory = ["Miner's Pick", "Copper", "Silver", "Gold", "Copper"]
def Convert1AgTo2Cu():
	if "Silver" in Inventory:
		Inventory.remove("Silver")
		x=0
		for x in range (0,2):
			Inventory.append("Copper")
			x+=1
		return "Your Silver has successfuly been converted into 2 Copper!"
	else:
		return "You don't have any Silver!"
def Convert1AuTo3Cu():
	if "Gold" in Inventory:
		Inventory.remove("Gold")
		x=0
		for x in range (0,3):
			Inventory.append("Copper")
			x+=1
		return "Your Gold has successfuly been converted into 3 Copper!"
	else:
		return "You don't have any Gold!"	
#Convert1AgTo2Cu()
#Convert1AuTo3Cu()

