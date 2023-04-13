import pygame #Importa el modulo pygame
import sys 

ancho = 800 #Asigna el ancho inicado
alto = 500 #Asigna la altura indicada

pygame.init() #Inicia pygame
ventana=pygame.display.set_mode((ancho, alto)) #Establece ancho y alto en forma de tupla
pygame.display.set_caption("proyecto") #Establece el titulo de la ventana creada anteriormente


while True:
    ventana.fill([76,33,32])
    for evento in pygame.event.get():
        print(evento)
        if evento.type== pygame.QUIT: # Si se le da click a la X...
            sys.exit() #Cierra el juego
    pygame.display.update()
    