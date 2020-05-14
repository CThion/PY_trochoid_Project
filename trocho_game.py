# ==============================================================================
"""Our display screen for trochoid game"""
# ==============================================================================
__author__  = "Plantey--veux Axel & Thion Clement"
__version__ = "1.0" # draw lines, rectangles, ovals, strings and images
__date__    = "2020-04-"
# ==============================================================================
from ezTK import *
from math import *
# ==============================================================================
def tick():
    """recursive fonction calling hypo_trocho"""
    if win.start_stop['text']=="start": return
    win.t +=0.1
    win.timer['text'] = win.t #increment t
    hypo_trocho(win.t)
    win.after(100, tick)
#=================================================================================    
def hypo_trocho(t):
    """calcul a trochoide coord at time t, then add the coord to the global liste of coord, then trace the trochoide with all
    the point of this list, then remove the older line created."""
    #VARIABLES----------------------------------------
    R = int(win.R_entry.state) #R = radius of the fixed circle
    r = int(win.r_entry.state) #r = radius of the rolling circle
    h = int(win.h_entry.state) #h = distance from the tracing point to the centre of the rolling circle
    m = R/r                    # m=R/r is the modulus of the trochoid

    #FONCTION-----------------------------------------
      #  new point coords = begin point coord + parametric fonction
    xi = int(win.xC_entry.state) + (R+m*R)*cos(m*t)-h*cos(t+m*t) 
    yi = int(win.xC_entry.state) + -(R+m*R)*sin(m*t)+h*sin(t+m*t) 
      #  add nex point to point_list 
    win.points_coords_list.append((xi, yi)) #--add the new point's coords
      #  create line with upadted point_coords_list
    win.canvas_item.append(win.canvas.create_line(win.points_coords_list))
#================================================================================
def epi_trocho(t):
    """calcul a trochoide coord at time t, then add the coord to the global liste of coord, then trace the trochoide with all
    the point of this list, then remove the older line created."""
    #VARIABLES----------------------------------------
    R = int(win.R_entry.state) #R = radius of the fixed circle
    r = int(win.r_entry.state) #r = radius of the rolling circle
    h = int(win.h_entry.state) #h = distance from the tracing point to the centre of the rolling circle
    m = R/r                    # m=R/r is the modulus of the trochoid

    #FONCTION-----------------------------------------
      #new point coords = begin point coord + parametric fonction
    xi = int(win.xC_entry.state) + (R-m*R)*cos(m*t)+h*cos(t-m*t) 
    yi = int(win.yC_entry.state) + -(R-m*R)*sin(m*t)+h*sin(t-m*t) 
      #  add nex point to point_list 
    win.points_coords_list.append((xi, yi))
      #  create line with upadted point_coords_list
    win.canvas_item.append(win.canvas.create_line(win.points_coords_list))
    #--------------------------------------------------
    
    
#================================================================================
def test():
    '''temporary fonction for checking out bib_drawer's issues'''
    #list_of_screen_coods = [(50,250),(150,100),(250,250),(350,100),(450,250),(550,100)]
    print(
        'win.canvas_item = ', win.canvas_item,
        'win.points_coords_list = ', win.points_coords_list,
        sep='\n',end='\n\n'
        )
    win.canvas.create_line([100,200,50,60])
    #win.TEST['state']='disabled'
    

#================================================================================
def on_start():
      """callback function for the 'START/STOP' button"""
        # switch button (state <--> 1-stat)
      win.start_stop.state = 1 - win.start_stop.state 
        # if win.button.state == 1: tick() # start 'tick' when button state is 1
      if win.start_stop.state == 1: 
            # start the recusive 
            tick()
#=================================================================================          

def on_reset():
    """callback fonction for the 'reset' button"""
      #  supress all created canvas_line
    for item in win.canvas_item: win.canvas.delete(item)
      #  actualise the liste of canvas lines
    win.canvas_item = []
      #  supress all created points and initialised with start point coords.
    win.points_coords_list = [(int(win.xC_entry.state), int(win.yC_entry.state))]
      #  reinitialise time
    win.t = 0
#===================================================================================
def pre_disp():
    """calback fontion for every parameting widgets (scale, entry...)"""
    return
#===================================================================================
#===================================================================================
def main_bot_band(key_butt):

    """callback fuction for buttons in left_band <forme fixe> <cercle mobile> <trait trocho>
    When called it does the switch from the parameting display to the drawing diplay, in
    the left_band
    The key_butt identify each of the three buttons"""
    #about <forme fixe> button
      
      #affiachge 1
    if key_butt == 1:

        bot_band_fixe()
          
      #Affichage 2
    elif key_butt == 2:
    
        bot_band_rond()
              
      #affichage 3
    else:
        
        bot_band_trocho()
        

def bot_band_fixe():
    del win.big_band[1]
    win.bot_band_fixe=Frame(win.big_band,bg='yellow', width=900, height=300, grow=True)
    win.label_aff_1=Label(win.bot_band_fixe, text=('Affichage 1'))
    
def bot_band_rond():
    del win.big_band[1]
    win.bot_band_rond=Frame(win.big_band,bg='yellow', width=900, height=300, grow=True)
    win.label_aff_2=Label(win.bot_band_rond, text='Affichage 2')

def bot_band_trocho():
    global win  
    del win.big_band[1]
    win.bot_band_trocho=Frame(win.big_band,bg='yellow', width=900, height=300,flow='ES',fold=4, grow=True)
    

    #-------------------------xC value-----------------------------
    Label(win.bot_band_trocho, text='choice the x C coords')
    win.xC_entry = Entry(win.bot_band_trocho,command=pre_disp)
    win.xC_entry.insert(0, 200)
    #-------------------------yC value-----------------------------
    Label(win.bot_band_trocho, text='choice the y C coords')
    win.yC_entry = Entry(win.bot_band_trocho, command=pre_disp)
    win.yC_entry.insert(0, 200)
    
    #-------------------------R value------------------------------
    Label(win.bot_band_trocho, text='choice the R value')
    win.R_entry = Entry(win.bot_band_trocho, command=pre_disp)
    win.R_entry.insert(0,30)
    #-------------------------r value------------------------------
    Label(win.bot_band_trocho, text='choice the r value')
    win.r_entry = Entry(win.bot_band_trocho, command=pre_disp)
    win.r_entry.insert(0,30)
    
    #-------------------------h value------------------------------
    Label(win.bot_band_trocho, text='choice the h value')
    
    win.h_entry = Entry(win.bot_band_trocho, command=pre_disp)
    win.h_entry.insert(0,30)
    
    
#==============================================================================  
    
def main():
    """our graphic interface"""
    global win
    width, height = 1500, 1000
    win = Win(title='trochoïde', grow=True, flow='SE', op=2)
#===========================================================================================================
    win.canvas_item = [] #  list of points used to draw the trochoide curve.
    win.points_coords_list = [] #  containers for all created canvas item
    win.t = 0 #global time used in parametrics equations
#=======================================(parent: win)=======================================================
    #frame for general options (language...)
    win.top_band= Frame(win, bg='red', width=width, height=height//40, grow=False)  
    #principal frame
    win.frameking= Frame(win, width=width, height=height, bg='black', flow='W')#frame principale 

#=======================================(parent: win.frameking)===============================================
    win.big_band = Frame(win.frameking, bg='yellow', width=(width)*3/4, height=height,op=0, flow='S', grow=True) #La largeur est égale à 1200 en sommant les deux largeurs
    win.left_band = Frame(win.frameking, bg='white', width=(width)*1/4, height=height,op=0, flow='S', grow=True)#On garde la même hauteur

#=======================================(parent: win.big_band)===================================================
    win.prince_band= Frame(win.big_band, bg='red', width=(width)*3/4, height=(height)*7/10,op=0,flow='W', grow=True) #On garde la largeur de la frame parent
    #win.bot_band=Frame(win.big_band,bg='blue', width=900, height=300, border=4, grow=True) #Somme des hauteurs = 1000 
      #welcome message
    win.welcomeDisplay = Label(win.big_band, text='Salamaalekum.')
#=======================================(parent: win.prince_band)==================================================
    #frame at right containing button for starting and drawing control while playing 
    win.right_band=Frame(win.prince_band, bg='pink', width=(width)*1/12, height=(height)*7/10, grow=True,flow='S')
    #canvas to display the trocho
    win.canvas=Canvas(win.prince_band, bg='white', width=(width)*2/3, height=(height)*7/10, grow=True)

#=======================================(parent: win.left_band)=============================================== 
    #confining buttons into individul frame to better control their dimentions
  #-----------------  
    win.frButt_fixe= Frame(win.left_band, bg='gray', width=(width)*1/4, height=(height)*1/3, grow=True)
    Button(win.frButt_fixe, text='Choix de la forme fixe', command=lambda: main_bot_band(1))
  #-----------------
    win.frButt_rond= Frame(win.left_band, bg='cyan', width=(width)*1/4, height=(height)*1/3, grow=True)
    Button(win.frButt_rond, text='Choix du rond mobile', command=lambda: main_bot_band(2))
  #-----------------
    win.frButt_trocho= Frame(win.left_band, bg='purple', width=(width)*1/4, height=(height)*1/3, grow=True)
    Button(win.frButt_trocho, text='Paramétres trochoides', command=lambda: main_bot_band(3))
  #-----------------
    
    
    #would be a list to stock left_band's widget. If done, wouldn't be necessary to set <win.> to windget's name anymore.
    #win.left_band_list = []
    #win.left_band_list.append(win.frButt_fixe, win.frButt_rond, win.frButt_trocho)
#=======================================(prent: win.play_ctr)===============================================
#Boutons qui se changent tentative d'implantation de draw à trocho
    win.start_stop=Button(win.right_band,text=('start', 'stop'), grow=True, command=on_start)
    win.timer = Label(win.right_band, text=0, border=1, grow=True)
    win.reset = Button(win.right_band, text='reset', grow=True, command=on_reset)
    main_bot_band(3)
  

    on_reset()
    win.loop()

   
if __name__ == '__main__':
  main()
    
