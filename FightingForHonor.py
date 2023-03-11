import pygame
from fighter import Fighter
pygame.init()

#creates Game Window
Screen_Width = 1000
Screen_Height = 600

Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("Fighting For Honor")


#Set Framerate
clock = pygame.time.Clock()
FPS = 60

#Define colors
Red = (255,0,0)
Yellow = (255,255,0)
White = (255,255,255)

#load BackGround Image
background = pygame.image.load("GateJapan.jpg").convert_alpha()
#Function that displays background
def display_Bg():
 scaledBG = pygame.transform.scale(background,(Screen_Width, Screen_Height))
 Screen.blit(scaledBG,(0,0))
    
  
#Function for drawing the health bars
# bottom bar is character's health in yellow. length of color has to be set to character's health value in order for character to take damage
def Health_Bar(Health, x, y): 
  pygame.draw.rect (Screen, Red, (x,y, 400,30))
  pygame.draw.rect (Screen, Yellow, (x,y, Health,30))
  
    
#Creates both Characters
Ronin = Fighter(200,360)
Samurai = Fighter(700,360)

#gameloop
run = True
while run:
    
 clock.tick(FPS)
    
 #Display Background
 display_Bg()
    
 #Show Health Bars
 Health_Bar(Ronin.Health, 20,20)
 Health_Bar(Samurai.Health, 580,20)
    
 #Move the fighters
 Ronin.Move(Screen_Width, Screen_Height,Screen, Samurai)
 ##################Samurai.Move()
    
 #Draw Fighters
 Ronin.Draw(Screen)
 Samurai.Draw(Screen)
 #event handler
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         run = False
            
 #Updates display for background
 pygame.display.update()


#exit pygame
pygame.quit()

