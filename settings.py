#https://docs.python.org/3/faq/programming.html#id11
#https://stackoverflow.com/questions/13034496/using-global-variables-between-files

from ezTK import *
import bib_drawer as bd
#==============================================================================================================================================
win = Win(title='trochoïde', grow=True, flow='SE', op=2)
#==============================================================================================================================================
    #VARIABLES
t = 0 #global time used in parametrics equations
canvas_item = [] #  containers for all created canvas item
points_coords_list = [0]  #  list of points used to draw the trochoide curve, initialised with first point in 0
display_indic ="parameting" #used by on_change() & on_return(). Default is "parameting", can also be "runing". Indicate which display is activ
bot_band_indic ="welcome" #used by on_save(), to know which bot_band is active
#==============================================================================================================================================
            #dictionnary for values of differents bot_band 
    #R=rayon cercle fixe
    #r=rayon cercle mobile
    #h= distance entre point de tracé et centre cercle mobile
    #xC yC coordonnées du centre du cercle fixe.
hypo_dic = { #values of all bot_band_trocho's entries
    "h":30, 
    "troco_color":"cyan", 
    "width":2, 
    "troco_speed":250
    } 
#-------------------
fixe_dic = { #values of all bot_band_fixe's entries 
    "xC":200, 
    "yC":200,
    "R":30,
    "fixe_type":"oval", 
    "fixe_color":"blue", 
    "fixe_width":4
    } 
#-------------------
rond_dic = { #values of all bot_band_rond's entries
    "r":30, 
    "trocho_type":"hypo", 
    "rond_color":"red", 
    "rond_width":2
    } 

#==============================================================================================================================================

