from lib2to3.pgen2.token import COLON
import pygame
import os



#CONSTANTS AND LOADING
Wid,Hei = 900,500
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40
VEL = 3
WIN  = pygame.display.set_mode((Wid,Hei))
pygame.display.set_caption("Game 1")
COLOUR = (0,0,102)  #RGB colour values are stored here
FPS = 60 #Framerate per second
#Loading 2 images 
#we use os so that the path is found
SHIP_1 = pygame.image.load(os.path.join(
    "Assets",'spaceship_yellow.png'))
SHIP_2 = pygame.image.load(os.path.join(
    "Assets",'spaceship_red.png'))
#pygame.transform is used to rotate and scale the image
SHIP_1 = pygame.transform.rotate(pygame.transform.scale(
    SHIP_1,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
SHIP_2 = pygame.transform.rotate(pygame.transform.scale(
    SHIP_2,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

#Declaring the main surface
def draw_window(red,yellow):
    WIN.fill((COLOUR)) 
    WIN.blit(SHIP_1,(yellow.x,yellow.y))
    WIN.blit(SHIP_2,(red.x,red.y)) #Blit is used to put images and texts onto the screen
    pygame.display.update()

#to press the keys and define movements for red and yellow
def yellow_handle_movement(keys_pressed,yellow):
        if keys_pressed[pygame.K_a]: #LEFT
            yellow.x-=VEL
        if keys_pressed[pygame.K_d]: #RIGHT
            yellow.x+=VEL
        if keys_pressed[pygame.K_w]: #UP
            yellow.y-=VEL
        if keys_pressed[pygame.K_s]: #DOWN
            yellow.y+=VEL

def red_handle_movement(keys_pressed,red):
        if keys_pressed[pygame.K_RIGHT]: #RIGHT
            red.x+=VEL
        if keys_pressed[pygame.K_UP]: #UP
            red.y-=VEL
        if keys_pressed[pygame.K_DOWN]: #DOWN
            red.y+=VEL
        if keys_pressed[pygame.K_LEFT]: #LEFT
            red.x-=VEL

def main():
    red = pygame.Rect(675,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(225,200,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock() #run at 60FPS
    run = True
    while run:        #Ensures that the game keeps running
        clock.tick(FPS)
        i = 200
        for event in pygame.event.get(): #Shows the event
            if event.type == pygame.QUIT: #Quiting the application
                run = False
            draw_window(red,yellow)
        keys_pressed = pygame.key.get_pressed() #returns the key getting pressed
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
    pygame.quit()  #Quits the application


if __name__ == "__main__":
    main()