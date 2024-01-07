from tkinter import *

win=Tk()

WIDTH=int(win.winfo_screenwidth()*0.5)
HEIGHT=int(win.winfo_screenheight()*0.85)




COLUMNS=5
ROWS=5

BUTTON_X=7.5/COLUMNS
BUTTON_Y=4/ROWS

FONTSIZE=(COLUMNS+ROWS)

FONT="Ubuntu"

MINE_COUNT=int((COLUMNS*ROWS)/5)

TOTAL_CELLS=ROWS*COLUMNS-MINE_COUNT

INSTRUCTIONS="Hint: you can right-click on a cell to mark it as a suspected mine "


def get_bg(object):
    return object.cget('bg')

def get_width(obj):
    return obj.cget('width')