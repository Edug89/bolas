import pygame as pg
import random

class Rectangulo:
    def __init__(self, x, y, w= 0, h=0, color=(255,255,255),vx = 0, vy = 0):
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
        if self.x >= tam_pantalla[0] - self.w or self.x <= 0:
            self.vx = - self.vx
        if self.y >= tam_pantalla[1] - self.h or self.y <= 0:
            self.vy = - self.vy

    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color, (self.x, self.y, self.w, self.h))


pg.init()
tam_pantalla = (800,600)
cantidad_rectangulos = (15)

pantalla_principal = pg.display.set_mode((tam_pantalla))
pg.display.set_caption("Rectángulos botarines")
diccionario = {}
for rectangulos_saltarines in range(cantidad_rectangulos):
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    velocidad = (random.randint(1,10), random.randint(1,10))
    tamano = (random.randint(25,55), random.randint(25,55))
    diccionario[rectangulos_saltarines] = Rectangulo(400,300, color = color, vx = velocidad[0], vy = velocidad[1], w = tamano[0], h = tamano[1])
game_over = False


while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((255,135,135))
    for rectangulos_finitos in range(cantidad_rectangulos):
        diccionario[rectangulos_finitos].dibujar(pantalla_principal)
        diccionario[rectangulos_finitos].mover()

    pg.display.flip()

pg.quit()

