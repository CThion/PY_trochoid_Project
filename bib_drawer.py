from ezTK import *
from math import *
import settings as st
import trocho_game as tg


#============================================================================================================================= 
def tick():
    """DOCSTRING
    """
    if st.start_stop['text']=="start": return
    st.t +=0.1  #increment time
    st.timer['text'] = round(st.t,1) #update t display in label
    if st.trocho_type_list[st.i%2] == "Hypotrochoides": trocho(hypo_cord_calculator, st.t) #will draw an hypotrochoide
    else: trocho(epi_cord_calculator, st.t) #will draw an épitrochoide
    st.win.after(st.bot_band_dic["speed"], tick) #speed of the drawing, determined by st.troco_speed

#=================================================================================    
def hypo_cord_calculator(t):
  """fonction to compute the point coordinates of a trochoide at t time
  """
  #VARIABLES----------------------------------------
  R = st.bot_band_dic["bot_band_fixe"]["R"] #R = radius of the fixed circle
  r = st.bot_band_dic["bot_band_rond"]["r"] #r = radius of the rolling circle
  h = st.bot_band_dic["bot_band_trocho"]["h"] #h = distance from the tracing point to the centre of the rolling circle
  m = R/r                    # m=R/r is the modulus of the trochoid
  #FONCTION-----------------------------------------
    #new point coords = begin point coord + parametric fonction
  xi = st.bot_band_dic["bot_band_fixe"]["xC"] + (R-r)*cos(t)+h*cos((R-r)*t/r) 
  yi = st.bot_band_dic["bot_band_fixe"]["yC"] + (R-r)*sin(t)-h*sin((R-r)*t/r) 
  return (xi, yi)

#=================================================================================    
def epi_cord_calculator(t):
  """fonction to compute the point coordinates of a trochoide at t time
  """
  #VARIABLES----------------------------------------
  R = st.bot_band_dic["bot_band_fixe"]["R"] #R = radius of the fixed circle
  r = st.bot_band_dic["bot_band_rond"]["r"] #r = radius of the rolling circle
  h = st.bot_band_dic["bot_band_trocho"]["h"] #h = distance from the tracing point to the centre of the rolling circle
  m = R/r                    # m=R/r is the modulus of the trochoid
  #FONCTION-----------------------------------------
    #new point coords = begin point coord + parametric fonction
  xi = st.bot_band_dic["bot_band_fixe"]["xC"] + (R+r)*cos(t)-h*cos((R+r)*t/r) 
  yi = st.bot_band_dic["bot_band_fixe"]["yC"] + (R+r)*sin(t)-h*sin((R+r)*t/r) 
  return (xi, yi)

#================================================================================
def trocho(trocho_type, t):
  """DOCKSTRING
  """
  st.points_coords_list[0] = trocho_type(0)  #first point of the trocho, initialised by 0 in settings
  st.points_coords_list.append(trocho_type(t)) #add the new point's coords tuple
    #create line with upadted point_coords_list     st.troco_color_entry.state    st.troco_width_entry.state
  st.canvas_item.append(st.canvas.create_line(st.points_coords_list, fill="blue", width=st.bot_band_dic["bot_band_trocho"]["width"]))
    #delete all the previous canvas_line.  
  if len(st.canvas_item) > 1 : #if there is only one canvas_line, do not delete it.
    for item in st.canvas_item[0:len(st.canvas_item)-1]: st.canvas.delete(item)

#===============================================================================
#===============================================================================
#===============================================================================
#===============================================================================
def on_start():
      """callback function for the 'START/STOP' button. Call the tick() fonction that call drawing fonctions."""
        # switch button (state <--> 1-stat)
      tg.type_checker()
      st.start_stop.state = 1 - st.start_stop.state 
        # if st.button.state == 1: tick() # start 'tick' when button state is 1
      if st.start_stop.state == 1: 
            #tg.save_value()
            tick() # start the recusive 

#===============================================================================      
def on_reset(): #exeption
    """
    callback fonction for the 'reset' button. exeption define the number of lines in st.canvas_item that wont be suppressed (from the 
    last created. If execption = 0, st.cavas_item is fully cleared. 
    """ 
    for item in st.canvas_item: st.canvas.delete(item) #  supress all created canvas_line except the last ones
    st.canvas_item = []#  actualise the liste of canvas lines
    st.points_coords_list = [0] #  supress all created points
    st.t = 0 #  reinitialise time

#===================================================================================

def pre_disp():
    """calback fontion for every parameting widgets (scale, entry...) which makes the display of parametings choosen by the user in real time,
    before he started to play."""
    return



#===================================================================================
    
