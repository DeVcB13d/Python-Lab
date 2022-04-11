import pygame
import numpy as np
#Defining the constants
WIN_HEI = 600
WIDTH = 400
HEIGHT = 400
WINDOW_COLOUR = (247,16,78)
LINE_COLOUR = (60,0,199)
CIRCLE_COLOUR = (0,0,0)
FPS = 60
WIN = pygame.display.set_mode((WIDTH,WIN_HEI))
LINE_THIC = 10
SHAPE_THICK = 20
#Function for the main window
def draw_window():
    WIN.fill(WINDOW_COLOUR)
    pygame.draw.line(WIN,LINE_COLOUR,(0,HEIGHT/3),(WIDTH,HEIGHT/3),LINE_THIC)
    pygame.draw.line(WIN,LINE_COLOUR,(0,2*(HEIGHT/3)),(WIDTH,2*(HEIGHT/3)),LINE_THIC)
    pygame.draw.line(WIN,LINE_COLOUR,(WIDTH/3,0),(WIDTH/3,HEIGHT),LINE_THIC)
    pygame.draw.line(WIN,LINE_COLOUR,(2*(WIDTH/3),0),(2*(WIDTH/3),HEIGHT),LINE_THIC)
Pdata = np.zeros((3,3))
def Pdata_updata(row,col,XO):
    Pdata[row][col] = XO

def Isfull():
    ret = True
    for i in range(0,3):
        for j in range(0,3):
            if Pdata[i][j] == 0 :
                ret = False
    return ret

def draw_shape(x,y,player):
    if player == 1:
        pygame.draw.circle(WIN,CIRCLE_COLOUR,[x,y],((WIDTH/3)-1),SHAPE_THICK)


#Main functions
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            draw_window()
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__" :
    main()