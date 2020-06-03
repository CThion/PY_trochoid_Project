

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
        'st.canvas_item = ', st.canvas_item,
        'st.points_coords_list = ', st.points_coords_list,
        'plage normalement supprimée: ', st.canvas_item[0:len(st.canvas_item)-1],
        'nombre ditem de canvas', len(st.canvas_item),
        sep='\n',end='\n\n'
        )
    #st.TEST['state']='disabled'

def save_value():
    """save all value in dic (in settings). Called  by start_stop button and the three button of the left_band
    """


    

#===================================================================================
def on_language(key_but):
  """callback function for all menu radiobuttons"""
  
  
    # Dont need to convert its str
  st.min= str(st.minmenu.state.get())
 #--------------------------Francais-----------------------------------------------
      
  if st.min == "Francais" and key_but == "trocho" :
      
      st.change1.state=0
      st.change2.state=0
      st.change3.state=0
      st.change4.state=0
      st.change5.state=0
      st.change6.state=0
      st.change7.state=0
      st.change8.state=0
      st.change9.state=0
      st.change10.state=0
      
  elif st.min == "Francais" and key_but == "fixe" :

      
      st.change1.state=0
      st.change2.state=0
      st.change3.state=0

      
      st.change11.state=0
      st.change12.state=0
      st.change13.state=0

  elif st.min == "Francais" and key_but == "rond" :

      st.change1.state=0
      st.change2.state=0
      st.change3.state=0

      
      st.change14.state=0
      st.change15.state=0



      
 #--------------------------Anglais-----------------------------------------------
      

  elif st.min == "Anglais" and key_but == "trocho" :
      
      st.change1.state=1
      st.change2.state=1
      st.change3.state=1
      
      st.change4.state=1
      st.change5.state=1
      st.change6.state=1
      st.change7.state=1
      st.change8.state=1
      st.change9.state=1
      st.change10.state=1

      
  elif st.min == "Anglais" and key_but == "fixe" :
      
      st.change1.state=1
      st.change2.state=1
      st.change3.state=1
      
      st.change11.state=1
      st.change12.state=1
      st.change13.state=1
      
  elif st.min == "Anglais" and key_but == "rond" :

      st.change1.state=1
      st.change2.state=1
      st.change3.state=1

      st.change14.state=1
      st.change15.state=1

      



      
 #--------------------------Espagnol-----------------------------------------------         
  elif st.min == "Espagnol" and key_but == "trocho" :
      
      st.change1.state=2
      st.change2.state=2
      st.change3.state=2
     
      st.change4.state=2
      st.change5.state=2
      st.change6.state=2
      st.change7.state=2
      st.change8.state=2
      st.change9.state=2
      st.change10.state=2
      
  elif st.min == "Espagnol" and key_but == "fixe" :
      
      st.change1.state=2
      st.change2.state=2
      st.change3.state=2

      
      st.change11.state=2
      st.change12.state=2
      st.change13.state=2

  elif st.min == "Espagnol" and key_but == "rond" :
      
      st.change1.state=2
      st.change2.state=2
      st.change3.state=2

      st.change14.state=2
      st.change15.state=2




      
 #--------------------------Japonais-----------------------------------------------      

  elif st.min == "Japonais" and key_but == "trocho" :
      
      st.change1.state=3
      st.change2.state=3
      st.change3.state=3

      st.change4.state=3
      st.change5.state=3
      st.change6.state=3
      st.change7.state=3
      st.change8.state=3
      st.change9.state=3
      st.change10.state=3
      
  elif st.min == "Japonais" and key_but == "fixe" :
      
      st.change1.state=3
      st.change2.state=3
      st.change3.state=3

      st.change11.state=3
      st.change12.state=3
      st.change13.state=3

  elif st.min == "Japonais" and key_but == "rond" :
      
      st.change1.state=3
      st.change2.state=3
      st.change3.state=3

      st.change14.state=3
      st.change15.state=3

#===================================================================================
def on_case(key_but2):
  """"""
  if key_but2=="Epi":
      st.change16.state+=1
         
        
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
      Label(st.big_band, text='Salamaalekum.')
        
def bot_band_fixe():
    del st.big_band[1]
    st.bot_band_fixe = Frame(st.big_band,bg='yellow', width=900, height=300,flow='ES',fold=2, grow=True)
    #2 frame to aligne different widgets
    fr1 = Frame(st.bot_band_fixe); fr2 = Frame(st.bot_band_fixe)
    #----------------------------------------------------------------------------------------------------------------------------------------------#
    st.change11 = Label(fr1, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'))
    Entry(fr2)
    #-------------------------------------#
    st.change12 = Label(fr1, text=('Choix de la taille de la forme fixe','Choice of size of fixed shape','Elección del tamaño de la forma fija.','固定形状のサイズの選択'))
    Entry(fr2)
    #-------------------------------------#
    st.change13 = Label(fr1, text=('Choix de la postion de la forme fixe','Choice of the position of the fixed shape','Elección de la posición de la forma fija.','固定形状の位置の選択'))
    Entry(fr2)

    del st.frButt_fixe[0]
    st.change1 = Button(st.frButt_fixe,fg='white', text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda:(main_bot_band("fixe"), on_language("fixe")))
    del st.frButt_rond[0]
    st.change2 = Button(st.frButt_rond, text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda:(main_bot_band("rond"),on_language("rond")))
    del st.frButt_trocho[0]
    st.change3=Button(st.frButt_trocho,bg='purple',fg='black', text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda:(main_bot_band("trocho"),on_language("trocho")))
    
def bot_band_rond():
    width,height = 900,500
    del st.big_band[1]
    st.bot_band_rond=Frame(st.big_band,bg='yellow', width=900, height=300,flow='ES',fold=2, grow=True)
    #2 frame to aligne different widgets
    fr1 = Frame(st.bot_band_rond); fr2 = Frame(st.bot_band_rond)

    st.change14 = st.label_aff_2=Label(fr1, text=('Choix de la taille du cercle mobile','Choice of the size of the moving circle','Elección del tamaño del círculo móvil','動く円のサイズの選択'))
    
    Scale(fr2, orient='horizontal', scale=(0, 10))
    
    st.change15 = Label(fr1,text=('Choix de la position du cercle mobile','Choice of the position of the moving circle','Elección de la posición del círculo móvil','動く円の位置の選択'))
    
    st.change16 = Button(fr2,text=('Hypotrochoides','Epitrochoides'),command=lambda : on_case("Epi"))  

    del st.frButt_rond[0]
    st.change2 = Button(st.frButt_rond,fg='white', text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda:(main_bot_band("rond"),on_language("rond")))
    del st.frButt_trocho[0]
    
    st.change3 = Button(st.frButt_trocho,bg='purple',fg='black',  text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda:(main_bot_band("trocho"),on_language("trocho")))
    del st.frButt_fixe[0]
    st.change1 = Button(st.frButt_fixe, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda:(main_bot_band("fixe"), on_language("fixe")))

def bot_band_trocho():
    del st.big_band[1]
    st.bot_band_trocho = Frame(st.big_band,bg='yellow', width=900, height=300,flow='ES',fold=5, grow=True)
    #4 frame to aligne differents widgets
    fr1 = Frame(st.bot_band_trocho); fr2 = Frame(st.bot_band_trocho); fr3 = Frame(st.bot_band_trocho); fr4 = Frame(st.bot_band_trocho)
    #-------------------------xC value-----------------------------
    st.change10 = Label(fr1, text=('Choisir coords de x C','choice the x C coords','Elige coordenadas de x C','x C の座標を選択'))
    st.xC_entry = Entry(fr2, command=bd.pre_disp)
    st.xC_entry.insert(0, st.hypo_dic['xC']) #default xC value
    #-------------------------yC value-----------------------------
    st.change9 = Label(fr1, text=('Choisir coords de y C','choice the y C coords','Elige coordenadas de y C','y C の座標を選択'))
    st.yC_entry = Entry(fr2, command=bd.pre_disp)
    st.yC_entry.insert(0, st.hypo_dic['yC']) #default yC value
    #-------------------------R value------------------------------
    st.change8 = Label(fr1, text=('Choisir valeur R','choice the R value','Elige valor R','値を選択 R'))
    st.R_entry = Entry(fr2, command=bd.pre_disp)
    st.R_entry.insert(0,st.hypo_dic['R']) #default R value
    #-------------------------r value------------------------------
    st.change7 = Label(fr1, text=('Choisir valeur r','choice the r value','Elige valor r','値を選択 r'))
    st.r_entry = Entry(fr2, command=bd.pre_disp)
    st.r_entry.insert(0,st.hypo_dic['r']) #default r value
    #-------------------------h value------------------------------
    st.change6 = Label(fr3, text=('Choisir valeur h','choice the h value','Elige valor h','値を選択 h'))
    st.h_entry = Entry(fr4, command=bd.pre_disp)
    st.h_entry.insert(0, st.hypo_dic['h']) #default h value
    #--------------------------color----------------------------
    st.change5 = Label(fr3, text=('Choisir la couleur','Choose color','Elegir colores','色を選ぶ'))
    st.troco_color_entry=Entry(fr4)
    st.troco_color_entry.insert(0, st.hypo_dic['troco_color']) #default color value
    #--------------------------width----------------------------
    st.change4 = Label(fr3, text=('Choisir largeur trocho','choice the trocho width','Elegir ancho','幅を選択してください'))
    st.troco_width_entry = Entry(fr4, command=bd.pre_disp)
    st.troco_width_entry.insert(0, st.hypo_dic['width']) #default width value
    #--------------------------Speed--------------------------------
    
    
    st.change3 = Button(st.frButt_trocho,bg='purple',fg='white',  text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda:(main_bot_band("trocho"),on_language("trocho")))
    del st.frButt_trocho[0]

    del st.frButt_rond[0]
    st.change2 = Button(st.frButt_rond, text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda:(main_bot_band("rond"),on_language("rond")))
    del st.frButt_fixe[0]
    st.change1 = Button(st.frButt_fixe, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda:(main_bot_band("fixe"), on_language("fixe")))
    #st.change16 = Label(fr_speed, text=('  vitesse','  speed'))
    
#==============================================================================
def on_return(key_br):

    width, height = 900, 500

    if key_br=="Return":

        st.start_stop.state=0
        del st.top_band[0]
        main_bot_band("welcome")
        st.left_band = Frame(st.frameking, bg='green', width=(width)*1/4, height=height,op=0, flow='S', grow=True)
        
        st.frButt_fixe = Frame(st.left_band, bg='gray', width=(width)*1/4, height=(height)*1/3, grow=True)
        st.change1 = Button(st.frButt_fixe, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda:(main_bot_band("fixe"), on_language("fixe")))# Trois choix possibles 1 par state
  #-----------------
        st.frButt_rond = Frame(st.left_band, bg='cyan', width=(width)*1/4, height=(height)*1/3, grow=True)
        st.change2 = Button(st.frButt_rond, text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda:(main_bot_band("rond"),on_language("rond")))# Trois choix possibles 1 par state
  #-----------------
        st.frButt_trocho = Frame(st.left_band, bg='purple', width=(width)*1/4, height=(height)*1/3, grow=True)
        st.change3 = Button(st.frButt_trocho,bg='purple',fg='black', text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda:(main_bot_band("trocho"),on_language("trocho")))
        
#==============================================================================
def on_change(key_but3):
    save_value() #save value before deling the bot_band
    if key_but3=="Start":
        del st.left_band[0]
        del st.left_band[1]
        del st.left_band[0]
       
        del st.frameking[1]
        
        del st.big_band[1]

        st.change_return = Button(st.top_band,text="Return",command=lambda:on_return("Return"))

#==============================================================================  
def main():
    """our graphic interface"""
    width, height = 900, 500
  #=======================================(parent: st.win)=======================================================
    st.top_band= Frame(st.win, bg='red', width=width, height=height//40, grow=False) #frame for general options (language...)
    #language début
    
    st.win.master['menu'] = menu = Menu(st.win.master)
    st.minmenu = Menu(menu, tearoff=False); st.minmenu.state = StringVar()
    menu.add_cascade(label='Langue', menu=st.minmenu)
    for value in ("Francais","Anglais","Espagnol","Japonais"):
        st.minmenu.add_radiobutton(label=value, var=st.minmenu.state, command=on_language(key_but="base"))
    #language fin

    #principal frame
    
    st.frameking= Frame(st.win, width=width, height=height, bg='black', flow='W')#frame principale 

  #=======================================(parent: st.frameking)=================================================
    st.big_band = Frame(st.frameking, bg='yellow', width=(width)*3/4, height=height,op=0, flow='S', grow=True) #La largeur est égale à 1200 en sommant les deux largeurs
    st.left_band = Frame(st.frameking, bg='green', width=(width)*1/4, height=height,op=0, flow='S', grow=True)#On garde la même hauteur

  #=======================================(parent: st.big_band)===================================================
    st.prince_band = Frame(st.big_band, bg='red', width=(width)*3/4, height=(height)*7/10,op=0,flow='W', grow=True) #On garde la largeur de la frame parent
    main_bot_band("welcome")
  #=======================================(parent: st.prince_band)================================================
    #frame at right containing button for starting and drast.wing control while playing 
    st.right_band = Frame(st.prince_band, bg='#FFAEC9', width=(width)*1/12, height=(height)*7/10, grow=True, flow='W')
    #canvas to display the trocho
    st.canvas = Canvas(st.prince_band, bg='white', width=(width)*2/3, height=(height)*7/10, grow=True)
  #=======================================(parent: st.left_band)==================================================
    #confining buttons into individul frame to better control their dimentions
  #-----------------  
    st.frButt_fixe = Frame(st.left_band, bg='gray', width=(width)*1/4, height=(height)*1/3, grow=True)
    st.change1 = Button(st.frButt_fixe, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda:(main_bot_band("fixe"), on_language("fixe")))# Trois choix possibles 1 par state
  #-----------------
    st.frButt_rond = Frame(st.left_band, bg='cyan', width=(width)*1/4, height=(height)*1/3, grow=True)
    st.change2 = Button(st.frButt_rond, text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda:(main_bot_band("rond"),on_language("rond")))# Trois choix possibles 1 par state
  #-----------------
    st.frButt_trocho = Frame(st.left_band, bg='purple', width=(width)*1/4, height=(height)*1/3, grow=True)
    st.change3 = Button(st.frButt_trocho,bg='purple',fg='black',  text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda:(main_bot_band("trocho"),on_language("trocho"))) # Trois choix possibles 1 par state
  #=======================================(prent: st.right_band)===============================================
  #Boutons qui se changent tentative d'implantation de draw à trocho
    fr1 = Frame(st.right_band, flow='N'); fr2 = Frame(st.right_band, flow='N')#; fr3 = Frame(st.right_band); fr4 = Frame(st.right_band,border=0,width=width,height=0,bd=0) ;fr5 = Frame(st.right_band,border=0,grow=True) 
    st.start_stop=Button(fr1,text=('start', 'stop'), grow=True, command=lambda:(bd.on_start(),on_change("Start")))
    st.timer = Label(fr1, text=0, bd=1, grow=True)
    st.reset = Button(fr1, text='reset', grow=True, command=bd.on_reset)
    #speed 
    lapin = Image(file='lapin.gif')
    tortue = Image(file='tortue.gif')
    Label(fr2, image=lapin, grow=True)                                                                                                                                                                                                                                                           
    st.troco_speed = Scale(fr2, orient='VERTICAL', showvalue=0, bd=0, scale=(10, 1000), grow=True) ; st.troco_speed.set(st.hypo_dic['troco_speed']) #default speed
    Label(fr2, image=tortue, grow=True)                                                                                                                                                                                                                                                           
  #===================================================================================
    #widgets temporaire, seulement pour tester le programme graphiquement
    test_frame = Frame(st.win, bg="yellow")
    Button(test_frame, text="TEST", command=test)
    st.canvas.create_window(50, 50, window=test_frame)
  #===================================================================================
    st.win.loop()

   
if __name__ == '__main__':
  main()
    
