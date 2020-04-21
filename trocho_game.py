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

#==============================================================================  
    
def main():
    """our graphic interface"""
    global win
    width, height = 500, 500
    win = Win(title='trochoïde', grow=True, flow='SE', op=2)
#=======================================(parent: win)=======================================================
    #frame for general options (language...)
    win.top_band= Frame(win, bg='red', width=width, height=height//40, grow=False)  
    #principal frame
    win.frameprince= Frame(win, width=width, height=height, bg='black', flow='W')#frame principale 

#=======================================(parent: win.frameprince)===============================================
    win.big_band = Frame(win.frameprince, bg='yellow', width=width, height=height, flow='S', grow=False)
    win.left_band = Frame(win.frameprince, bg='white', width=width, height=height, flow='S', border=5, grow=False)

#=======================================(parent: win.big_band)===================================================
    win.play_band= Frame(win.big_band, bg='red', width=width/2, height=0.7*height, border=4,flow='W', grow=False)
    win.bot_band=Frame(win.big_band,bg='blue', width=width, height=height, border=4, grow=False)

#=======================================(parent: win.play_band)==================================================
    #frame at right containing button for starting and drawing control while playing 
    win.play_ctr=Frame(win.play_band, bg='green', width=0.1*width, height=0.7*height, border=4, grow=False)
    #canvas to display the trocho
    win.canvas=Canvas(win.play_band, bg='purple', width=width, height=0.7*height, border=5, grow=False)

#=======================================(parent: win.left_band)===============================================
    #confining buttons into individul frame to better control their dimentions
  #-----------------  
    win.frButt_fixe= Frame(win.left_band, bg='gray', width=width, height=0.3*height, grow=True)
    Button(win.frButt_fixe,text='Choix de la forme fixe')
  #-----------------
    win.frButt_rond= Frame(win.left_band, bg='yellow', width=width, height=0.3*height, grow=True)
    Button(win.frButt_rond, text='Choix du rond mobile')
  #-----------------
    win.frButt_trocho= Frame(win.left_band, bg='red', width=width, height=0.3*height, grow=True)
    Button(win.frButt_trocho,text='Paramétres trochoides')
  #-----------------
    Button(win.play_ctr,text='Lets play')
#=======================================()===============================================
    win.loop()

   
if __name__ == '__main__':
  main()
    
