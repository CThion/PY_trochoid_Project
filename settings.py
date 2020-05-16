#https://docs.python.org/3/faq/programming.html#id11
#https://stackoverflow.com/questions/13034496/using-global-variables-between-files

from ezTK import *

global Win
win = Win(title='trochoïde', grow=True, flow='SE', op=2)



    #VARIABLES
win.canvas_item = [] #  list of points used to draw the trochoide curve.
win.points_coords_list = [] #  containers for all created canvas item
win.t = 0 #global time used in parametrics equations


    #used in epitroco et hypotroco et reset. stock points
#win.epi_points_coords_list = [0, 0]
#win.hypo_points_coords_list = [0, 0]