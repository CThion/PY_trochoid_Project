from ezTK import *
from math import *
import settings as st


#============================================================================================================================= 
def tick():
    """recursive fonction calling hypo_trocho. Contrôle the speed of the drawing."""
    if st.start_stop['text']=="start": return
    st.t +=0.1  #increment time
    st.timer['text'] = round(st.t,1) #update t display in label
    hypo_trocho(st.t) #call the main drawing fonction with next time value
    st.win.after(st.troco_speed.state, tick) #speed of the drawing determined by st.troco_speed

#=================================================================================    
def hypo_cord_calculator(t):
  """calcul a trochoide coord at time t, then add the coord to the global liste of coord, then trace the trochoide with all
  the point of this list, then remove the older line created."""
  #VARIABLES----------------------------------------
  R = st.hypo_dic["R"] #R = radius of the fixed circle
  r = st.hypo_dic["r"] #r = radius of the rolling circle
  h = st.hypo_dic["h"] #h = distance from the tracing point to the centre of the rolling circle
  m = R/r                    # m=R/r is the modulus of the trochoid
  #FONCTION-----------------------------------------
    #new point coords = begin point coord + parametric fonction
  xi = st.hypo_dic["xC"] + (R+m*R)*cos(m*t)-h*cos(t+m*t) 
  yi = st.hypo_dic["yC"] + -(R+m*R)*sin(m*t)+h*sin(t+m*t) 
  return (xi, yi)

def hypo_trocho(t):
    #add next point to point_list 
  st.points_coords_list[0] = hypo_cord_calculator(0)  #first point of the trocho, initialised by 0 in settings
  st.points_coords_list.append(hypo_cord_calculator(t)) #--add the new point's coords tuple
    #create line with upadted point_coords_list     st.troco_color_entry.state    st.troco_width_entry.state
  st.canvas_item.append(st.canvas.create_line(st.points_coords_list, fill="red", width=5))
    #delete all the previous canvas_line.  
  if len(st.canvas_item) > 1 : #if there is only one canvas_line, do not delete it.
    for item in st.canvas_item[0:len(st.canvas_item)-1]: st.canvas.delete(item)

#================================================================================
def epi_trocho(t):
    """calcul a trochoide coord at time t, then add the coord to the global liste of coord, then trace the trochoide with all
    the point of this list, then remove the older line created."""
    #VARIABLES----------------------------------------
    R = int(st.R_entry.state) #R = radius of the fixed circle
    r = int(st.r_entry.state) #r = radius of the rolling circle
    h = int(st.h_entry.state) #h = distance from the tracing point to the centre of the rolling circle
    m = R/r                    # m=R/r is the modulus of the trochoid

    #FONCTION-----------------------------------------
      #new point coords = begin point coord + parametric fonction
    xi = int(st.xC_entry.state) + (R-m*R)*cos(m*t)+h*cos(t-m*t) 
    yi = int(st.yC_entry.state) + -(R-m*R)*sin(m*t)+h*sin(t-m*t) 
      #  add nex point to point_list 
    st.points_coords_list.append((xi, yi))
      #  create line with upadted point_coords_list
    st.canvas_item.append(st.canvas.create_line(st.points_coords_list))
    #--------------------------------------------------
    
#================================================================================
def on_start():
      """callback function for the 'START/STOP' button"""
        # switch button (state <--> 1-stat)
      st.start_stop.state = 1 - st.start_stop.state 
        # if st.button.state == 1: tick() # start 'tick' when button state is 1
      if st.start_stop.state == 1: 
            # start the recusive 
            tick()

#=================================================================================          
def on_reset(): #exeption
    """
    callback fonction for the 'reset' button. exeption define the number of lines in st.canvas_item that wont be suppressed (from the 
    last created. If execption = 0, st.cavas_item is fully cleared. 
    """
      #  supress all created canvas_line except the last ones 
    for item in st.canvas_item: st.canvas.delete(item)
      #  actualise the liste of canvas lines
    st.canvas_item = []
      #  supress all created points and initialised with start point coords.
    st.points_coords_list = [(int(st.xC_entry.state), int(st.yC_entry.state))]
      #  reinitialise time
    st.t = 0

#===================================================================================

def pre_disp():
    """calback fontion for every parameting widgets (scale, entry...) which makes the display of parametings choosen by the user in real time,
    before he started to play."""
    return

#===================================================================================
    
