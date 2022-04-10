import pygame

#Defining the constants

WIDTH = 500
HEIGHT = 600
WINDOW_COLOUR = (0,0,0)
FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#Function for the main window
def draw_window():
    WIN.fill(WINDOW_COLOUR)

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
    pygame.quit()

if __name__ == "__main__":
    main()