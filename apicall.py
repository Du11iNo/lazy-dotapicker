import requests

def getMatchups(heroID: int):
    response = requests.get(f"https://api.opendota.com/api/heroes/{heroID}/matchups")
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

def getStats():
    response = requests.get("https://api.opendota.com/api/heroStats")
    return response.json() if response.status_code == 200 else None

def getHeroStats(heroID: int, stats: list):
    for i in range(len(stats)):
        if stats[i]["id"] == heroID:
            return stats[i]

def getHeroWR(heroID: int, stats: list):
    hero = getHeroStats(heroID, stats)
    return (hero["5_win"]/hero["5_pick"] + hero["6_win"]/hero["6_pick"] + hero["7_win"]/hero["7_pick"]) / 3


def getIdByName(hero: str, heroList: list):
    for i in range(len(heroList)):
        if heroList[i]["localized_name"] == hero:
            return heroList[i]["id"]
    return -1

def getLaneRoles():
    response = requests.get("https://api.opendota.com/api/scenarios/laneRoles")
    return response.json() if response.status_code == 200 else None 