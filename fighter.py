import pygame

#test

class Fighter():
 def __init__(self, x, y):
     self.rect = pygame.Rect((x,y,100,200))
     #controls how fast you go up and down(for character jump)
     self.vel_y = 0
     #makes it so that you can jump a certain distance up
     self.jump = False
     #can attack once per key press
     self.attacking = False 
     #defing attack variable
     self.attack_type = 0
     #Defines health
     self.Health = 100
           
        
 #Adding Movement To Characters (rectangles), Dx/Dy records the change in those coordinates
 def Move(self, screen_width,screen_height,surface, target):
     SPEED = 10
     Gravity = 2
     dx = 0
     dy = 0
     
     #get Keypresses that allows keys to move the player
     key = pygame.key.get_pressed()
     
      #Cant preform other movements while attacking        
     if self.attacking == False:
       pass
       #Directional movement
     if key[pygame.K_a]:#Left
       dx = -SPEED
     if key[pygame.K_d]:#Right
        dx = SPEED
      #Jumping   , and statement makes it so that the player can only jump again when on the ground/ no double jump
     if key[pygame.K_w] and self.jump == False:
         self.vel_y = -30
         self.jump = True
      #Attack
     if key[pygame.K_r] or key[pygame.K_t]:
         self.attack(surface, target)
       #Determines whether to use attack 1 or 2
         if key[pygame.K_r]:
           self.attack_type = 1
         if key[pygame.K_t]:
           self.attack_type = 2




   #adds Gravity
     self.vel_y += Gravity
     dy += self.vel_y
        
        
    
      
      
      
     #Ensure player doesnt go off screen
     if self.rect.left + dx < 0:
       dx = -self.rect.left
     if self.rect.right + dx > screen_width:
       dx = screen_width - self.rect.right
     if self.rect.bottom + dy > screen_height - 40:
       self.vel_y = 0
       self.jump = False
       dy = screen_height - 40 - self.rect.bottom
         
         
         
     #Update Player Position
     self.rect.x += dx
     self.rect.y += dy
                            #Key Note: Surface is what makes the rectangles show up
  #Define attack variable       attack starts from the center of player rectangle, width is multiplied by 2 and overlaps half the rectangle
 def attack(self,surface,target):
    self.attacking = True
    attacking_range = pygame.Rect(self.rect.centerx, self.rect.y, 2*self.rect.width, self.rect.height)
    pygame.draw.rect(surface,(0,255,0), attacking_range)
  #basically registers player hitting player
    if attacking_range.colliderect(target.rect):
      target.Health -= 10
      print("hit")
     
  #Visually adds the rectangles(soon to be sprite images)
 def Draw(self, surface):
   pygame.draw.rect(surface, (255,0,0), self.rect)
    
