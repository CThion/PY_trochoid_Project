from ezTK import *
from math import *


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
    
    
def main():
    """programm tot test canvas widget"""
    global win
    win = Win(title="canvas_training", grow=True)
    
    win.canvas = Canvas(win, width=600, height=600)
    win.item = []
    xP, yP = 200, 200
    xQ = 400
    yQ = yP+abs(xQ-xP)
    
    win.roulette = win.canvas.create_oval(xP,yP,xQ,yQ)
    win.temoin = win.canvas.create_line(xP,yP,xQ,yQ)

    #win.roulette2 = win.canvas.create_oval(xP,yP,xQ,yQ)
    win.temoin2 = win.canvas.create_line(xP,yP,xQ,yQ,fill="blue")
    
    win.centre = win.canvas.create_line((xQ+xP)/2,2,(xQ+xP)/2,500, fill="blue")
    win.centre = win.canvas.create_line(2,(yQ+yP)/2, 500, (yQ+yP)/2, fill="green")
    
    movator()
    
    win.loop()
    


if __name__ == '__main__':
  main()
    
