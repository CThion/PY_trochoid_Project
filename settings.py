#https://docs.python.org/3/faq/programming.html#id11
#https://stackoverflow.com/questions/13034496/using-global-variables-between-files
"""DDDDDDDDDDDDDDDDOOOOOOOOOOOOOOOOOOOOOCCCCCCCCCCCCCCCCKKKKKKKKKKKKKKKKKKKSTRINGGGGGGGGGGGGGGGGGG
"""

from ezTK import *
import bib_drawer as bd
#==============================================================================================================================================
win = Win(title='trochoïde', grow=True, flow='SE', op=2)
#==============================================================================================================================================
    #VARIABLES

t = 0 #global time used in parametrics equations

#=======================================list============================================
canvas_item = [] #  containers for all created canvas item
points_coords_list = [0]  #  list of points used to draw the trochoide curve, initialised with first point in 0
trocho_type_list = ['Hypotrochoides','Epitrochoides'] ; i=0  #liste of state for troco_type_butt, with i the current position in the list

#=======================================dic============================================
entry_dic={"bot_band_trocho":[], "bot_band_fixe":[],"bot_band_rond":[]} #each list will contain the widget of referent bot_band (used for test_error)

    #R=rayon cercle fixe
    #r=rayon cercle mobile
    #h= distance entre point de tracé et centre cercle mobile
    #xC yC coordonnées du centre du cercle fixe.
bot_band_dic = { #bibli of default values thare are used to intialise every onglet
    "bot_band_trocho":{#bot_band_trocho's values
            "h":100, 
            "color":"cyan", 
            "width":2, 
            }, 
    "bot_band_fixe":{ #bot_band_fixe's values
            "xC":300, 
            "yC":300,
            "R":100,
            "fixe_type":"oval", 
            "color":"blue", 
            "fixe_width":4
            }, 
    "bot_band_rond":{ #bot_band_rond's values
            "r":60, 
            "trocho_type":'Hypotrochoides', 
            "color":"red", 
            "rond_width":2
            }, 
    "speed":100} 


#=======================================indic============================================
display_indic ="parameting" #used by on_change() & on_return(). Default is "parameting", can also be "runing". Indicate which display is activ
bot_band_indic ="welcome" #used by on_save(), to know which bot_band is active. Initialised with bot_band_welcome
type_error_indic = False #indicator manage by type_error(), used by other fontion as a condition tu run or not. Get True when there is an error. False by default







