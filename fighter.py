import pygame

#test

class Fighter():
 def __init__(self, x, y, flip,Data, Spritesheet,animations):
   #loading x and y cordinates on sprite sheets
     self.SizeWidth = Data[0]
     self.SizeHeight = Data[1]
     self.ImageScale = Data[2]
     self.Offset = Data[3]
     self.flip = flip
     #loads sprites frame by frame
     self.animation_list = self.load_sprites(Spritesheet,animations)
     #Determines what player is doing to load correct sprites
     self.action = 0 #0 = idle, 1 = run, 2 = jump, 3 = fall, 4 = attack1, 5 = attack2, 6 = get hit, 7 = death 
     self.frame_index = 0
     self.image = self.animation_list[self.action][self.frame_index]
     self.update_time = pygame.time.get_ticks()
     #healthbar
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
     #Defines health. 
     # Health must be set to length of health bar

     self.Health = 400
           
#load sprites
 def load_sprites (self, Spritesheet,animations):
   animation_list = []
   for y,animation in enumerate(animations):
    temp_img_list = []
    for x in range(animation):
       temp_img = Spritesheet.subsurface (x * self.SizeWidth,y * self.SizeHeight , self.SizeWidth, self.SizeHeight)
       temp_img_list.append(pygame.transform.scale(temp_img, (self.SizeWidth * self.ImageScale, self.SizeHeight * self.ImageScale)))
    animation_list.append(temp_img_list)
    print(animation_list)
   return animation_list
        
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
       
     #ensures players are always facing eachother
     if target.rect.centerx > self.rect.centerx:
       self.flip = False
     else:
       self.flip = True   
         
         
     #Update Player Position
     self.rect.x += dx
     self.rect.y += dy
     
     #Handles Animatiion Updates
 def update(self):
  animation_cooldown = 400
  self.image = self.animation_list [self.action][self.frame_index]
  #check if enough time has passed since last update
  if pygame.time.get_ticks() - self.update_time > animation_cooldown:
     self.frame_index += 1 
     self.update_time = pygame.time.get_ticks()
     #will check if animation has been completed/ will loop again
     if self.frame_index >= len(self.animation_list[self.action]):
       self.frame_index = 0
       
                            #Key Note: Surface is what makes the rectangles show up
  #Define attack variable       attack starts from the center of player rectangle, width is multiplied by 2 and overlaps half the rectangle
 def attack(self,surface,target):
    self.attacking = True
    attacking_range = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2*self.rect.width, self.rect.height)
    pygame.draw.rect(surface,(0,255,0), attacking_range)
  #basically registers player hitting player
    if attacking_range.colliderect(target.rect):
      target.Health -= 10
      
     
  #Visually adds the rectangles(soon to be sprite images)
 def Draw(self, surface):
   img = pygame.transform.flip(self.image, self.flip, False)
   pygame.draw.rect(surface, (255,0,0), self.rect)
   surface.blit(img,(self.rect.x - (self.Offset[0] * self.ImageScale), self.rect.y -(self.Offset[1] * self.ImageScale)))
