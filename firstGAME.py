#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Isobel Huckaby
#
# Created:     17/12/2013
# Copyright:   (c) Isobel Huckaby 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#def main():
#    pass

bif="bg.jpg"
mif="poop.png"

import pygame, sys
from pygame.locals import *

pygame.init ()
screen=pygame.display.set_mode((1216,687),0,32)
#background size for window, 32 bit

background=pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))

    x,y = pygame.mouse.get_pos()
    x -= mouse_c.get_width()/2
    y -= mouse_c.get_height()/2

    screen.blit(mouse_c,(x,y))
    pygame.display.update()








#if __name__ == '__main__':
#    main()
