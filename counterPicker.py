import apicall as ac
import subprocess

def counterPick():
    heroes = ac.getHeroes()

    while True:
        hero = input("Counters for (exit with q): ")
        if hero == "q":
            return

        if ac.os.name == "nt":
            subprocess.run(["cmd", "/c", "cls"],check=True)
        else:
            subprocess.run(["clear"],check=True)

        id = ac.getIdByName(hero, heroes)
        if id == -1:
            print(f"Failed to find hero: {hero}")
            continue
        stats = ac.getStratzJson(id)

        try:
            top = stats["data"]["heroStats"]["heroVsHeroMatchup"]["disadvantage"][0]["vs"][:5]
        except IndexError as e:
            print("Currently there is not enough data for the Counter Picker. Wait some time until enough data has been gathered.\nThis usually happens when an update has been released on Dota 2")
            return
        
        for i in range(len(top)):
            row = top[i]
            print(f"    {ac.getHeroById(row["heroId2"], heroes)["localized_name"]}: {row["synergy"]}")