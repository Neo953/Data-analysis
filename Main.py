import pygame
from pygame.locals import*
import random

from virus import virus
from doctor import doctor



pygame.init()
font = pygame.font.SysFont(None, 70)
split_time = 10
doc_num = 100
bac_num = 1000
round_over = False
size = (width, height) = (850,480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (25,255,255)

bacteria = pygame.sprite.Group()
doctor = pygame.sprite.Group()
def init():
    global round_over
    doctor.empty()
    bacteria.empty()
    round_over = False
    for i in range(bac_num):
        bacteria.add(virus((random.randint(50, width-50), random.randint(50, height-50)), split_time))
    for i in range(doc_num):
        doctor.add(doctor((random.randint(50, width - 50), random.randint(50, height - 50))))
    global check
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            check = True

def timeout():
    for i in range(300):
        clock.tick(60)
        process_events()

def end():
    timeout()
    init()




def process_events():
    global check
    for event in pygame.get():
        if event.type == pygame.QUIT:
            check = True

def main():
    global round_over
    init()
    while True:
        clock.tick(60)
        process_events()
        if len(bacteria) > bac_num*split_time:
            text = font.render("You were beaten", True, (255,0,0))
            text.rect = text.get_rect()
        elif len(bacteria) == 0:
            text = font.render("You win!", True,(255,0,0))
            text_rect = text.get_rect()
            round_over = True
        else:
            doctor.update()
            bacteria()
            pygame.sprite.groupcollide(doctor, bacteria, False, True)
            text = font.render("bacteria count: {}".format(len(bacteria)), True, (255,0,0))
            text_rect = text.get_rect()
        screen.fill(color)
        doctor.draw(screen)
        bacteria.draw(screen)
        pygame.display.flip()
        if round_over:
            end()

if __name__ == "__main__":
    main()
