from ezTK import *
from math import *
#=============================================================================================================================
# r is the radius of the rolling circle, <CONSTANT
# R is the radius of the fixed circle, <CONSTANT
# m=R/r is the modulus of the trochoid,  <CONSTANT
# h is the distance from the tracing point to the centre of the rolling circle <CONSTANT
# 
#####epitro
#x=(R+mR)cosmt−hcos(t+mt),
#y=(R+mR)sinmt−hsin(t+mt)
#==============================================================================================================================
def hypo_trocho():
    """draw an hypotrochoide"""
    R = win.R_entry.state
    win.canvas.create_oval(50,50,100,R)


#==============================================================================================================================
def on_start():
      """callback function for the 'START/STOP' button"""
      win.start.state = 1 - win.start.state # switch button (state <--> 1-stat
      #if win.button.state == 1: tick() # start 'tick' when button state is 1
      if win.start.state == 1: hypo_trocho()
    

def pre_disp():
    """calback fontion for every parameting widgets (scale, entry...)"""



#==============================================================================================================================
def main():
    """programm tot test canvas widget"""
    height, width = 1000, 1300
    global win
    win = Win(title="drawer fonctions", flow='E', grow=True)
    
    #=========================(parent: win)=======================================
    win.left_band = Frame(win, width=width/4, height=height, flow='S', grow=True)
    win.canvas = Canvas(win, width=width*3/4, height=height)

    #=========================(parent: left_band)=================================
    win.start = Button(win.left_band, text=('start', 'stop'), command=on_start)
    parameters_band = Frame(win.left_band, flow='ES', fold=2, grow=True)

    #=========================(parent: parameters_band)===========================
    Label(parameters_band, text='choice the R value')
    win.R_entry = Entry(parameters_band, commande=pre_disp)
    #-----
    Label(parameters_band, text='choice the r value')
    win.r_entry = Entry(parameters_band, commande=pre_disp)
    #-----
    Label(parameters_band, text='choice the h value')
    win.h_entry = Entry(parameters_band, commande=pre_disp)
    #-----


    #==============================================================================
    win.loop()
    
#==============================================================================================================================
#==============================================================================================================================

if __name__ == '__main__':
  main()
    
