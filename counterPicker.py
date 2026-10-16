import apicall as ac
import sys
from math import sqrt

def wilsonScore(p: float, n: int):
    z = 1.282
    return (p + (z*z)/(2*n) - z * sqrt((p*(1-p)/n) + ((z*z)/(4*n*n)))) / (1 + z*z/n)

heroes = ac.getHeroes()

if heroes == None:
    print("Failed to load Heroes data", file=sys.stderr)
    exit()

while True:
    inp = input("Write who's counter you want: ")
    if inp == "q":
        exit()
    matchups = ac.getMatchups(ac.getIdByName(inp, heroes))
    if matchups == None:
        print("Failed to load matchups")
        continue

    scores = {}
    stats = ac.getStats()
    for i in range(len(matchups)):
        heroName = ac.getHeroById(matchups[i]["hero_id"], heroes)["localized_name"]
        sampleSize = matchups[i]["games_played"]
        sampleProp = (sampleSize - matchups[i]["wins"]) / sampleSize if sampleSize != 0 else None
        if sampleProp != None:
            scores[heroName] = wilsonScore(sampleProp, sampleSize) - ac.getHeroWR(matchups[i]["hero_id"], stats)
        else:
            continue
    scores = sorted(scores, key=scores.get)
    final = list(scores[-5:])
    final.reverse()
    for i in range(len(final)):
        print(final[i])