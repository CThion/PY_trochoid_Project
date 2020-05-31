from ezTK import *
from math import *
import settings as st


#============================================================================================================================= 
def tick():
    """recursive fonction calling hypo_trocho"""
    if st.win.start_stop['text']=="start": return
    st.win.t +=0.1
    st.win.timer['text'] = round(st.win.t,1) #increment t
    hypo_trocho(st.win.t)
    st.win.after(100, tick)

#=================================================================================    
def hypo_trocho(t):
    """calcul a trochoide coord at time t, then add the coord to the global liste of coord, then trace the trochoide with all
    the point of this list, then remove the older line created."""
    #VARIABLES----------------------------------------
    R = int(st.win.R_entry.state) #R = radius of the fixed circle
    r = int(st.win.r_entry.state) #r = radius of the rolling circle
    h = int(st.win.h_entry.state) #h = distance from the tracing point to the centre of the rolling circle
    m = R/r                    # m=R/r is the modulus of the trochoid
    #FONCTION-----------------------------------------
      #new point coords = begin point coord + parametric fonction
    xi = int(st.win.xC_entry.state) + (R+m*R)*cos(m*t)-h*cos(t+m*t) 
    yi = int(st.win.xC_entry.state) + -(R+m*R)*sin(m*t)+h*sin(t+m*t) 
      #add next point to point_list 
    st.win.points_coords_list.append((xi, yi)) #--add the new point's coords tuple
      #create line with upadted point_coords_list
    st.win.canvas_item.append(st.win.canvas.create_line(st.win.points_coords_list, fill=st.win.troco_color_entry.state, width=st.win.troco_width_entry.state))
      #delete all the previous canvas. If not done, the program get more and more slower because have to manage with so many different lines.
    if len(st.win.canvas_item) > 1 :
          for item in st.win.canvas_item[0:len(st.win.canvas_item)-1]: st.win.canvas.delete(item)
#================================================================================
def epi_trocho(t):
    """calcul a trochoide coord at time t, then add the coord to the global liste of coord, then trace the trochoide with all
    the point of this list, then remove the older line created."""
    #VARIABLES----------------------------------------
    R = int(st.win.R_entry.state) #R = radius of the fixed circle
    r = int(st.win.r_entry.state) #r = radius of the rolling circle
    h = int(st.win.h_entry.state) #h = distance from the tracing point to the centre of the rolling circle
    m = R/r                    # m=R/r is the modulus of the trochoid

    #FONCTION-----------------------------------------
      #new point coords = begin point coord + parametric fonction
    xi = int(st.win.xC_entry.state) + (R-m*R)*cos(m*t)+h*cos(t-m*t) 
    yi = int(st.win.yC_entry.state) + -(R-m*R)*sin(m*t)+h*sin(t-m*t) 
      #  add nex point to point_list 
    st.win.points_coords_list.append((xi, yi))
      #  create line with upadted point_coords_list
    st.win.canvas_item.append(st.win.canvas.create_line(st.win.points_coords_list))
    #--------------------------------------------------
    
#================================================================================
def on_start():
      """callback function for the 'START/STOP' button"""
        # switch button (state <--> 1-stat)
      st.win.start_stop.state = 1 - st.win.start_stop.state 
        # if st.win.button.state == 1: tick() # start 'tick' when button state is 1
      if st.win.start_stop.state == 1: 
            # start the recusive 
            tick()

#=================================================================================          
def on_reset(): #exeption
    """
    callback fonction for the 'reset' button. exeption define the number of lines in st.win.canvas_item that wont be suppressed (from the 
    last created. If execption = 0, st.win.cavas_item is fully cleared. 
    """
      #  supress all created canvas_line except the last ones 
    for item in st.win.canvas_item: st.win.canvas.delete(item)
      #  actualise the liste of canvas lines
    st.win.canvas_item = []
      #  supress all created points and initialised with start point coords.
    st.win.points_coords_list = [(int(st.win.xC_entry.state), int(st.win.yC_entry.state))]
      #  reinitialise time
    st.win.t = 0

#===================================================================================

def pre_disp():
    """calback fontion for every parameting widgets (scale, entry...) which makes the display of parametings choosen by the user in real time,
    before he started to play."""
    return

#===================================================================================
    
