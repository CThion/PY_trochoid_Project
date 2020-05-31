#https://docs.python.org/3/faq/programming.html#id11
#https://stackoverflow.com/questions/13034496/using-global-variables-between-files

from ezTK import *
#==============================================================================================================================================
global Win
win = Win(title='trochoïde', grow=True, flow='SE', op=2)
#==============================================================================================================================================


    #VARIABLES
win.t = 0 #global time used in parametrics equations
win.canvas_item = [] #  containers for all created canvas item

#==============================================================================================================================================
    #dictionnary for values of different bot_band 
hypo_dic = {"xC":200, "yC":200, "R":30, "r":30, "h":30, "troco_color":"cyan", "width":2} #values of all bot_band_trocho's entries
#R = radius of the fixed circle   #r = radius of the rolling circle  #h = distance from the tracing point to the centre of the rolling circle
win.points_coords_list = [(hypo_dic["xC"], hypo_dic["yC"])]  #  list of points used to draw the trochoide curve.

fixe_dic = {"fixe_color":"blue"} #values of all bot_band_fixe's entries 

rond_dic = {"rond_color":"red"} #values of all bot_band_rond's entries



    #used in epitroco et hypotroco et reset. stock points
#win.epi_points_coords_list = [0, 0]
#win.hypo_points_coords_list = [0, 0]
