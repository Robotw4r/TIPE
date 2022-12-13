from stockfish import Stockfish
from tkinter import *

stockfish = Stockfish(path="/usr/games/stockfish")

autoMode = True

def updateBoard():
    move = [stockfish.get_best_move()]
    stockfish.make_moves_from_current_position(move)
    return stockfish.get_board_visual()
'''
def updateManual():
    playermove = [pièce]
    stockfish.make_moves_from_current_position(playermove)
    move = [stockfish.get_best_move()]
    stockfish.make_moves_from_current_position(move)
    return stockfish.get_board_visual()
'''

def nextTurn():
    if autoMode == True:
        my_label.config(text = updateBoard())
    #else:
    #    my_label.config(text = updateManual())

Main_window = Tk()

my_label = Label(Main_window,
                 text=stockfish.get_board_visual())

my_button = Button(Main_window,
                   text="Next turn",
                   command=nextTurn)

#boutonMode = Button(Main_window,text="Change Mode (Auto / Manual)", command = print("LOL") )

#pièce = Entry(Main_window)

my_label.pack()
my_button.pack()
#boutonMode.pack()
#pièce.pack()

Main_window.mainloop()