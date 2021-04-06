import random
def adventureReward():
	Artifact_list = ["Air Scepter","Earth Scepter","Fire Scepter",
	"Water Scepter","Air Amulet", "Earth Amulet","Fire Amulet",
	"Water Amulet","Air Scroll", "Earth Scroll","Fire Scroll",
	"Water Scroll","Air Rune","Earth Rune","Fire Rune","Water Rune"]
	Mineral_list = ["Ruby","Emerald","Aquamarine","Topaz","Diamond","Amythyst"]
	RanList = [1,2,3,4,5,6,7,8,9,10]
	randomran = random.choice(RanList)
	if randomran == 1:
		return(random.choice(Artifact_list))
	elif randomran == 2:
		return(random.choice(Artifact_list))
	elif randomran == 3:
		return(random.choice(Artifact_list))
	elif randomran == 4:
		return(random.choice(Artifact_list))
	elif randomran == 5:
		return(random.choice(Artifact_list))
	elif randomran == 6:
		return(random.choice(Artifact_list))
	elif randomran == 7:
		return(random.choice(Artifact_list))
	elif randomran == 8:
		return(random.choice(Artifact_list))
	elif randomran == 9:
		return(random.choice(Mineral_list))
	elif randomran == 10:
		return(random.choice(Mineral_list))
	if ramdomran == 9:
		return "You got", Mineral_List+"!"
	elif ramdomran == 10:
		return "You got", Mineral_List+"!"
	else:
		return "You got", Artifact_List+"!"

