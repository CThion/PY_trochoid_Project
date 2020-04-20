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



def movator():
    """vitesse linéaire: d/t : (d=2px)/(t=10ms)
    ==> vitesse constante pour l'instant, on verra plus tard
    pour passer à v en dérivé."""

    xPw, yPw, xQw, yQw = win.canvas.coords(win.roulette)
    xC, yC = (xPw+xQw)/2,(yPw+yQw)/2 #coords du centre des cercles
    xP, yP, xQ, yQ = xPw-xC, yPw-yC, xQw-xC, yQw-yC #changement de variabe, on se ramène à l'origine du repère
    R = sqrt((xQ-xP)**2+(yQ-yP)**2)/2 #rayon du cercle contenant le carré contenant la roulette.
    #a = d/(2*R) #angle de rotation, dépendant de d
    
    for k in range(1,4):
        a = radians(k*20)
    #nouvelles coords du point P
        xP2 = xP*cos(a)+yP*sin(a) + xC 
        yP2 = -xP*sin(a)+yP*cos(a) + yC 
    #nouvelles coords du point Q
        xQ2 = xQ*cos(a)+yQ*sin(a) + xC 
        yQ2 = -xQ*sin(a)+yQ*cos(a) + yC

        #win.canvas.create_oval(xP2, yP2, xQ2, yQ2, outline="blue")
        win.canvas.create_line(xP2, yP2, xQ2, yQ2, fill="red")

    #win.canvas.coords(win.roulette, xP2, yP2, xQ2, yQ2)
    #win.canvas.coords(win.temoin, xP2, yP2, xQ2, yQ2)
    #win.after(t, movator(d, t))









def drawLine():
    #initialisation
    xa, ya, xb, yb = win.canvas.coords(win.item[-1])#coords du dernier oval
    xa, ya, xb, yb = xa+8*cos(xa+3), ya+8*sin(ya+3), xb+8*cos(xb+3), yb+8*sin(yb+3) #new coords
    win.item.append([win.canvas.create_oval(xa, ya, xb, yb)])#new oval               
    win.canvas.after(10, drawLine)

def arret():

    if win.start.state == 1: win.after(10, arret)
    
#==============================================================================
def on_start():
  """callback function for the 'START/STOP' button"""
  win.start.state=1-win.start.state
  print(win.start.state)
#===========================================  

def on_state():
    """permet de changer les états des boutons de choix de forme"""
    win.start2.state=win.start2.state+1
    win.start3.state=win.start2.state
    print(win.start2.state)
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
    win.frameMain= Frame(win, width=width, height=height, bg='blue')#frame principale (avec le caneva et ctrl)
    frameLeftBand = Frame(win.frameMain, width=width, height=height, grow=False)#bandeau gauche
    frameLeftBand_1= Frame(frameLeftBand,bg='white', width=110, height=90, border=5, flow='S', grow=False)
    win.start=Button(frameLeftBand_1, text=("Start drawing",'Stop drawing'),command=on_start)
    Button(frameLeftBand_1, text="Clear drawing")
    win.start2=Button(frameLeftBand_1, text=('Choose the form'),command=on_state)
    win.start2=Button(frameLeftBand_1, text=('carré','rond','fonction')) #Bouton qui se modifie en fonction du state
    win.start3=Button(frameLeftBand_1, text=('Côté','Rayon','f(x)='))#Idem qui ci-dessus
    Button(frameLeftBand_1, text="Couelur du trait ")
    Button(frameLeftBand_1, text="Epaisseur du trait ")
    Entry(frameLeftBand_1, width=10)
    win.canvas = Canvas(win.frameMain, bg="white")
    win.item.append([win.canvas.create_oval(100, 100, 110, 110, fill="black")])
    win.canvas.create_line(5,5,6,6,7,7,8,8,9,9,10,10,14,14,19,28,57,64)
    win.after(1000, drawLine) # start animation after 1000ms
  #-----------------------------------------------------------------------------
    #win.width, win.height = width, height 

if __name__ == '__main__':
  main()
    
