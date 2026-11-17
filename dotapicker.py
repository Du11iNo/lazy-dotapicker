import sys
import subprocess
import counterPicker, randomizer
import apicall as ac


while True:
    choice = input("Pick either Randomizer or Counter Picker (\"r\" or \"c\", \"q\" to exit): ")

    match choice.lower():
        case "r":
            randomizer.randomize()
        case "c":
            counterPicker.counterPick()
        case "q":
            break
        case _:
            if ac.os.name == "nt":
                subprocess.run(["cmd", "/c", "cls"],check=True)
            else:
                subprocess.run(["clear"],check=True)
            print("Wrong input")