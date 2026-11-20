from random import randint, choice
import apicall as ac
import json
import sys, os
import subprocess

off = False
safe = False
mid = False
role = 0


def randomize():
    choices = set()

    try:
        heroes = ac.getHeroes()
        if heroes == None:
            print("Failed to load Heroes data", file=sys.stderr)
            return
        laneData = None
        with open(ac.relative_path("laneData.json"), "r", encoding="utf-8") as f:
            laneData = json.load(f)
        if laneData == None:
            print("Failed to load Lanes data", file=sys.stderr)
            return
    except IOError as e:
        print(e)
        return

    if mid:
        choices.update(laneData.get("mid"))
    if off:
        choices.update(laneData.get("off"))
    if safe:
        choices.update(laneData.get("safe"))
    if not mid and not off and not safe:
        choices.update(laneData.get("mid"))
        choices.update(laneData.get("safe"))
        choices.update(laneData.get("off"))

    match role:
        case 1: return choice(list(choices.intersection(set(laneData.get("core")))))
        case 2: return choice(list(choices.intersection(set(laneData.get("support")))))
        case _: return choice(list(choices))


def clear():
    if ac.os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"],check=True)
    else:
        subprocess.run(["clear"],check=True)