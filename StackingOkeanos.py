#This will seperate the unique items, count them, and convert into dictionary. SI_dct is the new Inventory dictionary.
Inventory = ["Miner's Pick", "Copper", "Silver", "Gold", "Copper", "Gold", "Gold"]
UI=[]
SI=[]
def UniqueGen(UI, Inventory):
	for x in Inventory:
		if x not in UI:
			UI.append(x)
def Convert2Dct(SI):
    SI_dct = {SI[i]: SI[i + 1] for i in range(0, len(SI), 2)}
	return "SI_dct"
def StackInventory(UniqueGen,UI,Inventory):
	UniqueGen(UI, Inventory)
	for x in UI:
		SI.append(x)
		SI.append(str(Inventory.count(x)))
	return Convert2Dct(SI)

#return StackInventory(UniqueGen,UI,Inventory)
