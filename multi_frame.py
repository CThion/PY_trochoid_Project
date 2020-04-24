# ==============================================================================
"""MULTI_FRAME : demo program for window manipulations"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # dynamic creation and destruction of frames
__date__    = "2020-04-22"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def make_brick():
  """create the brick configuration in the bottom frame"""
  del win[1] # delete the current bottom frame
  Brick(win, width=400, height=200, bg='blue')
# ------------------------------------------------------------------------------
def make_grid():
  """create the grid configuration in the bottom frame"""
  del win[1] # delete the current bottom frame
  grid = Frame(win, fold=10) # create a new frame to store the grid
  colors = ('#F00','#0F0','#00F','#0FF','#F0F','#FF0')
  for loop in range(100): # create a 10x10 grid of Brick
    Brick(grid, height=32, width=32, bg=colors, state=loop)
# ------------------------------------------------------------------------------
def make_scales():
  """create the scales configuration in the bottom frame"""
  del win[1] # delete the current bottom frame
  frame = Frame(win, fold=2) # create a new frame to store the scales
  for char in 'ABCDEF': # loop over chars to create specific Label/Scale pairs
    Label(frame, text=f"Value of {char} :", width=10, anchor='SW', grow=False)
    Scale(frame, scale=(0,99))
# ------------------------------------------------------------------------------
def main(rows=9, cols=9):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='MULTI-FRAME', op=2)
  top = Frame(win) # create top frame to store the 3 Buttons
  Button(top, text='BRICK', width=8, command=make_brick)
  Button(top, text='GRID', width=8, command=make_grid)
  Button(top, text='SCALES', width=8, command=make_scales)
  Frame(win, width=400) # create bottom frame to store the chosen configuration
  win.loop()
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
