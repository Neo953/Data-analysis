import pygame, random
from pygame.locals import*
from virus import virus
from doctor import doctor



pygame.it()
font = pygame.font.SysFont(None, 70)
split_time = 1-

size = (width, height) = (850,480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (25,255,255)

bacteria = pygame.sprite.Group()
doctor = pygame.sprite.Group()
def init():
    for i in range(bac_num:
def process_events():
    global check
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            check = True


def main():
    while True:
        clock.tick(60)
        process_events()
        screen.fill(color)
        doctor.draw(screen)
        bacteria.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
