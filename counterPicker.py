import apicall as ac
import json
import subprocess

heroes = ac.getHeroes()

while True:
    hero = input("Counters for (exit with q): ")
    if hero == "q":
        exit()

    if ac.os.name == "nt":
        subprocess.run(["cls"],check=True)
    else:
        subprocess.run(["clear"],check=True)

    id = ac.getIdByName(hero, heroes)
    if id == -1:
        print(f"Failed to find hero: {hero}")
        continue
    stats = ac.getStratzJson(id)
    top = stats["data"]["heroStats"]["heroVsHeroMatchup"]["disadvantage"][0]["vs"][:5]

    for i in range(len(top)):
        row = top[i]
        print(f"    {ac.getHeroById(row["heroId2"], heroes)["localized_name"]}: {row["synergy"]}")