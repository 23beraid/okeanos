import random
Artifact_list = ["Artifact1", "Artifact2","Artifact3",
"Artifact4","Artifact5", "Artifact6","Artifact7",
"Artifact8","Artifact9", "Artifact10",]
Mineral_list = ["Mineral1","Mineral2",
"Mineral3","Mineral4","Mineral5","Mineral6",
"Mineral7","Mineral8","Mineral9","Mineral10",]
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

