import random
def adventureReward():
	Artifact_list = ["Air Scepter","Earth Scepter","Fire Scepter",
	"Water Scepter","Air Amulet", "Earth Amulet","Fire Amulet",
	"Water Amulet","Air Scroll", "Earth Scroll","Fire Scroll",
	"Water Scroll","Air Rune","Earth Rune","Fire Rune","Water Rune"]
	Mineral_list = ["Ruby","Emerald","Aquamarine","Topaz","Diamond","Amythyst"]
	RanList = [1,2,3,4,5,6,7,8,9,10]
	randomran = random.choice(RanList)
	Mineral_list = random.choice(Mineral_list)
	Artifact_list = random.choice(Artifact_list)
	if randomran == 9:
		return Mineral_list
	elif randomran == 10:
		return Mineral_list
	else:
		return Artifact_list
#adventureReward()
