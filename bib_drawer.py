from ezTK import *
from math import *
#============================================================================================================================= 
#####epitro
#x=(R+mR)cosmt−hcos(t+mt),
#y=(R+mR)sinmt−hsin(t+mt)

#=============================================================================================================================
def test():
      
    #list_of_screen_coods = [(50,250),(150,100),(250,250),(350,100),(450,250),(550,100)]
    print(
        'win.canvas_item = ', win.canvas_item,
        'win.points_coords_list = ', win.points_coords_list,
        sep='\n',end='\n\n'
        )
    #win.TEST['state']='disabled'

#=============================================================================================================================
def epi_trocho(t):
    """calcul a trochoide coord at time t, then add the coord to the global liste of coord, then trace the trochoide with all
    the point of this list, then remove the older line created."""
    #VARIABLES----------------------------------------
    xC, yC = int(win.xC_entry.state), int(win.yC_entry.state) #coord of begin point 
    R = int(win.R_entry.state) #R = radius of the fixed circle
    r = int(win.r_entry.state) #r = radius of the rolling circle
    h = int(win.h_entry.state) #h = distance from the tracing point to the centre of the rolling circle
    m = R/r                    # m=R/r is the modulus of the trochoid

    #FONCTION-----------------------------------------
      #new point coords = begin point coord + parametric fonction
    xi = int(win.xC_entry.state) + (R-m*R)*cos(m*t)+h*cos(t-m*t) 
    yi = int(win.yC_entry.state) + -(R-m*R)*sin(m*t)+h*sin(t-m*t) 
      #add nex point to point_list and create line with it
    win.points_coords_list.append((xi, yi))
    win.canvas_item.append(win.canvas.create_line(win.points_coords_list))
    #--------------------------------------------------

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
    xi = int(win.xC_entry.state) + (R+m*R)*cos(m*t)-h*cos(t+m*t) # x center coord + parametric fonction
    yi = int(win.xC_entry.state) + -(R+m*R)*sin(m*t)+h*sin(t+m*t) 

    #print("win.points_coords_list =", len(win.points_coords_list), "win.canvas_item =", len(win.canvas_item))
    win.points_coords_list.append((xi, yi)) #--add the new point's coords
    #win.canvas.create_line(win.canvas_item[-1].coord, )
    
    
    for (x0,y0,x1,y1) in coords_list_spliter(win.points_coords_list):
        win.canvas_item.append(win.canvas.create_line(x0,y0,x1,y1, width=1, fill="red"))
    if len(win.points_coords_list)>1:
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
        # switch button (state <--> 1-stat)
      win.start.state = 1 - win.start.state 
        # if win.button.state == 1: tick() # start 'tick' when button state is 1
      if win.start.state == 1: 
            # start the recusive 
          tick()

#==============================================================================================================================
def on_reset():
    """callback fonction for the 'reset' button"""
    for item in win.canvas_item: win.canvas.delete(item)
    for coord in win.points_coords_list: del coord
      # initialise points_coords_list with begin point coords.
    win.points_coords_list.append((int(win.xC_entry.state), int(win.yC_entry.state)))
    
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

    #-------------------------(global variables)----------------------------------
    win.canvas_item = [] #  list of points used to draw the trochoide curve.
    win.points_coords_list = [] #  containers for all created canvas item
    win.t = 0 #global time used in parametrics equations

   #===========================(canvas)============================================
    win.canvas = Canvas(win, width=width*3/4, height=height)
    test_frame = Frame(win, bg="yellow", grow=True)
    win.TEST = Button(test_frame, text="TEST", width=10, height=10, grow=True, command=test)
    win.canvas.create_window(400, 50, window=test_frame)

    #=========================(left_band)=========================================
    win.left_band = Frame(win, width=width/4, height=height, bg='cyan', flow='N', grow=True)
    #------------(parameters_band)------------------------------------------------
    parameters_band = Frame(win.left_band, flow='ES', fold=2, grow=True)
    #-----xC
    Label(parameters_band, text='choice the x C coords')
    win.xC_entry = Entry(parameters_band, command=pre_disp)
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
    #------------(start & reset & timer)-----------------------------------------------
    win.start = Button(win.left_band, text=('start', 'stop'), grow=True, command=on_start)
    win.reset = Button(win.left_band, text='reset', grow=True, command=lambda:on_reset()) #read when program lauched ==> initialise win.point_coord_list
    win.timer = Label(win.left_band, text=0, border=1, grow=True)
 
    win.loop()
    
#==============================================================================================================================
#==============================================================================================================================

if __name__ == '__main__':
  main()
    
