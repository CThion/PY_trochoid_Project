
  
"""Our display screen for trochoid game"""
# ==============================================================================
__author__  = "Plantey--veux Axel & Thion Clement"
__version__ = "1.0" # draw lines, rectangles, ovals, strings and images
__date__    = "2020-04-"
# ==============================================================================
from PIL import ImageGrab
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
        'entry_dic', st.entry_dic,
        'entry_dic_bo_zejfoeriuhg', st.entry_dic["bot_band_trocho"],
        sep='\n',end='\n\n'
        )
    for value in st.entry_dic[st.bot_band_indic]: print(value.state)
    #st.TEST['state']='disabled'


#=====================================================================# la fonction suivante a été inspiré d'un auteur du forum trouvable ci dessous
#https://www.developpez.net/forums/d122973/autres-langages/python/gui/tkinter/tkinter-recuperer-contenu-d-canvas-sous-format-image/ inspiré de ce forum
def on_save_image():
    st.canvas.pack()
    x = Canvas.winfo_rootx(st.canvas)
    y = Canvas.winfo_rooty(st.canvas)
    w = Canvas.winfo_width(st.canvas)
    h = Canvas.winfo_height(st.canvas)
    img= ImageGrab.grab((x, y, x+w, y+h)).save("IMAGE.png")   
    MessageDialog.showinfo('INFO SAUVEGARDE', message='Votre fichier va etre sauvegarder dans le répertoire du fichier trocho')
#=====================================================================

#===============================================================================    
def type_checker():
  """fonction to check type of the value write by the user in the intries. Called by every bot_band_xxx(), and by every commmand's entry.
  """
  if st.bot_band_indic == "welcome": return #there is no value to check in bot_band_welcome
  for value in st.entry_dic[st.bot_band_indic]: #try every intry.state of the current bot_band
    try: int(value.state)
    except ValueError:#display a label on the canvas to warn the user about the mistake, and replace the wrong value by the latest good one.
        st.type_error_indic = True #indic that currently there is an error somewhere
        MessageDialog.showwarning('WARN', message='Attention, vous devez impérativement entrer un unique nombre')
        #test_fr_error = Frame(st.win,bg='red') 
        #Label(test_fr_error, text="attention, vous devez impérativement entrer un unique nombre")
        #error_message = st.canvas.create_window(100, 100, window=test_fr_error) 
        #st.win.after(4000, lambda:st.canvas.delete(error_message)) #delete warning message after 5 seconds
        return
  st.type_error_indic = False  #if try have went well, indic there is no wrong value anymore
  save_value() #save value because we're sure its type is good now.
           
#===============================================================================
def save_value():
    """save all value in dic (in settings). Called  by start_stop button and the three button of the left_band. Exception:colors values are saved 
    with on_scale()
    """
    
    st.bot_band_dic["speed"] = st.speed.state
    if st.bot_band_indic == "bot_band_trocho":
        st.bot_band_dic["bot_band_trocho"] = { # update all value in st.bot_band_indic with the curent states of all widgets conserned in the current bot_band 
        "h":int(st.h_entry.state), 
        "width":int(st.troco_width_entry.state), 
        }
    #---------------------------------------------
    elif st.bot_band_indic == "bot_band_rond":
        st.bot_band_dic["bot_band_rond"] = {# update all value in st.bot_band_indic with the curent states of all widgets conserned in the current bot_band
        "r":int(st.r_entry.state), 
        "trocho_type":st.troco_type_butt.state, 
        "rond_width":int(st.rond_width_entry.state)
        }
    #--------------------------------------------------
    elif st.bot_band_indic == "bot_band_fixe":
        #type_checker("error_xC")
        st.bot_band_dic["bot_band_fixe"] = { #values of all bot_band_fixe's entries 
        "xC":int(st.xC_entry.state), 
        "yC":int(st.yC_entry.state),
        "R":int(st.R_entry.state),
         
        "fixe_width":int(st.fixe_width_entry.state)
        }

#==================================================================================
def on_language(key_but):
  """callback function for all menu radiobuttons"""
  
  
    # Dont need to convert its str
  st.min= str(st.minmenu.state.get())
 #--------------------------Francais-----------------------------------------------
      
  if st.min == "Francais" and key_but == "trocho" :
      
      st.change1.state=0
      st.change2.state=0
      st.change3.state=0
      
      st.h_label.state=0 ; st.troco_color_label.state=0
      st.troco_width_label.state=0
      
  elif st.min == "Francais" and key_but == "fixe" :

    
      st.change1.state=0
      st.change2.state=0
      st.change3.state=0


      st.yC_label.state=0 ; st.xC_label.state=0 ;st.R_label.state=0
      st.fixe_width_label.state=0 ;st.fixe_color_label.state=0

  elif st.min == "Francais" and key_but == "rond" :

      st.change1.state=0
      st.change2.state=0
      st.change3.state=0  
      st.r_label.state=0 ;st.troco_type_label.state=0
      st.rond_color_label.state = 0 ;st.rond_width_label.state=0

 #--------------------------Anglais-----------------------------------------------
      

  elif st.min == "Anglais" and key_but == "trocho" :
      
      st.change1.state=1
      st.change2.state=1
      st.change3.state=1
      
      st.h_label.state=1 ; st.troco_color_label.state=1
      st.troco_width_label.state=1
      
  elif st.min == "Anglais" and key_but == "fixe" :
      
      st.change1.state=1
      st.change2.state=1
      st.change3.state=1


      st.yC_label.state=1; st.xC_label.state=1 ;st.R_label.state=1
      st.fixe_width_label.state=1;st.fixe_color_label.state=1
      
  elif st.min == "Anglais" and key_but == "rond" :

      st.change1.state=1
      st.change2.state=1
      st.change3.state=1

      

      st.r_label.state=1 ;st.troco_type_label.state=1
      st.rond_color_label.state = 1 ;st.rond_width_label.state=1
      
 #--------------------------Espagnol-----------------------------------------------         
  elif st.min == "Espagnol" and key_but == "trocho" :
      
      st.change1.state=2
      st.change2.state=2
      st.change3.state=2
      
      st.h_label.state=2 ; st.troco_color_label.state=2
      st.troco_width_label.state=2
      
  elif st.min == "Espagnol" and key_but == "fixe" :
      
      st.change1.state=2
      st.change2.state=2
      st.change3.state=2


      st.yC_label.state=2; st.xC_label.state=2 ;st.R_label.state=2
      st.fixe_width_label.state=2;st.fixe_color_label.state=2

  elif st.min == "Espagnol" and key_but == "rond" :
      
      st.change1.state=2
      st.change2.state=2
      st.change3.state=2

      

      st.r_label.state=2 ;st.troco_type_label.state=2
      st.rond_color_label.state = 2;st.rond_width_label.state=2

 #--------------------------Japonais-----------------------------------------------      

  elif st.min == "Japonais" and key_but == "trocho" :
      
      st.change1.state=3
      st.change2.state=3
      st.change3.state=3
      
      st.h_label.state=3 ; st.troco_color_label.state=3
      st.troco_width_label.state=3
      
  elif st.min == "Japonais" and key_but == "fixe" :
      
      st.change1.state=3
      st.change2.state=3
      st.change3.state=3


      st.yC_label.state=3; st.xC_label.state=3 ;st.R_label.state=3
      st.fixe_width_label.state=3;st.fixe_color_label.state=3
      
      
      
      

      #st.fixe_type_label.state=3

  elif st.min == "Japonais" and key_but == "rond" :
      
      st.change1.state=3
      st.change2.state=3
      st.change3.state=3

      

      st.r_label.state=3 ;st.troco_type_label.state=3
      st.rond_color_label.state = 3;st.rond_width_label.state=3
      
      
      #st.troco_type_label.state=3

#==================================================================================
def on_scale():
  """callback function for all three RGB scales"""
  x = '0123456789ABCDEF'
  r, g, b = st.win.R.state, st.win.G.state, st.win.B.state
  color = '#' + x[r//16] + x[r%16] + x[g//16] + x[g//16] + x[b//16] + x[b//16]
  st.win.brick['bg']= st.win.Label['text'] = color #update color on the display and in dictionnaries
  st.bot_band_dic[st.bot_band_indic]["color"] = color

#===================================================================================
def on_case(key_but2):
  """fonction to make switch the trocho_type button's text in bot_band_rond. Called by bot_band_rond
  """
  if key_but2=="Epi":
      st.troco_type_butt.state+=1

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
    st.bot_band_indic = "welcome" #update st.bot_band_indic in settings
    Label(st.big_band, text='Salamaalekum.')
        
def bot_band_fixe():
    type_checker()
    if st.type_error_indic : return #if there is an error in the current bot_band, don't set up the next bot_band til the problem is not solved
    st.bot_band_indic = "bot_band_fixe" #update st.bot_band_indic in settings
    st.entry_dic["bot_band_fixe"]=[] #if not done, st.entry_dic["bot_band_xxx"].append(st.YYY_entry) would make st.entry_dic bigger and bigger
    del st.big_band[1] #del previous bot_band
    st.bot_band_fixe = Frame(st.big_band,bg='yellow', width=900, height=300,flow='ES',fold=5, grow=True)
    fr1 = Frame(st.bot_band_fixe); fr2 = Frame(st.bot_band_fixe) ;fr3 = Frame(st.bot_band_fixe); fr4 = Frame(st.bot_band_fixe) #2 frame to aligne different widgets
    #-------------------------xC value-----------------------------
    st.xC_label = Label(fr1, text=('Choisir coords de x C','choice the x C coords','Elige coordenadas de x C','x C の座標を選択'))
    st.xC_entry = Entry(fr2, command=lambda:(bd.pre_disp(), type_checker() )) ; st.entry_dic["bot_band_fixe"].append(st.xC_entry) #add entry to entry_dic
    st.xC_entry.insert(0, st.bot_band_dic["bot_band_fixe"]['xC']) #default xC value
    #-------------------------yC value-----------------------------
    st.yC_label = Label(fr1, text=('Choisir coords de y C','choice the y C coords','Elige coordenadas de y C','y C の座標を選択'))
    st.yC_entry = Entry(fr2, command=lambda:(bd.pre_disp(), type_checker())); st.entry_dic["bot_band_fixe"].append(st.yC_entry) #add entry to entry_dic
    st.yC_entry.insert(0, st.bot_band_dic["bot_band_fixe"]['yC']) #default yC value
    #-------------------------R value------------------------------
    st.R_label = Label(fr1, text=('Choisir valeur R','choice the R value','Elige valor R','値を選択 R'))
    st.R_entry = Entry(fr2, command=lambda:(bd.pre_disp(), type_checker())); st.entry_dic["bot_band_fixe"].append(st.R_entry) #add entry to entry_dic
    st.R_entry.insert(0,st.bot_band_dic["bot_band_fixe"]['R']) #default R value    
    #-------------------------fixe_color------------------------------
    st.fixe_color_label = Label(fr3, text=('Choisir la couleur','Choose color','Elegir colores','色を選ぶ'))
    #____________Couleurs avec RGB_____________________________________________________
    
    Label(fr3)
    Label(fr3)
    Scale(fr4, scale=(0,255), troughcolor='#F00', show=False, command=on_scale)
    Scale(fr4, scale=(0,255), troughcolor='#0F0', show=False, command=on_scale)
    Scale(fr4, scale=(0,255), troughcolor='#00F', show=False, command=on_scale)
    
    st.win.R, st.win.G, st.win.B = fr4[0], fr4[1], fr4[2]
    st.win.Label, st.win.brick = fr3[1], fr3[2] 
    #-------------------------fixe_width------------------------------
    st.fixe_width_label = Label(fr1,text="Largeur")
    st.fixe_width_entry = Entry(fr2, command=lambda:(bd.pre_disp(), type_checker())) ; st.entry_dic["bot_band_fixe"].append(st.fixe_width_entry) #add entry to entry_dic
    st.fixe_width_entry.insert(0,st.bot_band_dic["bot_band_fixe"]["fixe_width"])
    #-------------------------------------------------------------------------
    #Permet d'afficher la zone sur laquelle l'utlisateur est à un moment "t" en mettant en blanc la chaine de caractéres du dit boutton activé et en mettant en noir les autres
    del st.frButt_fixe[0]
    st.change1 = Button(st.frButt_fixe,fg='white', text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda:(main_bot_band("fixe"), on_language("fixe")))
    del st.frButt_rond[0]
    st.change2 = Button(st.frButt_rond, text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda:(main_bot_band("rond"),on_language("rond")))
    del st.frButt_trocho[0]
    st.change3=Button(st.frButt_trocho,bg='purple',fg='black', text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda:(main_bot_band("trocho"),on_language("trocho")))
    
def bot_band_rond():
    type_checker()
    if st.type_error_indic : return #if there is an error in the current bot_band, don't set up the next bot_band til the problem is not solved
    #save_value() #save value of the current bot_band before delete it and set the bot_band_rond
    st.bot_band_indic = "bot_band_rond" #update st.bot_band_indic in settings
    st.entry_dic["bot_band_rond"]=[] #if not done, st.entry_dic["bot_band_xxx"].append(st.YYY_entry) would make st.entry_dic bigger and bigger
    del st.big_band[1] #del the current bot_band
    st.bot_band_rond = Frame(st.big_band,bg='yellow', width=900, height=300, flow='ES', fold=4, grow=True) #main frame
    fr1 = Frame(st.bot_band_rond); fr2 = Frame(st.bot_band_rond);fr3 = Frame(st.bot_band_rond);fr4 = Frame(st.bot_band_rond)#2 frame to aligne different widgets # 
    #-------------------------  r  ------------------------------
    st.r_label = Label(fr1, text=('Choix de la taille du cercle mobile','Choice of the size of the moving circle','Elección del tamaño del círculo móvil','動く円のサイズの選択')) 
    st.r_entry = Entry(fr2, command=lambda:(bd.pre_disp(), type_checker())); st.entry_dic["bot_band_rond"].append(st.r_entry) #add entry to entry_dic
    st.r_entry.insert(0,st.bot_band_dic["bot_band_rond"]['r']) #default r value
    #-------------------------trocho_type-----------------------------
    st.troco_type_label = Label(fr1, text=('Choix de la position du cercle mobile','Choice of the position of the moving circle','Elección de la posición del círculo móvil','動く円の位置の選択'))
    st.troco_type_butt = Button(fr2,text=('Hypotrochoides','Epitrochoides'),command=lambda : (on_case("Epi"), save_value()))  
    #--------------------------rond_color----------------------------
    st.rond_color_label = Label(fr3, text=('Choisir la couleur','Choose color','Elegir colores','色を選ぶ'))
    Label(fr3)
    Label(fr3)
    Scale(fr4, scale=(0,255), troughcolor='#F00', show=False, command=on_scale)
    Scale(fr4, scale=(0,255), troughcolor='#0F0', show=False, command=on_scale)
    Scale(fr4, scale=(0,255), troughcolor='#00F', show=False, command=on_scale)
    
    st.win.R, st.win.G, st.win.B = fr4[0], fr4[1], fr4[2]
    st.win.Label, st.win.brick = fr3[1], fr3[2] 
    #--------------------------rond_width----------------------------
    st.rond_width_label = Label(fr1, text=('Choisir largeur trocho','choice the trocho width','Elegir ancho','幅を選択してください'))
    st.rond_width_entry = Entry(fr2, command=lambda:(bd.pre_disp(), type_checker())); st.entry_dic["bot_band_rond"].append(st.rond_width_entry) #add entry to entry_dic
    st.rond_width_entry.insert(0, st.bot_band_dic["bot_band_rond"]['rond_width']) #default width value
    #---------------------------------------------------------------------------------------------------------
    #Permet d'afficher la zone sur laquelle l'utlisateur est à un moment "t" en mettant en blanc la chaine de caractéres du dit boutton activé et en mettant en noir les autres 
    del st.frButt_rond[0]
    st.change2 = Button(st.frButt_rond,fg='white', text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda:(main_bot_band("rond"),on_language("rond")))
    del st.frButt_trocho[0]
    st.change3 = Button(st.frButt_trocho,bg='purple',fg='black',  text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda:(main_bot_band("trocho"),on_language("trocho")))
    del st.frButt_fixe[0]
    st.change1 = Button(st.frButt_fixe, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda:(main_bot_band("fixe"), on_language("fixe")))

def bot_band_trocho():
    """DOCSTRING
    """
    type_checker()
    if st.type_error_indic : return #if there is an error in the current bot_band, don't set up the next bot_band til the problem is not solved
    st.bot_band_indic = "bot_band_trocho" #update st.bot_band_indic in settings
    st.entry_dic["bot_band_trocho"]=[] #if not done, st.entry_dic["bot_band_xxx"].append(st.YYY_entry) would make st.entry_dic bigger and bigger
    del st.big_band[1]
    st.bot_band_trocho = Frame(st.big_band,bg='yellow', width=900, height=300,flow='ES',fold=5, grow=True)
    #4 frame to aligne differents widgets
    fr1 = Frame(st.bot_band_trocho); fr2 = Frame(st.bot_band_trocho); fr3 = Frame(st.bot_band_trocho) ;fr4 = Frame(st.bot_band_trocho)
    #-------------------------h value------------------------------
    st.h_label = Label(fr1, text=('Choisir valeur h','choice the h value','Elige valor h','値を選択 h'))
    st.h_entry = Entry(fr2, command=lambda:(bd.pre_disp(), type_checker())); st.entry_dic["bot_band_trocho"].append(st.h_entry) #add entry to entry_dic
    st.h_entry.insert(0, st.bot_band_dic["bot_band_trocho"]['h']) #default h value
    #--------------------------troco_color----------------------------
    st.troco_color_label = Label(fr3, text=('Choisir la couleur','Choose color','Elegir colores','色を選ぶ'))
     
    Label(fr3)
    Label(fr3)
    Scale(fr4, scale=(0,255), troughcolor='#F00', show=False, command=on_scale)
    Scale(fr4, scale=(0,255), troughcolor='#0F0', show=False, command=on_scale)
    Scale(fr4, scale=(0,255), troughcolor='#00F', show=False, command=on_scale)
    
    st.win.R, st.win.G, st.win.B = fr4[0], fr4[1], fr4[2]
    st.win.Label, st.win.brick = fr3[1], fr3[2] 
    #--------------------------width----------------------------
    st.troco_width_label = Label(fr1, text=('Choisir largeur trocho','choice the trocho width','Elegir ancho','幅を選択してください'))
    st.troco_width_entry = Entry(fr2, command=lambda:(bd.pre_disp(), type_checker())); st.entry_dic["bot_band_trocho"].append(st.troco_width_entry) #add entry to entry_dic
    st.troco_width_entry.insert(0, st.bot_band_dic["bot_band_trocho"]['width']) #default width value 
    
    #Permet d'afficher la zone sur laquelle l'utlisateur est à un moment "t" en mettant en blanc la chaine de caractéres du dit boutton activé et en mettant en noir les autres
    st.change3 = Button(st.frButt_trocho,bg='purple',fg='white',  text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda:(main_bot_band("trocho"),on_language("trocho")))
    del st.frButt_trocho[0]
    del st.frButt_rond[0]
    st.change2 = Button(st.frButt_rond, text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda:(main_bot_band("rond"),on_language("rond")))
    del st.frButt_fixe[0]
    st.change1 = Button(st.frButt_fixe, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda:(main_bot_band("fixe"), on_language("fixe")))
    #st.troco_type_butt = Label(fr_speed, text=('  vitesse','  speed'))
    
#==============================================================================
def on_return():
    """fonction to switch from the "running" display (when the trocho is being drown) to the parameting display
    """
    width, height = 900, 500
    if st.display_indic == "running":
        #st.start_stop.state = 0
         #delete st.change_return button
          #now recreate all widgets of the parameting display
        Button(st.top_band,text="Sauvegarder l'image",command=on_save_image)
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
        st.display_indic = "parameting" #update st.display_indic
        del st.top_band[1]
        del st.top_band[0]
#------------------------------------------------------------------------------
def on_change():
    """fonction to switch from the parameting display (with left_band and bot_band) to the drawing display. Called by start_stop button
    """
    if st.display_indic == "parameting": #means "if we are currently with the parameting display"
        type_checker()
        if st.type_error_indic: return
        #save_value() #save value before deling the bot_band
        del st.left_band[0] #delete all widgets exept right_band and canvas
        del st.left_band[1]
        del st.frameking[1]
        del st.big_band[1]
        st.change_return = Button(st.top_band,text="Return",command=lambda:on_return()) #button to come back on the previous diplay
        st.display_indic="running" #update st.display_indic
        st.bot_band_indic="welcome" #in order not to get in the if condition in on_save() also called by start_stop
        bd.on_start() #now can start to draw
    else: bd.on_start()

#==============================================================================  
def main():
    """our graphic interface"""
    width, height = 900, 500
  #=======================================(parent: st.win)=======================================================
    st.top_band= Frame(st.win, bg='red', width=width, height=height//40, grow=False) #frame for general options (language...)

    Button(st.top_band,text="Sauvegarder l'image",command=on_save_image)
      #language début
    st.win.master['menu'] = menu = Menu(st.win.master)
    st.minmenu = Menu(menu, tearoff=False); st.minmenu.state = StringVar()
    menu.add_cascade(label='Langue', menu=st.minmenu)
    for value in ("Francais","Anglais","Espagnol","Japonais"):
        st.minmenu.add_radiobutton(label=value, var=st.minmenu.state, command=on_language(key_but="base"))
      #language fin    
    st.frameking= Frame(st.win, width=width, height=height, bg='black', flow='W')#principal frame
  #=======================================(parent: st.frameking)=================================================
    st.big_band = Frame(st.frameking, bg='yellow', width=(width)*3/4, height=height,op=0, flow='S', grow=True) #La largeur est égale à 1200 en sommant les deux largeurs
    st.left_band = Frame(st.frameking, bg='green', width=(width)*1/4, height=height,op=0, flow='S', grow=False)#On garde la même hauteur
  #=======================================(parent: st.big_band)===================================================
    st.prince_band = Frame(st.big_band, bg='red', width=(width)*3/4, height=(height)*7/10,op=0,flow='W', grow=True) #On garde la largeur de la frame parent
    bot_band_welcome()
  #    bot_band_fixe()
  #=======================================(parent: st.prince_band)================================================
    #frame at right containing button for starting and drast.wing control while playing 
    st.right_band = Frame(st.prince_band, bg='#FFAEC9', width=(width)*1/12, height=(height)*7/10, grow=True, flow='W')
    #canvas to display the trocho
    st.canvas = Canvas(st.prince_band, bg='white', width=(width)*2/3, height=(height)*7/10, grow=True)
  #=======================================(parent: st.left_band)==================================================
    #confining buttons into individul frame to better control their dimentions
  #-----------------  
    st.frButt_fixe = Frame(st.left_band, bg='gray', width=(width)*1/4, height=(height)*1/3, grow=True)
    st.change1 = Button(st.frButt_fixe, text=('Choix de la forme fixe','Choose of fix form','Elección de forma fija','固定形状の選択'),command=lambda:(type_checker(), main_bot_band("fixe"), on_language("fixe")))# Trois choix possibles 1 par state
  #-----------------
    st.frButt_rond = Frame(st.left_band, bg='cyan', width=(width)*1/4, height=(height)*1/3, grow=True)
    st.change2 = Button(st.frButt_rond, text=('Choix du rond mobile','Choose of mobile circle','Elección de la ronda móvil','移動ラウンドの選択'), command=lambda:(type_checker(), main_bot_band("rond"),on_language("rond")))# Trois choix possibles 1 par state
  #-----------------
    st.frButt_trocho = Frame(st.left_band, bg='purple', width=(width)*1/4, height=(height)*1/3, grow=True)
    st.change3 = Button(st.frButt_trocho,bg='purple',fg='black',  text=('Paramétres trochoides','Trochoids parameters','Parámetros trocoides','トロコイドパラメータ'),command=lambda:(type_checker(), main_bot_band("trocho"),on_language("trocho"))) # Trois choix possibles 1 par state
  #=======================================(prent: st.right_band)===============================================
    fr1 = Frame(st.right_band, flow='N'); fr2 = Frame(st.right_band, flow='N', grow=False)#; fr3 = Frame(st.right_band); fr4 = Frame(st.right_band,border=0,width=width,height=0,bd=0) ;fr5 = Frame(st.right_band,border=0,grow=True) 
    st.start_stop = Button(fr1, text=('start', 'stop'), grow=True, command=lambda:(on_change()))
    st.timer = Label(fr1, text=0, bd=1, grow=True)
    st.reset = Button(fr1, text='reset', grow=True, command=bd.on_reset)
    #speed 
    lapin = Image(file='lapin.gif')
    tortue = Image(file='tortue.gif')
    Label(fr2, image=tortue, grow=True)                                                                                                                                                                                                                                                           
    st.speed = Scale(fr2, flow="N", showvalue=0, bd=0, scale=(10, 1000), grow=True, command=lambda:save_value()) ; st.speed.set(st.bot_band_dic['speed']) #default speed
    Label(fr2, image=lapin, grow=True)                                                                                                                                                                                                                                                           
  #===================================================================================
    #widgets temporaire, seulement pour tester le programme graphiquement
    test_frame = Frame(st.win, bg="yellow")
    Button(test_frame, text="TEST", command=test)
    st.canvas.create_window(50, 50, window=test_frame)

  #===================================================================================
    st.win.loop()

   
if __name__ == '__main__':
  main()
    
