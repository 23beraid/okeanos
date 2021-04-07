# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:03:26 2021

@author: 23dhisne
"""

"""
Items: Artifacts: (80%) Air Scepter Earth Scepter Fire Scepter Water Scepter Air Amulet Earth Amulet Fire Amulet Water Amulet Air Scroll Earth Scroll Fire Scroll Water Scroll Air Rune Earth Rune Fire Rune Water Rune Minerals: (20%) Ruby Emerald Aquamarine Topaz Diamond Amythyst Tools: Adventurer's Crown allows solo adventuring Warrior's Helm allows combat Miner's Pick allows mining Alchemist's Beaker allows Alchemy Mage's Robe makes one invincible to stealing Currency: Copper Silver (worth two copper) Gold (worth three copper)
"""

#variables
artifacts = ["Air Scepter", "Earth Scepter", "Fire Scepter", "Water Scepter", "Air Amulet", "Earth Amulet", "Fire Amulet", "Water Amulet", "Air Scroll", "Earth Scroll", "Fire Scroll", "Water Scroll", "Air Rune", "Earth Rune", "Fire Rune", "Water Rune"]
minerals = ["Ruby", "Emerald", "Aquamarine", "Topaz", "Diamond", "Amethyst"]
tools = ["Adventurer's Crown", "Warrior's Helm", "Miner's Pick", "Alchemist's Beaker", "Mage's Robe"]
mPrices = {}

def buy_item():
    print("Work in progress")
    #create purchase function
    
def in_sell_item():
    #i = input("Which item would you like to sell? Type here: ")
    if i.lower()=="exit":
        pass
    else:
        sell_item(i)
    
def sell_item(i):
    if (" " in i):
        first = True
        i2 = i.split()
        i = ""
        for j in i2:
            if first==False:
                i += " "
            else:
                first = False
            i += j.capitalize()
    else:
        i = i.capitalize()
    if i not in artifacts and i not in minerals and i not in tools:
        print("Not a valid artifact. Try again.")
        in_sell_item()
    else:
        enter_price(i,j)
    #exchange currency
    
def in_enter_price():
    #j = input("Enter the price you would like to put it on the market as, in units of copper: ")
    
def enter_price(i,j):
    #db("?") = len(mPrices[i])
    if j.isdigit():
        if i in mPrices:
            mPrices[i].append(int(j))
        else:
            mPrices[i] = [int(j)]
        print("Your item, " + i + ", has been put on the market at the price of " + j + " copper! It is now waiting to be ordered.")
    else:
        print("Not a valid price. Try again.")
        enter_price(i,j)
    
def display_items():
    txt = ""
    if mPrices != {}:
        for i in mPrices:
            for j in range(0,len(mPrices[i])):
                txt += i + ": "
                txt += str(mPrices[i][j]) + " copper\n"
    else:
        txt = "Unfortunately, the inventory is empty. Check for notifications when more items are added!"
    print(txt)
    
def main_screen():
    a = input("This is the marketplace main screen.\n\nTo see items and prices, type 'inventory'. To purchase an item from the market, type 'buy'. To trade an item to the market, type 'sell'. To leave the market, type 'exit'. Also, to cancel any command at any time, type 'cancel'.\n\nType here: ")
    if a.lower()=="inventory":
        display_items()
        main_screen()
    elif a.lower()=="buy":
        buy_item()
        main_screen()
    elif a.lower()=="sell":
        sell_item()
        main_screen()
    elif a.lower()=="exit":
        pass
    else:
        print("Not a valid command. Try again.")
        main_screen()

def go():
    main_screen()
    
go()
