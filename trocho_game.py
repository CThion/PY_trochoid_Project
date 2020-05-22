
  # ==============================================================================
"""Our display screen for trochoid game"""
# ==============================================================================
__author__  = "Plantey--veux Axel & Thion Clement"
__version__ = "1.0" # draw lines, rectangles, ovals, strings and images
__date__    = "2020-04-"
# ==============================================================================
from ezTK import *
from math import *
import settings as st
import bib_drawer as bd
# ==============================================================================
def test():
    '''temporary fonction for checking out bib_drawer's issues'''
    #list_of_screen_coods = [(50,250),(150,100),(250,250),(350,100),(450,250),(550,100)]
    print(
        'st.win.canvas_item = ', st.win.canvas_item,
        'st.win.points_coords_list = ', st.win.points_coords_list,
        'plage normalement supprimée: ', st.win.canvas_item[0:len(st.win.canvas_item)-1],
        'nombre ditem de canvas', len(st.win.canvas_item),
        sep='\n',end='\n\n'
        )
    st.win.canvas.create_line([100,200,50,60])
    #st.win.TEST['state']='disabled'

#===================================================================================
def main_bot_band(key_butt):
    """callback fuction for buttons in left_band <forme fixe> <cercle mobile> <trait trocho>
    When called it does the switch from the parameting display to the drast.wing diplay, in
    the left_band
    The key_butt identify each of the three buttons"""
    #about <forme fixe> button  
    #affiachge 1
    if key_butt == 1: bot_band_fixe()
    #Affichage 2
    elif key_butt == 2: bot_band_rond()          
    #affichage 3
    else: bot_band_trocho()
        
def bot_band_fixe():
    del st.win.big_band[1]
    st.win.bot_band_fixe=Frame(st.win.big_band,bg='yellow', width=900, height=300, grow=True)
    st.win.label_aff_1=Label(st.win.bot_band_fixe, text=('Affichage 1'))
    
def bot_band_rond():
    del st.win.big_band[1]
    st.win.bot_band_rond=Frame(st.win.big_band,bg='yellow', width=900, height=300, grow=True)
    st.win.label_aff_2=Label(st.win.bot_band_rond, text='Affichage 2')

def bot_band_trocho():
    del st.win.big_band[1]
    st.win.bot_band_trocho=Frame(st.win.big_band,bg='yellow', width=900, height=300,flow='ES',fold=4, grow=True)
    #-------------------------xC value-----------------------------
    Label(st.win.bot_band_trocho, text='choice the x C coords')
    st.win.xC_entry = Entry(st.win.bot_band_trocho,command=bd.pre_disp)
    st.win.xC_entry.insert(0, 200)
    #-------------------------yC value-----------------------------
    Label(st.win.bot_band_trocho, text='choice the y C coords')
    st.win.yC_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.yC_entry.insert(0, 200)
    #-------------------------R value------------------------------
    Label(st.win.bot_band_trocho, text='choice the R value')
    st.win.R_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.R_entry.insert(0,30)
    #-------------------------r value------------------------------
    Label(st.win.bot_band_trocho, text='choice the r value')
    st.win.r_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.r_entry.insert(0,30)
    #-------------------------h value------------------------------
    Label(st.win.bot_band_trocho, text='choice the h value')
    st.win.h_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.h_entry.insert(0,30)
    #--------------------------Couleurs----------------------------
    Label(st.win.bot_band_trocho,text='Choisir la couleur')
    st.win.troco_color_entry=Entry(st.win.bot_band_trocho)
    st.win.troco_color_entry.insert(0,"cyan")
    #--------------------------Epaisseur----------------------------
    Label(st.win.bot_band_trocho, text='choice the trocho width')
    st.win.troco_width_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.troco_width_entry.insert(0,3)
    
#==============================================================================  
def main():
    """our graphic interface"""
    width, height = 900, 500
  #=======================================(parent: st.win)=======================================================
    #frame for general options (language...)
    st.win.top_band= Frame(st.win, bg='red', width=width, height=height//40, grow=False)  
    #principal frame
    st.win.frameking= Frame(st.win, width=width, height=height, bg='black', flow='W')#frame principale 

  #=======================================(parent: st.win.frameking)===============================================
    st.win.big_band = Frame(st.win.frameking, bg='yellow', width=(width)*3/4, height=height,op=0, flow='S', grow=True) #La largeur est égale à 1200 en sommant les deux largeurs
    st.win.left_band = Frame(st.win.frameking, bg='white', width=(width)*1/4, height=height,op=0, flow='S', grow=True)#On garde la même hauteur

  #=======================================(parent: st.win.big_band)===================================================
    st.win.prince_band= Frame(st.win.big_band, bg='red', width=(width)*3/4, height=(height)*7/10,op=0,flow='W', grow=True) #On garde la largeur de la frame parent
    #st.win.bot_band=Frame(st.win.big_band,bg='blue', width=900, height=300, border=4, grow=True) #Somme des hauteurs = 1000 
      #welcome message
    st.win.welcomeDisplay = Label(st.win.big_band, text='Salamaalekum.')
    main_bot_band(3)
  #=======================================(parent: st.win.prince_band)==================================================
    #frame at right containing button for starting and drast.wing control while playing 
    st.win.right_band=Frame(st.win.prince_band, bg='pink', width=(width)*1/12, height=(height)*7/10, grow=True,flow='S')
    #canvas to display the trocho
    st.win.canvas=Canvas(st.win.prince_band, bg='white', width=(width)*2/3, height=(height)*7/10, grow=True)
  #=======================================(parent: st.win.left_band)=============================================== 
    #confining buttons into individul frame to better control their dimentions
  #-----------------  
    st.win.frButt_fixe= Frame(st.win.left_band, bg='gray', width=(width)*1/4, height=(height)*1/3, grow=True)
    Button(st.win.frButt_fixe, text='Choix de la forme fixe', command=lambda: main_bot_band(1))
  #-----------------
    st.win.frButt_rond= Frame(st.win.left_band, bg='cyan', width=(width)*1/4, height=(height)*1/3, grow=True)
    Button(st.win.frButt_rond, text='Choix du rond mobile', command=lambda: main_bot_band(2))
  #-----------------
    st.win.frButt_trocho= Frame(st.win.left_band, bg='purple', width=(width)*1/4, height=(height)*1/3, grow=True)
    Button(st.win.frButt_trocho, text='Paramétres trochoides', command=lambda: main_bot_band(3))
  #=======================================(prent: st.win.play_ctr)===============================================
  #Boutons qui se changent tentative d'implantation de draw à trocho
    st.win.start_stop=Button(st.win.right_band,text=('start', 'stop'), grow=True, command=bd.on_start)
    st.win.timer = Label(st.win.right_band, text=0, border=1, grow=True)
    st.win.reset = Button(st.win.right_band, text='reset', grow=True, command=bd.on_reset)
  #===================================================================================
    #widgets temporaire, seulement pour tester le programme graphiquement
    test_frame = Frame(st.win, bg="yellow")
    Button(test_frame, text="TEST", command=test)
    st.win.canvas.create_window(50, 50, window=test_frame)
  #===================================================================================
    #bd.on_reset() #used one time to create the st.win.points_coords_list. Otherwise need to push stat/stop butt twice befor it start
    st.win.points_coords_list = st.win.points_coords_list + [st.win.xC_entry.state, st.win.yC_entry.state]
    st.win.loop()

   
if __name__ == '__main__':
  main()
    
