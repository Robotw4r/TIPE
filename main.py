from stockfish import Stockfish
from tkinter import *
import time

stockfish = Stockfish(path="/usr/games/stockfish")

def updateBoard():
    move = [stockfish.get_best_move()]
    stockfish.make_moves_from_current_position(move)
    return stockfish.get_board_visual()

def nextTurn():
    my_label.config(text = updateBoard())

Main_window = Tk()

my_label = Label(Main_window,
                 text=stockfish.get_board_visual())

my_button = Button(Main_window,
                   text="Next turn",
                   command=nextTurn)


my_label.pack()
my_button.pack()

Main_window.mainloop()