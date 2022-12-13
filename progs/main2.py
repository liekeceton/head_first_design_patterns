from sys import path
path.append('C:\\Users\\LiekeCeton\\Projects\\Education\\packages') #Append path with sys.path.append
# #Add init.py to indicate that these are modules yto walk through

# import extra.iota #Use points to navigate through the structurepip
# print(extra.iota.FunI())

import extra.good
# from extra.good.best.tau import FunT

# print(extra.good.best.sigma.FunS())
# print(FunT())

# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False

from platform import processor

print(processor())
print(extra.entities())