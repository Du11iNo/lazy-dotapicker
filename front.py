import tkinter as tk
from tkinter import ttk

#Base
root = tk.Tk()
root.title("Lazy Dota Picker")
root.geometry("1280x720")
root.configure(bg="#2b2b2b")
root.minsize(640, 360)
#root.aspect(10,7,10,7) - not working
root.iconbitmap("placeholder.ico")

#Grid
root.columnconfigure((0, 1, 2), weight=1, uniform="cols")
root.rowconfigure(0, weight=1)

#Left
left = tk.Frame(root, bg="#aa2424", width=300, height=625)
left.grid(row = 0, column=0, sticky="nsew", padx=(100,25), pady=(75,20))
left.grid_propagate(False)
left.columnconfigure(0, weight=1)
left.rowconfigure(1, weight=1)

search_bar = tk.StringVar()
tk.Entry(left, textvariable=search_bar, width=47).grid(row=0, column=0, sticky="ew", padx=5, pady=(20,5))

sb = tk.Scrollbar(left)
sb.grid(row=1, column=0, sticky="ens", padx=(0, 5), pady=(0, 5))

#Middle
middle = tk.Frame(root, bg="#461fb1", width=300, height=625)
middle.grid(row=0, column=1, sticky="nsew", padx=(25,25), pady=(75,20))
middle.grid_propagate(False)
middle.columnconfigure(0, weight=1)

counters = []
for r in range(1, 6):
    middle.rowconfigure(r, weight=1, uniform="counters")
    c = tk.Canvas(middle, width=1, height=1)
    c.grid(row=r, column=0, sticky="nsew", padx=10, pady=(0, 1))
    counters.append(c)

#Right
right = tk.Frame(root, bg="#1fb143", width=300, height=625)
right.grid(row=0, column=2, sticky="nsew", padx=(25,100), pady=(75,20))
right.grid_propagate(False)
right.columnconfigure(0, weight=1)
right.rowconfigure(2, weight=1)

random_image = tk.Canvas(right, width=256, height=144, bg="#a5a5a5")
random_image.grid(row=0, column=0, sticky="nsew", padx=22, pady=25)

random_button = tk.Button(right, text="Random")
random_button.grid(row=1, column=0, padx=100, pady=(20,0))

modifiers = tk.Frame(right, width=280, height=400, bg="#942424")
modifiers.grid(row=2, column=0, sticky="nsew", padx=10, pady=(50, 20))
modifiers.grid_propagate(False)

for c in range(6):
    modifiers.columnconfigure(c, weight=1, uniform="mod")
for r in range(2):
    modifiers.rowconfigure(r, weight=1, uniform="modrows")

core_button    = tk.Button(modifiers, text="Core")
core_button.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

support_button = tk.Button(modifiers, text="Support")
support_button.grid(row=0, column=3, columnspan=3, sticky="nsew", padx=5, pady=5)

safe_button    = tk.Button(modifiers, text="Safe")
safe_button.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

mid_button     = tk.Button(modifiers, text="Mid")
mid_button.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

off_button     = tk.Button(modifiers, text="Off")
off_button.grid(row=1, column=4, columnspan=2, sticky="nsew", padx=5, pady=5)

root.mainloop()