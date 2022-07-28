import pygame as pg

class Cuadrado:
    def __init__(self,x, y , w=25, h=25, color = (255,255,255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

        self.vx = 0
        self.vy = 0

    def velocidad(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def mover(self):
        self.x += self.vx


#Inicializa pygame siempre hay que hacer
pg.init()

pantalla_principal = pg.display.set_mode((800 , 600))
pg.display.set_caption("Bolitas rebotando")

cuadrado = Cuadrado(400,300, color=(255,255,0))
cuadrado2 = Cuadrado(400,300,35,35, color=(255,255,0))



game_over = False
while not game_over:
#Es para capturar los eventos, y los estructura:(Debería de vaciarse para no rebentar)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
    pantalla_principal.fill((0,0,255))#rgb orden de los colores
    
    
    
    pg.draw.rect(pantalla_principal,cuadrado.color(cuadrado.x, cuadrado.y, cuadrado.w, cuadrado.h))
    pg.draw.rect(pantalla_principal,cuadrado2.color(cuadrado2.x, cuadrado2.y, cuadrado2.w, cuadrado2.h))
    pg.display.flip()


pg.quit()

