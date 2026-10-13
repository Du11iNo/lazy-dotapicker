import requests

def getMatchups(heroID: int):
    response = requests.get("https://api.opendota.com/api/heroes/" + str(heroID) + "/matchups")
    return response.json() if response.status_code == 200 else None

def getHeroes():
    response = requests.get("https://api.opendota.com/api/heroes")
    return response.json() if response.status_code == 200 else None

def getHero(heroID: int, heroList: list):
    if heroID < 0 or heroID > len(heroList):
        return None
    return heroList[heroID]

def getHeroName(heroID: int, heroList: list):
    return heroList[heroID]["localized_name"]

def getHeroAttackType(heroID: int, heroList: list):
    return heroList[heroID]["attack_type"]

def getHeroAttr(heroID: int, heroList: list):
    return heroList[heroID]["primary_attr"]

def getIdByName(hero: str, heroList: list):
    for i in range(len(heroList)):
        if heroList[i]["localized_name"] == hero:
            return i
    return -1