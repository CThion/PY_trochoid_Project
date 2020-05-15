
  
# ==============================================================================
"""Our display screen for trochoid game"""
# ==============================================================================
__author__  = "Plantey--veux Axel & Thion Clement"
__version__ = "1.0" # draw lines, rectangles, ovals, strings and images
__date__    = "2020-04-"
# ==============================================================================
from ezTK import *
from math import *
import bib_drawer as bd #if import all, conflict with main() in bib_drawer. Eventually changed.
# ==============================================================================

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
    del win.big_band[1]
    win.bot_band_trocho=Frame(win.big_band,bg='yellow', width=900, height=300, grow=True)
    win.label_aff_3=Label(win.bot_band_trocho, text='Affichage 3')    
    
#==============================================================================  
    





def main():
    """our graphic interface. La repartition du code dans main() suit la la logique de haut en bas gauche à droit de l'interface
    """
    global win
    
    width, height = 1300, 1000
    win = Win(title='trochoïde', width=width, height=height, flow='SE')
    win.width = win.winfo_width()
    win.height = win.winfo_height()
#=======================================(parent: win)=======================================================
    win.top_band= Frame(win, bg='red', height=win.height//40)  
  #----------------
    win.frameking= Frame(win, bg='black', flow='E') 

#=======================================( left_band )==parent:frameking===============================================
    win.left_band = Frame(win.frameking, bg='white', width=0.2*win.winfo_width(), flow='S')
#---------------------------------------------------------------------------------------------------------------------------
    Button(win.left_band, text='Choix de la forme fixe', command=lambda: main_bot_band(1))
  #-----------------
    Button(win.left_band, text='Choix du rond mobile', command=lambda: main_bot_band(2))
  #-----------------
    Button(win.left_band, text='Paramétres trochoides', command=lambda: main_bot_band(3))
  #-----------------

#=======================================( big_band )==parent:frameking===============================================
    win.big_band = Frame(win.frameking, bg='yellow', flow='S') #La largeur est égale à 1200 en sommant les deux largeurs
#---------------------------(prince_band)
    win.prince_band = Frame(win.big_band, bg='red', flow='W') #On garde la largeur de la frame parent
#--------(right_band)   
    win.right_band = Frame(win.prince_band, bg='cyan', width=100)
#--------(canvas)
    win.canvas = Canvas(win.prince_band, bg='white')
#---------------------------(bot_band)
    win.bot_band = Frame(win.big_band, bg='blue', height=height//10)
    win.welcomeDisplay = Label(win.bot_band, text='On mange des bébé mort.')

#=======================================(parent: win.prince_band)==================================================


    win.loop()

   
if __name__ == '__main__':
  main()
    

