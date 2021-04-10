Victiminv=db['inv'str(userid)]
Inventory=db['inv'+str(message.author.id)]
def StealfromVictim(Victiminv,Inventory,userid):
	if "Mages robe" not in Victiminv:
		if "Warriors helm" in Inventory:
			i=input("What item do you want to steal: ")
			for x in Victiminv:
				if x == i:
					Inventory.append(x)
					Victiminv.remove(x)
					break
		else:
			return "You need a Mages Robe to steal"
	else:
		return "The recipient can not be stolen from"
#StealfromVictim(Victiminv,Inventory,userid)

