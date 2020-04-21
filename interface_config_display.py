# ==============================================================================
"""CANVAS : demo program for the Canvas widget"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # draw lines, rectangles, ovals, strings and images
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
from math import *
# ==============================================================================

#==============================================================================  
    
def main():
    """our graphic interface"""
    global win
    width, height = 1000, 1000
    win = Win(title='trochoïde', grow=True, flow='SE', op=2)
    win.item = []
    
  #-----------------------------------------------------------------------------bandeau supérieur
    win.frameTop= Frame(win, bg='red', width=width, height=25, grow=False)
  #-----------------------------------------------------------------------------

    #Frame Begin
    
    win.frameprince= Frame(win, width=width, height=height, bg='black',flow='W')#frame principale 
    win.BigBand = Frame(win.frameprince,bg='yellow', width=width, height=height,flow='S', grow=False)
    win.Left_Band = Frame(win.frameprince,bg='white', width=width, height=height,flow='S', border=5, grow=False)
    win.midframe= Frame(win.BigBand, bg='red', width=500, height=700,border=4,flow='W',grow=False)
    win.botframe=Frame(win.BigBand,bg='blue',width=width,height=height,border=4,grow=False)
    win.play_ctr=Frame(win.midframe,bg='green',width=100,height=700,border=4,grow=False)
    win.canvas=Canvas(win.midframe,bg='purple',width=1000, height=700,border=5,grow=False)
    win.frBt_fixe= Frame(win.Left_Band,bg='gray',width=width,height=300,grow=True)
    win.frBt_rond= Frame(win.Left_Band,bg='yellow',width=width,height=300,grow=True)
    win.frBt_trocho= Frame(win.Left_Band,bg='red',width=width,height=300,grow=True)

    #Frame end

    #Button Begin
    Button(win.play_ctr,text='Lets play')
    Button(win.frBt_fixe,text='Choix de la forme fixe')
    Button(win.frBt_rond,text='Choix du rond fixe')
    Button(win.frBt_trocho,text='Paramétres trochoides')

    #Button End
    
   
    
  #-----------------------------------------------------------------------------
    #win.width, win.height = width, height 

if __name__ == '__main__':
  main()
    
