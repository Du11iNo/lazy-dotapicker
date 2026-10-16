from random import randint, choice
import os
import apicall as ac
from datetime import datetime
import json
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

heroes = ac.getHeroes()

if heroes == None:
    print("Failed to load Heroes data", file=sys.stderr)

laneData = None
with open("laneData.json", "r", encoding="utf-8") as f:
    laneData = json.load(f)

if laneData == None:
    print("Failed to load Lanes data", file=sys.stderr)

while True:

    x = input("Write '1' for Random, '2' for Options: ").strip()

    if x == "1" :

        print(ac.getHero(randint(0,len(heroes)), heroes)["localized_name"])
 
    elif x == "2":

        role = input("Choose a role (Carry/Support/Both): ").strip().lower()

        if role != "carry" and role != "support" and role != "both":
            continue

        lane = input("Choose a lane (Mid/Off/Safe/All): ").strip().lower()

        if lane != "mid" and lane != "off" and lane != "safe" and lane != "all":
            continue


        
        a = "1"
        while a == "1":

            if role.capitalize() == "Both":
                match lane:
                    case "safe":
                        ls = laneData.get("safe")
                    case "mid":
                        ls = laneData.get("mid")
                    case "off":
                        ls = laneData.get("off")
                    case _:
                        ls = heroes

                print(ac.getHero(choice([i for i in range(len(ls))]), heroes)["localized_name"])
                a = input("Write '1' to repeat with current options: ").strip()

            else:

                match lane:
                    case "safe":
                        ls = laneData.get("safe")  
                    case "mid":
                        ls = laneData.get("mid")
                    case "off":
                        ls = laneData.get("off")
                    case _:
                        ls = heroes

                print(ac.getHero(choice([i for i in range(len(heroes)) if role.capitalize() in heroes[i]["roles"] and ac.getHero(i,heroes)["id"] in ls]), heroes)["localized_name"])
                a = input("Write '1' to repeat with current options: ").strip()

    if not x:
        continue