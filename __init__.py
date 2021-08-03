import pygame as p
p.init()
screen=p.display.set_mode((800,600))
p.display.set_caption("Chess")
running =True

while running :
    for event in p.event.get():
        if event.type == p.QUIT:
            running =False
    screen.fill((255,34,0))
    p.display.update()