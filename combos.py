def duplicates(arr1, arr2):
    a = arr1
    b = arr2
    c = []
    for x in a:
        for y in b:
            if x == y:
                c.append(x)
    c = sorted(c)
    b = sorted(b)
    if c == b:
        return True
    else:
        return False

def combineElements(user, combination):
    needed = [combination + " Rune", combination + " Scroll", combination + " Scepter", combination + " Amulet"]
    combo = combination + " Combo"
    inventory=db['inv'+str(user.id)]
    if duplicates(inventory, needed) == True:
        for x in range(0, len(needed)):
            inventory.remove(needed[x])
        inventory.append(combo)
        db['inv'+str(user.id)]=inventory
        return "Successful Combination"
    else:
        return "You don't have the right items!"

def combineItems(user, combination):
    needed = ["Air " + combination, "Earth " + combination, "Fire " + combination, "Water " + combination]
    combo = combination + " Combo"
    inventory=db['inv'+str(user.id)]
    if duplicates(inventory, needed) == True:
        for x in range(0, len(needed)):
            inventory.remove(needed[x])
        inventory.append(combo)
        db['inv'+str(user.id)]=inventory
        return "Successful Combination"
        
    else:
        return "You don't have the right items!"
