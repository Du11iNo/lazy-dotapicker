import requests
from random import randint, choice
import os
import apicall as ac

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

heroes = ac.getHeroes()

while True:

    x = input("Write '1' for Random, '2' for Options: ").strip()

    if x == "1" :

        print(ac.getHeroName(randint(0,len(heroes))))

        input("Press any button to repeat: ").strip()
    
    elif x == "2":

        attackType = input("Choose an attack type (Melee/Ranged): ").strip()

        if attackType != "Melee" and attackType != "Ranged":
            continue

        role = input("Choose a role (Carry/Support): ").strip()

        if role != "Carry" and role != "Support":
            continue
        
        #print(heroes[choice([i for i in range(0, len(heroes)) if heroes[i]["attack_type"] == attackType and  role in heroes[i]["roles"]])]["localized_name"])
        print(ac.getHeroName(choice([i for i in range(0, len(heroes)) if ac.getHeroAttackType(i) == attackType and role in heroes[i]["roles"]])))

        input("Press any button to repeat: ").strip()
    
    if not x:
        continue