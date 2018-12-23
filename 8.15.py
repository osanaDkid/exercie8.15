##Résolution de l'exercice 15
##du chapitre 8 de gérard swinen
##on déplace des sphrères censé être des astres
##le programme montre la distance entre les sphères
##la force exercée sur chaque sphère
##Aussi le programme doit permettre de changer
##la valeur des charges de chaque atre


from tkinter import *
from math import sqrt

######### _Gestionnaire d'événements_ ########
def distance(x1,y1,x2,y2):
    di = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return di


def force_g(d, m1, m2):
    force = 6.67e-11 * m1*m2 / d**2
    return force

##cette fonction permet la sélection
##d'une sphère avec le cliq droit
def selection(event):
    global  n
    i = event.x
    u = event.y
    if i <= x[0]+15 and i >= x[0]-15 and u <= y[0]+15 and u >= y[0]-15 :
        n = 0
    if i <= x[1]+15 and i >= x[1]-15 and u <= y[1]+15 and u >= y[1]-15 :
        n = 1
    if i <= x[2]+15 and i >= x[2]-15 and u <= y[2]+15 and u >= y[2]-15 :
        n = 2
def moove(event):
    global x,y,n
    selection(event)            #Fonction qui permet la selection des sphères
    gd = event.x
    hb = event.y
    x[n], y[n] = event.x,event.y
    caneva.coords(oval[n],x[n] - 15,y[n] - 15,x[n]+15,y[n]+15)
    #calcul de la nouvelle distance
    di1 = distance(x[0],y[0],x[1],y[1])
    di2 = distance(x[1],y[1],x[2],y[2])
    di3 = distance(x[2],y[2],x[0],y[0])
    #convertion de la nouvelle distance
    d1 = di1*1e9
    d2 = di2*1e9
    d3 = di3*1e9
    #calcul des forces
    f1 = force_g(d1,m1,m2)
    f2 = force_g(d2,m1,m2)
    f3 = force_g(d3,m1,m2)
    
    valg1.configure(text = "F = "+str(f2 + f3))
    vald1.configure(text = "D = "+str(d1))

    valg2.configure(text = "F = "+str(f1 + f3))
    vald2.configure(text = "D = "+str(d2))

    valg3.configure(text = "F = "+str(f1 + f2))
    vald3.configure(text = "D = "+str(d3))



################## ___ PROGRAMME PRINCIPAL ___ #################

##Création et positionnement des GUI

fen = Tk()
m1 = 4e6
m2 = 4e6
m3 = 4e6

fra1 = Frame(fen)
fra2 = Frame(fen)
fra3 = Frame(fen)

    ## Coordonnées des sphères
oval = [0]*3
x = [75, 125, 175]
y = [125, 175, 225]
n = 0
caneva = Canvas(fen, width = 400, height=400, bg = "ivory" )
    ## Création des sphères

oval[0] = caneva.create_oval(x[0],y[0],x[0]+30, y[0]+30, fill = "red")
oval[1] = caneva.create_oval(x[1],y[1],x[1]+30, y[1]+30, fill = "green")
oval[2] = caneva.create_oval(x[2],y[2],x[2]+30, y[2]+30, fill = "blue")



valm1 = Label(fra1, text="M2 ="+ str(m1), fg = "red")
valm2 = Label(fra2, text="M2 ="+ str(m2), fg = "green")
valm3 = Label(fra3, text="M3 ="+ str(m3), fg = "blue")
valg1 = Label(fra1, text = "F = ......", fg = "red")
valg2 = Label(fra2, text = "F = ......", fg = "green")
valg3 = Label(fra3, text = "F = ......", fg = "blue")
vald1 = Label(fen, text = "D1 - D2 = ......", fg = "navy")
vald2 = Label(fen, text = "D1 - D3 = ......", fg = "purple")
vald3 = Label(fen, text = "D2 - D3 = ......", fg = "orange")

    ##packetage des différents widgets des frames
valm1.pack()
valg1.pack()
valm2.pack()
valg2.pack()
valm3.pack()
valg3.pack()

caneva.bind("<Button-1>",moove)



    ##positionnement des widgets
fra1.grid(row =0, sticky = W )
fra2.grid(row =1, sticky = W )
fra3.grid(row =2, sticky = W )
caneva.grid(row =0, column =1, rowspan = 2, columnspan = 3)
vald1.grid(row = 2, column = 1)
vald2.grid(row = 2, column = 2)
vald3.grid(row = 2, column = 3)




fen.mainloop()
