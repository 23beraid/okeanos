import time
def Copper():
	Copper.CopperAmount = 1
def Silver():
	Silver.SilverAmount = 1
def Gold():
	Gold.GoldAmount = 1
Inventory = ["Miner's Pick"]
#you can always add on to the inventory later on
if "Miner's Pick" in Inventory:
	def ConvertCuToAg():
		Copper()
		Silver()
		Copper.CopperAmount -= 1
		time.sleep(7200)
		Silver.SilverAmount+=1
	def ConvertAgToAu():
		Silver()
		Gold()
		Silver.SilverAmount-=1
		time.sleep(7200)
		Gold.GoldAmount+=1
#ConvertCuToAg()
#ConvertAgToAu()

#If the player has a (Miner's Pick) in their invertory, they unlock the two functions above
#The player can now state either function to convert.
