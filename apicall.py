import requests

def getMatchups(heroID: int):
    response = requests.get("https://api.opendota.com/api/heroes/" + str(heroID) + "/matchups")
    return response.json() if response.status_code == 200 else None

def getHeroes():
    response = requests.get("https://api.opendota.com/api/heroes")
    return response.json() if response.status_code == 200 else None

def getHeroById(heroID: int, heroList: list):
    for i in range(len(heroList)):
        if heroList[i]["id"] == heroID:
            return heroList[i]
    return None

def getHero(Idx: int, heroList: list):
    return heroList[Idx] if Idx >= 0 and Idx < len(heroList) else None

def getHeroAttr(heroID: int, heroList: list):
    return getHeroById(heroID, heroList)["primary_attr"]

def getIdByName(hero: str, heroList: list):
    for i in range(len(heroList)):
        if heroList[i]["localized_name"] == hero:
            return i
    return -1

def getLaneRoles():
    response = requests.get("https://api.opendota.com/api/scenarios/laneRoles")
    return response.json() if response.status_code == 200 else None 