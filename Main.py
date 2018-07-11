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
    for i in range(bac_num):
        bacteria.add(Virus((random.randint(50, width-50), random.randint(50, height-50))
    for i in range(doc_num):
        doctors.add(doctor((random.randint(50, width - 50), random.randint(50, height - 50))))
    global check
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            check = True


def main():
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
        else:
            doctor.update()
            bacteria()
            pygame.sprite.groupcollide(doctor, bacteria, False ,True)
            text = font.render("bacteria count: {}".format(len(bacteria)), True, (255,0,0))
            text_rect = text.get_rect()
        screen.fill(color)
        doctor.draw(screen)
        bacteria.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
