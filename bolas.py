import pygame as pg
import random 


class Cuadrado:
    def __init__(self,x, y , w=25, h=25, color = (255,255,255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

        self.vx = 3
        self.vy = 3

    def velocidad(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def mover(self, xmax, ymax):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= xmax - self.w:
            self.vx *= -1

        if self.y <= 0 or self.y >= ymax - self.h:
            self.vy *= -1

#Inicializa pygame siempre hay que hacer.
pg.init()

#Medida de la pantalla principal.
pantalla_principal = pg.display.set_mode((800 , 600))

#Nombre de la pantalla.
pg.display.set_caption("Bolitas rebotando")

cuadrado = Cuadrado(400,300, color=(255,255,0))
cuadrado.velocidad(5,5)
cuadrado2 = Cuadrado(400,300,35,35, color=(0,255,0))
cuadrado2.velocidad = (random.randint(-10, 10),random.randint(-10, 10))

game_over = False
while not game_over:
#Es para capturar los eventos, y los estructura:(Debería de vaciarse para no reventar)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0,0,255))#rgb orden de los colores de la pantalla principal
    cuadrado.mover(800,600)
    cuadrado2.mover(800,600)
    
    pg.draw.rect(pantalla_principal, cuadrado.color, (cuadrado.x, cuadrado.y, cuadrado.w, cuadrado.h))
    pg.draw.rect(pantalla_principal, cuadrado2.color, (cuadrado2.x, cuadrado2.y, cuadrado2.w, cuadrado2.h))
    pg.display.flip()

pg.quit()

