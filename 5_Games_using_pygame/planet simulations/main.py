import pygame
import math

pygame.init()

WIDTH , HEIGHT = 800,800

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Planet Simulation")
WHITE = (33,45,66)
YELLOW = (255,255,9)
BLUE = (255,230,245)
RED = (10,12,30)
class planet:
    AU = (1.46e6 * 1000)
    G = 6.67428e-11
    SCALE = 100 / AU #1AU is approx 100 pixels
    TIMESTEP = 3600*24 #1 day
    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.sun = 0

        self.xvel = 0
        self.yvel = 0
        self.distance_to_sun = 0
        self.orbit = []
    def draw(self,win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        pygame.draw.circle(win,self.color,(x,y),self.radius)
    def attraction(self,other):
        other_x,other_y = other.x,other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        if other.sun:
            self.distance_to_sun = distance
        force = self.G * self.mass / distance**2
        theta = math.atan2(distance_y,distance_y)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x,force_y
    def update_position(self,planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self==planet:
                continue
            fx,fy = self.attraction(planet)
            total_fx +=fx
            total_fy +=fy
        self.x_vel = total_fx / self.mass * self.TIMESTEP
        self.y_vel = total_fy / self.mass * self.TIMESTEP
        self.x += self.y_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x,self.y))




#Gameloop
def main():
    run = True
    clock = pygame.time.Clock()

    sun = planet(0,0,30,YELLOW,1.98892 * 10**30)
    sun.sun = True
    earth = planet(-1* planet.AU,0,16,BLUE,5.9742 * 10**24)
    mars = planet(-1.525*planet.AU,0,12,RED,6.39* 10**23)
    planets = [sun,earth,mars]
    while run:
        clock.tick(60)
        WIN.fill((10,33,0))
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run = False
        for p in planets:
            WIN.fill((10,33,0))
            p.update_position(planets)
            p.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()

