import pygame
from pygame import mixer
import time
import os
import random

from pygame.constants import KEYDOWN, K_SPACE

FPS = 60
WIDTH=1600
HEIGHT=800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
Turqyoise = (48,213,200)
BLACK = (0,0,0)
GREEN = (0,128,0)
LGREEN = (124,252,0)


pygame.mixer.init()
music_69 = mixer.Sound('music_69.wav')
music_x = mixer.Sound('xxx.wav')


CHARATER_IMG_69 = pygame.image.load(os.path.join('images','rapper69.png'))
body_69 = pygame.image.load(os.path.join('images','69_bod.png'))
part_69 = pygame.image.load(os.path.join('images','69_part.png'))

CHARATER_IMG_X = pygame.image.load(os.path.join('images','tenta.png'))
body_x = pygame.image.load(os.path.join('images','x_bod.png'))
part_x = pygame.image.load(os.path.join('images','x_part.png'))

CHARATER_IMG_JW = pygame.image.load(os.path.join('images','jw_complete.png'))
body_jw = pygame.image.load(os.path.join('images','jw_bod.png'))
part_jw = pygame.image.load(os.path.join('images','jw_part.png'))

CHARATER_IMG_69_RESIZE = pygame.transform.scale(CHARATER_IMG_69, (500,800))
CHARATER_IMG_X_RESIZE = pygame.transform.scale(CHARATER_IMG_X, (500,700))
CHARATER_IMG_JW_RESIZE = pygame.transform.scale(CHARATER_IMG_JW, (500,700))

BG_IMG = pygame.image.load(os.path.join('images', 'bg_img.png'))
BG_IMG_RESIZE = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

pygame.font.init()
font = pygame.font.SysFont('calibri', 40)
font2 = pygame.font.SysFont('calibri', 60)
startText = font.render("Play", True,(255,255,255))
SQUADTEXT = font2.render("GANG GANG", True,(255,255,255))
SELECTTEXT = font2.render("PICK ONE", True,(255,255,255))
PRESS_ENTER=font2.render("PRESS ENTER TO CONTINUE", True, (255,255,255))

mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()



def start_screen():
    intro = True
    pygame.mixer.music.load("kid.wav")
    pygame.mixer.music.play(-1)


    while intro:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        if 750+100>mouse[0]>550 and 700+50>mouse[1]>700:
            pygame.draw.rect(WIN, LGREEN, (750,700,100,50))
            if click[0]==1:
                characterSelect()
        else:
            pygame.draw.rect(WIN, GREEN, (750,700,100,50))


        WIN.blit(SQUADTEXT, (600, 100))
        WIN.blit(startText, (770,705))
        pygame.display.update()
        WIN.blit(BG_IMG_RESIZE,(0,0))




def game_69():
    head_speed = 2
    pygame.mixer.music.stop()
    pygame.mixer.music.load("music_69.wav")
    pygame.mixer.music.play(-1)

    head_box=pygame.Rect(0,190,80,150)
    loop = True
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE and 820<=head_box.x<=900:
                    game_69Winner()

        if head_box.x > WIDTH:
            head_box.x=-10

        head_box.x += head_speed
        WIN.blit(body_69,(WIDTH/2.5,HEIGHT/6))
        WIN.blit(part_69, head_box)
        pygame.display.update()
        WIN.fill(BLACK)

    pygame.quit()



def game_X():
    head_speed = 20
    pygame.mixer.music.stop()
    pygame.mixer.music.load("xxx.wav")
    pygame.mixer.music.play(-1)

    head_box=pygame.Rect(0,435,120,190)
    loop = True
    

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE and 825<=head_box.x<=950:
                    game_XWinner()
    
        if head_box.x > WIDTH:
            head_box.x=-10

        head_box.x += head_speed
        WIN.blit(body_x,(WIDTH/2.5,HEIGHT/6))
        #pygame.draw.rect(WIN, Turqyoise, head_box, 1)
        WIN.blit(part_x, head_box)
        pygame.display.update()
        WIN.fill(BLACK)


    pygame.quit()



def game_JW():
    head_speed = 10
    pygame.mixer.music.stop()
    pygame.mixer.music.load("jw.wav")
    pygame.mixer.music.play(-1)

    head_box=pygame.Rect(0,150,250,250)
    loop = True
    

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE and 660<=head_box.x<=810:
                    game_JWWinner()
        if head_box.x > WIDTH:
            head_box.x=-10

        head_box.x += head_speed
        WIN.blit(body_jw,(400,HEIGHT/6))
        WIN.blit(part_jw, head_box)
        pygame.display.update()
        WIN.fill(BLACK)

    pygame.quit()




def game_69Winner():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            characterSelect()            
        WIN.blit(PRESS_ENTER, (WIDTH/2, 10))
        WIN.blit(CHARATER_IMG_69_RESIZE,(WIDTH/2.5,HEIGHT/6))
        pygame.display.update()

    pygame.quit()




def game_XWinner():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            characterSelect()           
        WIN.blit(PRESS_ENTER, (WIDTH/2, 10))
        WIN.blit(CHARATER_IMG_X_RESIZE,(WIDTH/2.5,HEIGHT/6))
        pygame.display.update()

    pygame.quit()



def game_JWWinner():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            characterSelect()            
        WIN.blit(PRESS_ENTER, (WIDTH/2, 10))
        WIN.blit(CHARATER_IMG_JW_RESIZE,(WIDTH/2.5,HEIGHT/6))
        pygame.display.update()

    pygame.quit()





def characterSelect():

    run = True
    clock = pygame.time.Clock()
    box_69 = pygame.Rect(90,320,400,500)
    box_x = pygame.Rect(650,200,400,700)
    box_jw = pygame.Rect(1150,290,300,550)

    while run:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if 90+400>mouse[0]>90 and 320+500>mouse[1]>320:
            pygame.draw.rect(WIN, LGREEN, box_69,4)
            if click[0]==1:
                game_69()
        if 700+300>mouse[0]>700 and 200+500>mouse[1]>200:
            pygame.draw.rect(WIN, LGREEN, box_x,4)
            if click[0]==1:
                game_X()
        if 1200+200>mouse[0]>1200 and 290+550>mouse[1]>290:
            pygame.draw.rect(WIN, LGREEN, box_jw,4)
            if click[0]==1:
                game_JW()



        WIN.blit(CHARATER_IMG_69_RESIZE, (50,300))
        WIN.blit(CHARATER_IMG_X_RESIZE, (600,200))  
        WIN.blit(CHARATER_IMG_JW_RESIZE, (1000,200))
        WIN.blit(SELECTTEXT,(720,100))
        pygame.display.update()
        WIN.fill(BLACK)


    pygame.quit()




if __name__ == "__main__":
    start_screen()