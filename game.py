import tkinter as tk
from random import randint

game = tk.Tk()
game.title("game")
game.geometry("600x600")

money = 0
moneyget = 1
cost = 10
showcurrency = tk.Label(game, text=f"Money: {money}"); showcurrency.pack()
def click():
    global money, moneyget
    money += moneyget
    showcurrency.config(text=f"Money: {money}")
showcost = tk.Label(game, text=f"{cost}$"); showcost.pack(side="right")
clickbutton = tk.Button(game, text="Click", command=click, width=12, height=4).pack(side="bottom")
def upgrade():
    global money, moneyget, cost
    if money >= cost:
        money -= cost
        showcurrency.config(text=f"Money: {money}")
        moneyget += 1
        cost *= randint(2, 3)
        showcost.config(text=f"{cost}$")
    else:
        pass
upgradebutton = tk.Button(game, text="Buy upgrade",command=upgrade).pack(side="right")

game.mainloop()