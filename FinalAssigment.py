import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Final Assigment ICS2O')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

win = pygame.display.set_mode((500, 500))

x = 50
y = 50
width = 40
hight = 60
vel = 5

run = True
while run:
  pygame.time.delay(100)

for event in pygame.event.get():
  if event.type == pygame.QUIT:
    run = False

  pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
  pygame.display.update()

pygame.quit()


