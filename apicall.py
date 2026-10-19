import requests
from dotenv import load_dotenv
import os
import sys

if load_dotenv() == False:
    inp = input("No .env file found. Paste the api key from stratz.com/api here: ")
    try:
        with open(".env", "w") as f:
            f.write(f"API_KEY={inp}")
    except IOError:
        print("Failed to create file.\nTo fix this issue, create a .env file inside the working directory and write inside:\nAPI_KEY=[your-api-key]", file=sys.stderr)
        exit(1)

apiKey = os.getenv("API_KEY")
if apiKey == None:
    print("Failed to get API Key. Exiting...", file=sys.stderr)
    exit(1)

query = """
    query ($heroId: Short!){
        heroStats {
            heroVsHeroMatchup (heroId: $heroId) {
                disadvantage {
                    heroId
                    vs {
                        heroId2
                        synergy
                    }
                }
            }
        }
    }
"""

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

def getIdByName(hero: str, heroList: list):
    for i in range(len(heroList)):
        if heroList[i]["localized_name"].replace("-", "").replace(" ", "").lower() == hero.replace("-", "").replace(" ", "").lower():
            return heroList[i]["id"]
    return -1

def getStratzJson(heroId: int):
    variables = {"heroId": heroId}
    response = requests.post("https://api.stratz.com/graphql",
                             headers={"Authorization": f"Bearer {apiKey}", "Content-Type": "application/json", "User-Agent": "STRATZ_API"},
                             json={"query": query, "variables": variables})
    if response.status_code != 200:
        print("Failed to fetch data from api. Check stratz.com API Status.", file=sys.stderr)
        exit(1)    
    return response.json()