import random
Artifact_list = ["Air Scepter","Earth Scepter","Fire Scepter",
"Water Scepter","Air Amulet", "Earth Amulet","Fire Amulet",
"Water Amulet","Air Scroll", "Earth Scroll","Fire Scroll",
"Water Scroll","Air Rune","Earth Rune","Fire Rune","Water Rune"]
Mineral_list = ["Ruby","Emerald","Aquamarine","Topaz","Diamond","Amythyst"]
RanList = [1,2,3,4,5,6,7,8,9,10]
randomran = random.choice(RanList)
if randomran == 1:
	print(random.choice(Artifact_list))
elif randomran == 2:
	print(random.choice(Artifact_list))
elif randomran == 3:
	print(random.choice(Artifact_list))
elif randomran == 4:
	print(random.choice(Artifact_list))
elif randomran == 5:
	print(random.choice(Artifact_list))
elif randomran == 6:
	print(random.choice(Artifact_list))
elif randomran == 7:
	print(random.choice(Artifact_list))
elif randomran == 8:
	print(random.choice(Artifact_list))
elif randomran == 9:
	print(random.choice(Mineral_list))
elif randomran == 10:
	print(random.choice(Mineral_list))

