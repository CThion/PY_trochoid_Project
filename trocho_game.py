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
    win.frameTop= Frame(win, bg='red', width=width, height=height//40, grow=False)  
    #principal frame
    win.frameprince= Frame(win, width=width, height=height, bg='black', flow='W')#frame principale 

#=======================================(parent: win.frameprince)===============================================
    win.BigBand = Frame(win.frameprince, bg='yellow', width=width, height=height, flow='S', grow=False)
    win.Left_Band = Frame(win.frameprince, bg='white', width=width, height=height, flow='S', border=5, grow=False)

#=======================================(parent: win.BigBand)===================================================
    win.midframe= Frame(win.BigBand, bg='red', width=width/2, height=0.7*height, border=4,flow='W', grow=False)
    win.botframe=Frame(win.BigBand,bg='blue', width=width, height=height, border=4, grow=False)

#=======================================(parent: win.midframe)==================================================
    #frame at right containing button for starting and drawing control while playing 
    win.play_ctr=Frame(win.midframe, bg='green', width=0.1*width, height=0.7*height, border=4, grow=False)
    #canvas to display the trocho
    win.canvas=Canvas(win.midframe, bg='purple', width=width, height=0.7*height, border=5, grow=False)

#=======================================(parent: win.Left_Band)===============================================
    #confining buttons into individul frame to better control their dimentions
  #-----------------  
    win.frBt_fixe= Frame(win.Left_Band, bg='gray', width=width, height=0.3*height, grow=True)
    Button(win.frBt_fixe,text='Choix de la forme fixe')
  #-----------------
    win.frBt_rond= Frame(win.Left_Band, bg='yellow', width=width, height=0.3*height, grow=True)
    Button(win.frBt_rond, text='Choix du rond mobile')
  #-----------------
    win.frBt_trocho= Frame(win.Left_Band, bg='red', width=width, height=0.3*height, grow=True)
    Button(win.frBt_trocho,text='Paramétres trochoides')
  #-----------------
    Button(win.play_ctr,text='Lets play')
#=======================================()===============================================
    win.loop()

   
if __name__ == '__main__':
  main()
    
