import pygame
from pygame.locals import*
import random

from virus import virus
from doctor import Doctor
import matplotlib.pyplot as plt


pygame.init()
font = pygame.font.SysFont(None, 70)
split_time = 10
doc_num = 100
bac_num = 100
round_over = False

success = 0
tests = 0
case_samples = 10
test_data = []
done = False
size = (width, height) = (850,480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (25,255,255)

bacteria = pygame.sprite.Group()
doctor = pygame.sprite.Group()


def proccess_data():
    x = []
    y = []
    for row in test_data:
        if row[-1] >= 75:
            x.append(row[2])
            y.append(row[0])
        fig = plt.figure()
        plt.scatter(x, y)
        plt.title('Doctors needed to prevent an outbreak\n started by just 5 bacteria')
        plt.xlabel('split time (refreshes')
        plt.ylabel('doctors needed')
        fig.savefig('data.png')

def init():
    global round_over
    doctor.empty()
    bacteria.empty()
    round_over = False
    for i in range(bac_num):
        bacteria.add(virus((random.randint(50, width-50), random.randint(50, height-50)), split_time))
    for i in range(doc_num):
        doctor.add(Doctor((random.randint(50, width - 50), random.randint(50, height - 50))))
    global check
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            check = True

def timeout():
    for i in range(300):
        clock.tick(60)
        process_events()

def end():
    global tests, success, doc_num, split_time, done
    timeout()
    tests += 1
    if tests >= case_samples:
        test_data.append([doc_num, bac_num, split_time, tests, success/tests *100])
        print(test_data[-1])
        if test_data[-1][-1] == 0:
            doc_num += 2
        elif test_data[-1][-1] <= 75:
            doc_num += 1
        else:
            split_time = round(split_time*0.9)
            if split_time < 10:
                done = True
        tests = 0
    init()




def process_events():
    global check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check = True
            done = True


def main():
    global round_over, success
    init()
    while not done:
        clock.tick(60)
        process_events()
        if len(bacteria) > bac_num*split_time:
            text = font.render("You were beaten", True, (255,0,0))
            text.rect = text.get_rect()
        elif len(bacteria) == 0:
            text = font.render("You win!", True,(255,0,0))
            text_rect = text.get_rect()
            success += 1
            round_over = True
        else:
            doctor.update()
            bacteria.update()
            pygame.sprite.groupcollide(doctor, bacteria, False, True)
            text = font.render("bacteria count: {}".format(len(bacteria)), True, (255,0,0))
            text_rect = text.get_rect()
        screen.fill(color)
        doctor.draw(screen)
        bacteria.draw(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()
        proccess_data()
        if round_over:
            end()

if __name__ == "__main__":
    main()