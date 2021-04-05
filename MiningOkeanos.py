import time
def Copper():
	Copper.CopperAmount = 1
def Silver():
	Silver.SilverAmount = 1
def Gold():
	Gold.GoldAmount = 1
Inventory = ["Miner's Pick"]
#you can always add on to the inventory later on
	def ConvertCuToAg():
		Copper()
		if Copper.CopperAmount > 0:
			if "Miner's Pick" in Inventory:
				Copper()
				Silver()
				Copper.CopperAmount -= 1
				time.sleep(7200)
				Silver.SilverAmount+=1
	def ConvertAgToAu():
		Silver()
		if Silver.SilverAmount > 0:
			if "Miner's Pick" in Inventory:
				Silver()
				Gold()
				Silver.SilverAmount-=1
				time.sleep(7200)
				Gold.GoldAmount+=1
#ConvertCuToAg()
#ConvertAgToAu()

#If the player has a (Miner's Pick) in their invertory, they unlock the two functions above
#The player can now state either function to convert.
