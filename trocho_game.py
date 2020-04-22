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

def right_band_display():
    """callback fuction for buttons in left_band <forme fixe> <cercle mobile> <trait trocho>
    When called it does the switch from the parameting display to the drawing diplay, in
    the left_band
    The key_butt identify each of the three buttons"""
    #about <forme fixe> button
    win.right_band = Frame(win.prince_band, bg='green', width=100, height=700, border=4, flow='S', grow=True)
    win.speed_scale = Scale(win.right_band, scale=(0,99))
    win.start_butt = Button(win.right_band, text="START")
    #win.butt_forme_fixe.state=tk.DISABLED


#==============================================================================  
    
def main():
    """our graphic interface"""
    global win
    width, height = 1200, 1000
    win = Win(title='trochoïde', grow=True, flow='SE', op=2)
#=======================================(parent: win)=======================================================
    #frame for general options (language...)
    win.top_band= Frame(win, bg='red', width=width, height=height//40, grow=False)  
    #principal frame
    win.frameking= Frame(win, width=1200, height=1000, bg='black', flow='W')#frame principale 

#=======================================(parent: win.frameking)===============================================
    win.big_band = Frame(win.frameking, bg='yellow', width=900, height=1000, flow='S', grow=True) #La largeur est égale à 1200 en sommant les deux largeurs
    win.left_band = Frame(win.frameking, bg='white', width=300, height=1000, flow='S', border=5, grow=True)#On garde la même hauteur

#=======================================(parent: win.big_band)===================================================
    win.prince_band= Frame(win.big_band, bg='red', width=900, height=700, border=4,flow='W', grow=True) #On garde la largeur de la frame parent
    win.bot_band=Frame(win.big_band,bg='blue', width=900, height=300, border=4, grow=True) #Somme des hauteurs = 1000 

#=======================================(parent: win.prince_band)==================================================
    #frame at right containing button for starting and drawing control while playing 
    
    
    
    right_band_display()



    #canvas to display the trocho
    win.canvas=Canvas(win.prince_band, bg='purple', width=800, height=700, border=5, grow=True)
    
#=======================================(parent: win.left_band)=============================================== 
    #confining buttons into individul frame to better control their dimentions
  #-----------------  
    win.frButt_fixe= Frame(win.left_band, bg='gray', width=300, height=333, grow=True)
    Button(win.frButt_fixe, text='afficher right_band', command=right_band_display)
  #-----------------
    win.frButt_rond= Frame(win.left_band, bg='yellow', width=300, height=333, grow=True)
    Button(win.frButt_rond, text='masquer right_band', command=lambda: win.right_band.destroy())
  #-----------------
    win.frButt_trocho= Frame(win.left_band, bg='red', width=300, height=333, grow=True)
    Button(win.frButt_trocho, text='Paramétres trochoides', command=right_band_display)
  #-----------------
    win.butt_forme_fixe = win.left_band[0]
    win.butt_rond_mob = win.left_band[1]
    win.butt_troco = win.left_band[2]
    #would be a list to stock left_band's widget. If done, wouldn't be necessary to set <win.> to windget's name anymore.
    #win.left_band_list = []
    #win.left_band_list.append(win.frButt_fixe, win.frButt_rond, win.frButt_trocho)
#=======================================(prent: win.play_ctr)===============================================
    #Button(win.play_ctr,text='Lets play')
#
# 
    win.loop()

   
if __name__ == '__main__':
  main()
    
