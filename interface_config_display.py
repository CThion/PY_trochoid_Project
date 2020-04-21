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
    
    frameprince= Frame(win, width=width, height=height, bg='black',flow='W')#frame principale 
    BigBand = Frame(frameprince,bg='yellow', width=width, height=height,flow='S', grow=False)
    Left_Band = Frame(frameprince,bg='white', width=width, height=height,flow='S', border=5, grow=False)
    midframe= Frame(BigBand, bg='red', width=500, height=700,border=4,flow='W',grow=False)
    botframe=Frame(BigBand,bg='blue',width=width,height=height,border=4,grow=False)
    play_ctr=Frame(midframe,bg='green',width=100,height=700,border=4,grow=False)
    canvas=Canvas(midframe,bg='purple',width=width, height=700,border=5,grow=False)

    #Frame end

    #Button Begin

    Button(play_ctr,text='Lets play')
    Button(Left_Band,text='Choix de la forme fixe')
    Button(Left_Band,text='Choix de la forme du rond')
    Button(Left_Band,text='Choix de la forme fixe')

    #Button End
    
   
    
  #-----------------------------------------------------------------------------
    #win.width, win.height = width, height 

if __name__ == '__main__':
  main()
    
