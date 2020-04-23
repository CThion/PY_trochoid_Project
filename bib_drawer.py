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

#=============================================================================================================================
def coods_list_spliter(screen_points):
    """ Function to take list of points and make them into lines
    """
    is_first = True
    # Set up some variables to hold x,y coods
    x0 = y0 = 0
    # Grab each pair of points from the input list
    for (x,y) in screen_points:
        # If its the first point in a set, set x0,y0 to the values
        if is_first:
            x0 = x
            y0 = y
            is_first = False
        else:
            # If its not the fist point yeild previous pair and current pair
            yield x0,y0,x,y
            # Set current x,y to start coords of next line
            x0,y0 = x,y

def test():
    list_of_screen_coods = [(50,250),(150,100),(250,250),(350,100)]
    for (x00,y00,x11,y11) in linemaker(list_of_screen_coods):
        win.canvas.create_line(x00,y00,x11,y11, width=1,fill="red")

    
#==============================================================================================================================
def hypo_trocho(t=1, points=[]):
    """draw an hypotrochoide"""
    #VARIABLES----------------------------------------
    x0, y0 = win.C_entry.state.splite(','); x0, y0 = int(x0), int(y0) #intial point
    R = win.R_entry.state
    r = win.r_entry.state
    h = win.h_entry.state
    m = R/r

    #FONCTION-----------------------------------------
    xi = (R+m*R)*cos(m*t)-h*cos(t+m*t)
    yi = -(R+m*R)*sin(m*t)+h*sin(t+m*t)
    points.append([xi, yi])
    win.canvas.create_line()
    t+=1 #time goes by...
    #--------------------------------------------------
    

    win.after(20, hypo_trocho)

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
    height, width = 720, 1080
    global win
    win = Win(title="drawer fonctions", flow='E', grow=True)
    
    #=========================(parent: win)=======================================
    win.left_band = Frame(win, width=width/4, height=height, bg='cyan', flow='S', grow=True)
    win.canvas = Canvas(win, width=width*3/4, height=height)

    #=========================(parent: left_band)=================================
    win.start = Button(win.left_band, text=('start', 'stop'), command=test())
    parameters_band = Frame(win.left_band, flow='ES', fold=2, grow=True)

    #=========================(parent: parameters_band)===========================
    #-----C
    Label(parameters_band, text='choice the C coords')
    win.C_entry = Entry(parameters_band, command=pre_disp)
    #-----R
    Label(parameters_band, text='choice the R value')
    win.R_entry = Entry(parameters_band, command=pre_disp)
    #-----r
    Label(parameters_band, text='choice the r value')
    win.r_entry = Entry(parameters_band, command=pre_disp)
    #-----h
    Label(parameters_band, text='choice the h value')
    win.h_entry = Entry(parameters_band, command=pre_disp)

    #==============================================================================
    win.loop()
    
#==============================================================================================================================
#==============================================================================================================================

if __name__ == '__main__':
  main()
    
