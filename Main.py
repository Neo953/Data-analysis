import pygame
from pygame.locals import*

pygame.it()
size = (width, height) = (850,480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (25,255,255)

bacteria = pygame.sprite.Group()
doctor = pygame.sprite.Group()

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
