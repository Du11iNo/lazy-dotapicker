import requests
from random import randint, choice, seed
import os
import apicall as ac
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


heroes = ac.getHeroes()

while True:

    seed = datetime.now()

    x = input("Write '1' for Random, '2' for Options: ").strip()

    if x == "1" :

        print(ac.getHeroName(randint(0,len(heroes)), heroes))

    
    elif x == "2":

        attackType = input("Choose an attack type (Melee/Ranged/Both): ").strip()

        if attackType != "Melee" and attackType != "Ranged" and attackType != "Both":
            continue

        role = input("Choose a role (Carry/Support/Both): ").strip()

        if role != "Carry" and role != "Support" and role != "Both":
            continue
        
        a = "1"
        while a == "1":

            if role == "Both" and attackType == "Both":
                seed = datetime.now()
                print(ac.getHeroName(randint(0,len(heroes)), heroes))
                a = input("Write '1' to repeat with current options: ").strip()

            elif role == "Both" and attackType != "Both":
                seed = datetime.now()
                print(ac.getHeroName(choice([i for i in range(0, len(heroes)) if ac.getHeroAttackType(i,heroes) == attackType]), heroes))
                a = input("Write '1' to repeat with current options: ").strip()

            elif attackType == "Both" and role != "Both":
                seed = datetime.now()
                print(ac.getHeroName(choice([i for i in range(0, len(heroes)) if role in heroes[i]["roles"]]), heroes))
                a = input("Write '1' to repeat with current options: ").strip()

            else:
                seed = datetime.now()
                print(ac.getHeroName(choice([i for i in range(0, len(heroes)) if ac.getHeroAttackType(i,heroes) == attackType and role in heroes[i]["roles"]]), heroes))
                a = input("Write '1' to repeat with current options: ").strip()
    if not x:
        continue