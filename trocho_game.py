

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
    #st.win.TEST['state']='disabled'

def save_value(key_butt):
    """"""
    if key_butt == 1: return

#===================================================================================

#===================================================================================
def main_bot_band(key_butt):
    """callback fuction for buttons in left_band <forme fixe> <cercle mobile> <trait trocho>
    When called it does the switch from the parameting display to the drast.wing diplay, in
    the left_band
    The key_butt identify each of the three buttons"""
    #about <forme fixe> button  
    #welcome message
    if key_butt == "welcome": bot_band_welcome()
    #affiachge "fixe"
    elif key_butt == "fixe": bot_band_fixe()
    #Affichage "rond"
    elif key_butt == "rond": bot_band_rond()          
    #affichage "trocho"
    else: bot_band_trocho()

def bot_band_welcome():
      Label(st.win.big_band, text='Salamaalekum.')
        
def bot_band_fixe():
    del st.win.big_band[1]
    st.win.bot_band_fixe=Frame(st.win.big_band,bg='yellow', width=900, height=300,flow='ES',fold=2, grow=True)
    #----------------------------------------------------------------------------------------------------------------------------------------------#
    st.win.change11=Label(st.win.bot_band_fixe, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'))
    Entry(st.win.bot_band_fixe)
    #-------------------------------------#
    st.win.change12=Label(st.win.bot_band_fixe, text=('Choix de la taille de la forme fixe','Choice of size of fixed shape','Elección del tamaño de la forma fija.','固定形状のサイズの選択'))
    Entry(st.win.bot_band_fixe)
    #-------------------------------------#
    st.win.change13=Label(st.win.bot_band_fixe, text=('Choix de la postion de la forme fixe','Choice of the position of the fixed shape','Elección de la posición de la forma fija.','固定形状の位置の選択'))
    Entry(st.win.bot_band_fixe)
    
def bot_band_rond():
    del st.win.big_band[1]
    st.win.bot_band_rond=Frame(st.win.big_band,bg='yellow', width=900, height=300, grow=True)
    st.win.label_aff_2=Label(st.win.bot_band_rond, text='Choix de la taille du cercle mobile')
    Scale(st.win.bot_band_rond,orient='vertical', scale=(0, 10))
    Label(st.win.bot_band_rond,text='Choix de la position du cercle mobile')
    Checkbutton(st.win.bot_band_rond, text='Epitrochoides')
    Checkbutton(st.win.bot_band_rond, text='Hypotrochoides')

def bot_band_trocho():
    del st.win.big_band[1]
    st.win.bot_band_trocho=Frame(st.win.big_band,bg='yellow', width=900, height=300,flow='ES',fold=4, grow=True)
    #-------------------------xC value-----------------------------
    st.win.change10=Label(st.win.bot_band_trocho, text=('Choisir coords de x C','choice the x C coords','Elige coordenadas de x C','x C の座標を選択'))
    st.win.xC_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.xC_entry.insert(0, st.hypo_dic['xC'])
    #-------------------------yC value-----------------------------
    st.win.change9=Label(st.win.bot_band_trocho, text=('Choisir coords de y C','choice the y C coords','Elige coordenadas de y C','y C の座標を選択'))
    st.win.yC_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.yC_entry.insert(0, st.hypo_dic['yC'])
    #-------------------------R value------------------------------
    st.win.change8=Label(st.win.bot_band_trocho, text=('Choisir valeur R','choice the R value','Elige valor R','値を選択 R'))
    st.win.R_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.R_entry.insert(0,st.hypo_dic['R'])
    #-------------------------r value------------------------------
    st.win.change7=Label(st.win.bot_band_trocho, text=('Choisir valeur r','choice the r value','Elige valor r','値を選択 r'))
    st.win.r_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.r_entry.insert(0,st.hypo_dic['r'])
    #-------------------------h value------------------------------
    st.win.change6=Label(st.win.bot_band_trocho, text=('Choisir valeur h','choice the h value','Elige valor h','値を選択 h'))
    st.win.h_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.h_entry.insert(0, st.hypo_dic['h'])
    #--------------------------Couleurs----------------------------
    st.win.change5=Label(st.win.bot_band_trocho,text=('Choisir la couleur','Choose color','Elegir colores','色を選ぶ'))
    st.win.troco_color_entry=Entry(st.win.bot_band_trocho)
    st.win.troco_color_entry.insert(0,"cyan")
    #--------------------------Epaisseur----------------------------
    st.win.change4=Label(st.win.bot_band_trocho, text=('Choisir largeur trocho','choice the trocho width','Elegir ancho','幅を選択してください'))
    st.win.troco_width_entry = Entry(st.win.bot_band_trocho, command=bd.pre_disp)
    st.win.troco_width_entry.insert(0,3)
    
#==============================================================================  
def main():
    """our graphic interface"""
    width, height = 900, 500
  #=======================================(parent: st.win)=======================================================
    #frame for general options (language...)
    st.win.top_band= Frame(st.win, bg='red', width=width, height=height//40, grow=False)
    #language début
    
    st.win.master['menu'] = menu = Menu(st.win.master)
    st.win.minmenu = Menu(menu, tearoff=False); st.win.minmenu.state = StringVar()
    menu.add_cascade(label='Langue', menu=st.win.minmenu)
    for value in ("Francais","Anglais","Espagnol","Japonais"):
        st.win.minmenu.add_radiobutton(label=value, var=st.win.minmenu.state, command=bd.on_language)
    #language fin

    #principal frame
    
    st.win.frameking= Frame(st.win, width=width, height=height, bg='black', flow='W')#frame principale 

  #=======================================(parent: st.win.frameking)=================================================
    st.win.big_band = Frame(st.win.frameking, bg='yellow', width=(width)*3/4, height=height,op=0, flow='S', grow=True) #La largeur est égale à 1200 en sommant les deux largeurs
    st.win.left_band = Frame(st.win.frameking, bg='white', width=(width)*1/4, height=height,op=0, flow='S', grow=True)#On garde la même hauteur

  #=======================================(parent: st.win.big_band)===================================================
    st.win.prince_band= Frame(st.win.big_band, bg='red', width=(width)*3/4, height=(height)*7/10,op=0,flow='W', grow=True) #On garde la largeur de la frame parent
    main_bot_band("welcome")
  #=======================================(parent: st.win.prince_band)================================================
    #frame at right containing button for starting and drast.wing control while playing 
    st.win.right_band=Frame(st.win.prince_band, bg='pink', width=(width)*1/12, height=(height)*7/10, grow=True,flow='S')
    #canvas to display the trocho
    st.win.canvas=Canvas(st.win.prince_band, bg='white', width=(width)*2/3, height=(height)*7/10, grow=True)
  #=======================================(parent: st.win.left_band)==================================================
    #confining buttons into individul frame to better control their dimentions
  #-----------------  
    st.win.frButt_fixe= Frame(st.win.left_band, bg='gray', width=(width)*1/4, height=(height)*1/3, grow=True)

    st.win.change1=Button(st.win.frButt_fixe, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda: main_bot_band("fixe"))# Trois choix possibles 1 par state
  #-----------------
    st.win.frButt_rond= Frame(st.win.left_band, bg='cyan', width=(width)*1/4, height=(height)*1/3, grow=True)
    st.win.change2=Button(st.win.frButt_rond, text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda: main_bot_band("rond"))# Trois choix possibles 1 par state
  #-----------------
    st.win.frButt_trocho= Frame(st.win.left_band, bg='purple', width=(width)*1/4, height=(height)*1/3, grow=True)
    st.win.change3=Button(st.win.frButt_trocho, text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda: main_bot_band("trocho")) # Trois choix possibles 1 par state
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
    st.win.loop()

   
if __name__ == '__main__':
  main()
    
