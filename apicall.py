import requests

def getMatchups(heroID: int):
    response = requests.get("https://api.opendota.com/api/heroes/" + str(heroID) + "/matchups")
    return response.json() if response.status_code == 200 else None

def getHeroes():
    response = requests.get("https://api.opendota.com/api/heroes")
    return response.json() if response.status_code == 200 else None

def getHero(heroID: int):
    heroList = getHeroes()
    if heroID < 0 or heroID > len(heroList):
        return None
    return getHeroes[heroID]

def getHeroName(heroID: int):
    return getHero(heroID)["localized_name"]

def getHeroAttackType(heroID: int):
    return getHero(heroID)["attack_type"]

def getHeroAttr(heroID: int):
    return getHero(heroID)["primary_attr"]

def getIdByName(hero: str):
    heroList = getHeroes()
    for i in range(len(heroList)):
        if heroList[i]["localized_name"] == hero:
            return i
    return -1