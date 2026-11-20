import sys
import subprocess
import counterPicker, randomizer
import apicall as ac

def toggleMid():
    randomizer.mid = not randomizer.mid

def toggleOff():
    randomizer.off = not randomizer.off

def toggleSafe():
    randomizer.safe = not randomizer.safe

def pickSupport():
    if randomizer.role == 2:
        randomizer.role = 0
    else:
        randomizer.role = 2

def pickCore():
    if randomizer.role == 1:
        randomizer.role = 0
    else:
        randomizer.role = 1
