from random import randint, choice
import apicall as ac
import json
import sys, os
import subprocess


def randomize():
    try:
        heroes = ac.getHeroes()
        if heroes == None:
            print("Failed to load Heroes data", file=sys.stderr)
            return
        laneData = None
        with open(ac.relative_path("laneData.json"), "r", encoding="utf-8") as f:
            laneData = json.load(f)
        if laneData == None:
            print("Failed to load Lanes data", file=sys.stderr)
            return

        while True:

            x = input("Write '1' for Random, '2' for Options (q to exit): ").strip()

            clear()

            if x == "q":
                return

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

                        result = ac.getHero(choice([i for i in range(len(ls))]), heroes)["localized_name"]

                        clear()
                        if result == None:
                            print("No hero found...", file=sys.stderr)
                        else:
                            print(result)

                        a = input("Write '1' to repeat with current options (q to exit): ").strip()

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

                        result = ac.getHero(choice([i for i in range(len(heroes)) if role.capitalize() in heroes[i]["roles"] and ac.getHero(i,heroes)["id"] in ls]), heroes)["localized_name"]

                        clear()
                        if result == None:
                            print("No hero found...")
                        else:
                            print(result)

                        a = input("Write '1' to repeat with current options (q to exit): ").strip()

            if not x:
                continue
    except Exception as e:
        print(e)
    finally:
        os.system('pause')

def clear():
    if ac.os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"],check=True)
    else:
        subprocess.run(["clear"],check=True)