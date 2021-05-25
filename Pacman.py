import numpy as np
import random as rn

# =============================================================================
# Valores
# 0: espacio Vacio
# 6: Pacman
# 1: Pared
# 7,8,9: Fantasmas
# 2: Puntitos 
# =============================================================================

def crearTablero(filas=21,columnas=21):
    tablero = np.repeat(8, filas*columnas).reshape(filas, columnas)
    i = 0
    while i < columnas:
        tablero[(0,i)]= 1
        tablero[(filas-1), i]= 1
        i=i+1    
    j=0
    while j < filas:
        tablero[(j, columnas-1)]= 1
        tablero[(j, 0)]= 1
        j=j+1
    return tablero

   
def rellenarTablero(tablero):
    listaParedes=[(1,9),(1,10),(1,11),(2,2),(2,3),(2,5),(2,6),(2,7),(2,9),(2,10),(2,11),(2,13),(2,14),(2,15),(2,17),(2,18),(3,2),(3,3),(3,5),(3,6),(3,7),(3,9),(3,10),(3,11),(3,13),(3,14),(3,15),(3,17),(3,18),(4,2),(4,3),(4,9),(4,10),(4,11),(4,17),(4,18),(5,5),(5,7),(5,13),(5,15),(6,2),(6,3),(6,5),(6,7),(6,8),(6,9),(6,11),(6,12),(6,13),(6,15),(6,17),(6,18),(7,3),(7,5),(7,7),(7,13),(7,15),(7,17),(8,1),(8,3),(8,5),(8,7),(8,8),(8,9),(8,10),(8,11),(8,12),(8,13),(8,15),(8,17),(8,19),(9,5),(9,15),(10,2),(10,3),(10,7),(10,9),(10,10),(10,11),(10,13),(10,17),(10,18)
    ,(11,3),(11,5),(11,15),(11,17),(12,1),(12,3),(12,5),(12,7),(12,8),(12,9),(12,11),(12,12),(12,13),(12,15),(12,17),(12,19),(13,5),(13,15)
    ,(14,2),(14,3),(14,5),(14,7),(14,8),(14,9),(14,10),(14,11),(14,12),(14,13),(14,15),(14,17),(14,18),(15,3),(15,17),(16,2),(16,3),(16,4),(16,6),(16,8),(16,9),(16,10),(16,11),(16,12),(16,14),(16,16),(16,17),(16,19)
    ,(17,6),(17,10),(17,14),(18,2),(18,3),(18,4),(18,5),(18,6),(18,7),(18,8),(18,10),(18,12),(18,13),(18,14),(18,15),(18,16),(18,17),(18,18)]
    for i in range(0, len(listaParedes)):
        tablero[(listaParedes[i])]=1
    return
        
            
def posicionesIniciales(tablero):
    tablero[(15,10)]=7
    tablero[(7,8)]=2
    tablero[(7,9)]=3
    tablero[(7,10)]=4
    tablero[(7,11)]=5
    tablero[(7,12)]=6
    return
# NUMEROS LIBRES 8 9
def buscarPacman(tablero):
    n_fila = tablero.shape [0]
    n_col = tablero.shape [1]
    for i in range (1, n_fila-1) :
        for j in range (1, n_col-1):
            if tablero[(i,j)]==7:
                return ((i,j))
                

def buscarFantasmas(tablero):
    fantasmas=[2,3,4,5,6]
    coordFantasmas=[]
    n_fila = tablero.shape [0]
    n_col = tablero.shape [1]
    for i in range (1, n_fila-1) :
        for j in range (1, n_col-1):
            if tablero[(i,j)] in fantasmas:
                coordFantasmas.append((i,j))
    return coordFantasmas

def graficar(tablero):         
    k=0
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if i!=k:
                print()
                k+=1
            if tablero[(i,j)]==0:
                print(chr(0x00002B1C),end="")
            if tablero[(i,j)]==1:
                print(chr(0x00002B1B),end="")
            if tablero[(i,j)]==8:
                print(chr(0x00002728),end="")
            if tablero[(i,j)]==7:
                print(chr(0x0001F617),end="")
            if tablero[(i,j)]==2 or tablero[(i,j)]==3 or tablero[(i,j)]==4 or tablero[(i,j)]==5 or tablero[(i,j)]==6:
                print(chr(0x0001F47B),end="")
    print()

def moverPacman(tablero, tecla):
    pacman= buscarPacman(tablero)
    x=pacman[0]
    y=pacman[1]
    if tecla == "w" and tablero[x-1,y]!= 1:
        tablero[x-1,y]= tablero[pacman]
        tablero[pacman]= 0
    if tecla == "a" and tablero[x, y-1] != 1:
        tablero[x,y-1]= tablero[pacman]
        tablero[pacman]= 0
    if tecla == "s" and tablero[x+1,y]!= 1:
                tablero[x+1,y]= tablero[pacman]
                tablero[pacman]= 0
    if tecla == "d" and tablero[x,y+1]!= 1:
                tablero[x,y+1]= tablero[pacman]
                tablero[pacman]= 0

def misVecinos(coord):
    adyacentes=[]
    x=coord[0]
    y=coord[1]
    prioridad=[(x-1,y),(x,y+1),(x+1,y),(x,y-1)]
    for i in prioridad:
        if ((i[0]>0) and (i[1]>0)):
            adyacentes.append(i)
    rn.shuffle(adyacentes)
    return adyacentes
                    
def buscar_adyacente(tablero, coord):
    lista=[]
    for vecino in misVecinos(coord):
        if tablero[vecino]==0 or tablero[vecino]==7 or tablero[vecino]==8:
            lista.append(vecino)
            return lista
    return []

def moverFantasmas(tablero):
    fantasmas= buscarFantasmas(tablero)
    for i in range(0, len(fantasmas)):
        
        comer=buscar_adyacente(tablero, fantasmas[i])
        if 7 in comer:            
            return False
        
        mover=buscar_adyacente(tablero, fantasmas[i])
        if len(mover)>0:
            posicionAnterior= tablero[mover[0]]
            tablero[mover[0]]= tablero[fantasmas[i]]
            tablero[fantasmas[i]]= posicionAnterior
    

tablero = crearTablero()
rellenarTablero(tablero)
posicionesIniciales(tablero)


tecla = input()
while(tecla!= "q"):
    moverFantasmas(tablero)
    moverPacman(tablero,tecla)
    graficar(tablero)
    tecla = input()



