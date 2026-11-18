# LazyDotaPicker
A lazy, simple, Dota 2 hero picker and counter with a bonus randomized hero selector.

## Use
#### CMD Version
For counter-pick mode, write a hero's name, and counters from Stratz.com will be printed. An API Key, found on Stratz, will be asked each time the program is run. For a more permanent method, create a *.env* file and write: <br>
`API_KEY=<key>`
Save this file inside the same folder the executable file is. 

For randomizer mode, either randomize with default options or modify the options to your need

#### GUI Version
Currently in progress

---

## Build it yourself
Download the files, put them in the same folder and use PyInstaller to create a single executable using the command: <br>
`python -m PyInstaller --onefile --name LazyDotaPicker --clean --add-data "laneData.json;." dotapicker.py` <br>
For the CMD Version