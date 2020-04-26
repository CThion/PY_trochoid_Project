from ezTK import *
from math import *
#============================================================================================================================= 
#####epitro
#x=(R+mR)cosmt−hcos(t+mt),
#y=(R+mR)sinmt−hsin(t+mt)

def test2():
    return
    #return k for k in range(2,5)

def test():
    list_of_screen_coods = [(50,250),(150,100),(250,250),(350,100),(450,250),(550,100)]
    for (x00,y00,x11,y11) in coords_list_spliter(list_of_screen_coods):
        win.canvas.create_line(x00,y00,x11,y11, width=1,fill="red")


#=============================================================================================================================
def coords_list_spliter(screen_points): #https://stackoverflow.com/questions/16494896/create-a-line-using-a-list-of-coordinates-in-python-gui
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

#==============================================================================================================================
def hypo_trocho(t):
    """calcul a trochoide coord at time t, then add the coord to the global liste of coord, then trace the trochoide with all
    the point of this list, then remove the older line created."""
    #VARIABLES----------------------------------------
    R = int(win.R_entry.state) #R = radius of the fixed circle
    r = int(win.r_entry.state) #r = radius of the rolling circle
    h = int(win.h_entry.state) #h = distance from the tracing point to the centre of the rolling circle
    m = R/r                    # m=R/r is the modulus of the trochoid

    #FONCTION-----------------------------------------
    xi = int(win.xC_entry.state) + (R+m*R)*cos(m*t)-h*cos(t+m*t)
    yi = int(win.xC_entry.state) + -(R+m*R)*sin(m*t)+h*sin(t+m*t)
    #print(len(win.trocho_points_list))
    print("win.trocho_point_list =", len(win.trocho_points_list), "win.canvas_item =", len(win.canvas_item))
    win.trocho_points_list.append((xi, yi)) #--add the new point's coords
    for (x0,y0,x1,y1) in coords_list_spliter(win.trocho_points_list):
        win.canvas_item.append(win.canvas.create_line(x0,y0,x1,y1, width=1, fill="red"))
    if len(win.trocho_points_list)>1:
        del win.canvas_item[0]
    #--------------------------------------------------

#==============================================================================================================================
def tick():
    """recursive fonction calling hypo_trocho"""
    if win.start['text']=="start": return
    win.t +=0.1
    win.timer['text'] = win.t #increment t
    hypo_trocho(win.t)
    win.after(100, tick)

#==============================================================================================================================
def on_start():
      """callback function for the 'START/STOP' button"""
      win.start.state = 1 - win.start.state # switch button (state <--> 1-stat
      #if win.button.state == 1: tick() # start 'tick' when button state is 1
      if win.start.state == 1: tick()

    
#==============================================================================================================================
def pre_disp():
    """calback fontion for every parameting widgets (scale, entry...)"""
    return

#==============================================================================================================================
def main():
    """programm tot test canvas widget"""
    #=========VARIABLES=========
    global win
    height, width = 720, 1080
    
    win = Win(title="drawer fonctions", flow='E', grow=True)
    #=========================(parent: win)=======================================
    win.left_band = Frame(win, width=width/4, height=height, bg='cyan', flow='S', grow=True)
    win.canvas = Canvas(win, width=width*3/4, height=height)

    #=========================(parent: left_band)=================================
    win.start = Button(win.left_band, text=('start', 'stop'), command=on_start)
    win.timer = Label(win.left_band, text=0, border=1)
    parameters_band = Frame(win.left_band, flow='ES', fold=2, grow=True)

    #=========================(parent: parameters_band)===========================
    #-----
    Button(parameters_band, command=test)
    #-----xC
    Label(parameters_band, text='choice the x C coords')
    win.xC_entry = Entry(parameters_band, command=test2)
    win.xC_entry.insert(0, 200) #add a default value 100
    #-----yC
    Label(parameters_band, text='choice the y C coords')
    win.yC_entry = Entry(parameters_band, command=pre_disp)
    win.yC_entry.insert(0, 200)
    #-----R
    Label(parameters_band, text='choice the R value')
    win.R_entry = Entry(parameters_band, command=pre_disp)
    win.R_entry.insert(0,30)
    #-----r
    Label(parameters_band, text='choice the r value')
    win.r_entry = Entry(parameters_band, command=pre_disp)
    win.r_entry.insert(0,30)
    #-----h
    Label(parameters_band, text='choice the h value')
    win.h_entry = Entry(parameters_band, command=pre_disp)
    win.h_entry.insert(0,20)

    #--liste of points used to draw the trochoide curve. Initialised with the starting point choosen by user.
    win.canvas_item = []
    win.trocho_points_list = [] 
    win.t = 0

    #==============================================================================
    win.loop()
    
#==============================================================================================================================
#==============================================================================================================================

if __name__ == '__main__':
  main()
    
