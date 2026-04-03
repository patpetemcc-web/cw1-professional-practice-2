#important: pygame only runs on python versions 3.13 and earlier, pygame may not be installed and can be nstalled with pip commands
import pygame
import os

import random
pygame.init()

#pygame setup
#screen size
X = 1024
Y = 768

#screen creation 
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('spelling game')
scrn = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

#text
base_font = pygame.font.Font(None,64)



#button class
class Button():
    def __init__(self, x, y, image, alt_image):
        self.action = False
        self.current_image = image
        self.image = image
        self.alt_image = alt_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
       
        #handling clicking
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_image = self.alt_image
            if pygame.mouse.get_pressed()[0]==1:
              self.action = True
            else:
              self.action=False
        else:
           self.current_image = self.image

        scrn.blit(self.current_image,(self.rect.x,self.rect.y))
      


#code for start screen
def start_screen():
    #background, always draw first
    background = pygame.image.load("cw1-professional-practice-2-main\graphics\cw1 background.png")
    scrn.blit(background, (0, 0))

    #buttons
    start = pygame.image.load("cw1-professional-practice-2-main\graphics\start-button-1.png")
    start_b = pygame.image.load("cw1-professional-practice-2-main\graphics\start-button-2.png")
    start_button = Button(15,150,start,start_b)
    start_button.draw()
    if start_button.action==True:
       typing_screen(user_text='',current_word='',new_word_needed=True,health=500,game_timer=100)
    #makes the close button work, required for all screens
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          pygame.quit()
          exit()
    
    #updates frame, keeps loop
    pygame.display.update()
    
    start_screen()
    
#screen with actual gameplay
def typing_screen(user_text,current_word,new_word_needed,health,game_timer):
    #generating a new word

    if new_word_needed:
       current_word = random_word()
    
    #background, always draw first
    background = pygame.image.load("cw1-professional-practice-2-main\graphics\cw1 background.png")
    scrn.blit(background, (0, 0))
    
    #creating monster image and health bar and timer
    monster = pygame.image.load("cw1-professional-practice-2-main/graphics/pixil-frame-0.png")
    health_rect = pygame.Rect(50,20,500,60)
    health_rect.w = health
    timer_rect = pygame.Rect(50,10,10,10)
    timer_rect.w = round(game_timer)*4
    #text box handling
    word_rect = pygame.Rect(110,592,850,60)
    input_rect = pygame.Rect(110,672,850,60)
    
    text_box = base_font.render(user_text,False,(0,0,0))
    word_box = base_font.render(current_word,False,(0,0,0))
    
    input_rect.width = max(text_box.get_width()+10,200)
    word_rect.width = word_box.get_width()

    pygame.draw.rect(scrn,(0,255,255),timer_rect)
    pygame.draw.rect(scrn, (255,0,0), health_rect)
    pygame.draw.rect(scrn,(255,255,255),input_rect)
    pygame.draw.rect(scrn,(0,0,0),input_rect,2)
    pygame.draw.rect(scrn,(255,255,255),word_rect)
    pygame.draw.rect(scrn,(0,0,0),word_rect,2)
    scrn.blit(word_box,word_rect)
    scrn.blit(text_box,input_rect)

    #event handling loop
    for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                if input_check(user_text,current_word):
                    new_word_needed=True
                    health-=len(user_text)
                    user_text=''
                    monster=pygame.image.load("cw1-professional-practice-2-main/graphics/pixil-frame-1.png")
                else:
                   user_text=''
            else:
                user_text= user_text+event.unicode
       if event.type == pygame.QUIT:
          pygame.quit()
          exit()

    #win/loss check
    if health <=0:
       monster=pygame.image.load("cw1-professional-practice-2-main\graphics\pixil-frame-2.png")
       scrn.blit(monster,(0,-70))
       win()

    if game_timer <=0:
       scrn.blit(monster,(0,-70))
       lose()
    scrn.blit(monster,(0,-70))
    clock.tick(20)
    game_timer-=1/20
    pygame.display.update()
    typing_screen(user_text,current_word,new_word_needed,health,game_timer)

#win screen
def win():
   winner = pygame.image.load("cw1-professional-practice-2-main\graphics\winner.png")
   scrn.blit(winner,(50,50))
   while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:    
             start_screen()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#lose screen
def lose():
   loser = pygame.image.load("cw1-professional-practice-2-main\graphics\loser.png")
   scrn.blit(loser,(50,50))
   while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:    
             start_screen()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    


def random_word(): #output as string
    return 'apple' #for testing purposes
    
def input_check(wordToCheck,correctWord): #output boolean _

   if wordToCheck.lower() == correctWord.lower(): 
    return True 
   
   else: 
    return False 

    pass

def update_points(currentScore): #output intiger
    pass

def main():
    start_screen()
    
main()