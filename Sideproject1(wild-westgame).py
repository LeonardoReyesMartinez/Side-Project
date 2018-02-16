"""
SideProject: Reaction Timer/wild west

Description:
"""
import pygame
import tsk
pygame.init()
window = pygame.display.set_mode([1018, 572])
background = tsk.Sprite("RockCityCenter.jpg", 0, 0)
boulder = tsk.Sprite("Boulder.png", 450, 300)
enemy = tsk.Sprite("AlienBeetle.png", 100, 300)
drawing = True
flip_x = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
    enemy.scale = 0.5
    background.draw()
    boulder.draw()
    enemy.draw()
    pygame.display.flip()
