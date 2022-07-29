import pygame as pg
import random 

class Cuadrado:
    def __init__(self,x, y, w=25,h=25, color = (255,255,255),vx =0 ,vy = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy

    def mover(self,):
        self.x += self.vx
        self.y += self.vy
        if self.x >= tam_pan[0] - self.w or self.x  <= 0:
            self.vx = - self.vx
        if self.y >= tam_pan[1] - self.h or self.y  <= 0:
            self.vy = - self.vy

    def dibujar(self, pantalla):
        pg.draw.rect(pantalla,self.color, (self.x, self.y, self.w, self.h))
        
pg.init()
cantidad_cuadrados = 50
tam_pan = (800,600)

pantalla_principal = pg.display.set_mode((tam_pan))
pg.display.set_caption("Bolitas rebotando")
diccionario = {}
for cuadrados_finitos in range(cantidad_cuadrados):
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #tamano = (random.randint(10,45), random.randint(10,45))#revisar tamaño
    velocidad = (random.randint(1,10), random.randint(1,10))
    diccionario[cuadrados_finitos] = Cuadrado(400,300, color = color, vx = velocidad[0], vy = velocidad[1])
game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0,0,255))
    for cuadrados_finitos in range(50):
        diccionario[cuadrados_finitos].dibujar(pantalla_principal)#Pendiente arreglar
        diccionario[cuadrados_finitos].mover()#Pendiente arreglar


    pg.display.flip()

pg.quit()

