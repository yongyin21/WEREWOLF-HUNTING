import pygame
import random

class Data:
    def __init__(self):
        # Globalising some values to be used later
        global your_score,score,guess,guess_bool,grass1,grass2,grass3,grass4,grass5,grass6,grass7,grass8
        
        # Importing images
        self.grass= pygame.image.load("assets/bushp.png")
        self.grass=pygame.transform.rotate(pygame.transform.scale(self.grass,(80,80)),0)

        self.wolf= pygame.image.load("assets/wolfp.png")
        self.wolf=pygame.transform.rotate(pygame.transform.scale(self.wolf,(45,45)),0)

        self.heart= pygame.image.load("assets/heart_red.png")
        self.heart=pygame.transform.rotate(pygame.transform.scale(self.heart,(20,20)),0)

        self.heart_e= pygame.image.load("assets/heart2_e.png")
        self.heart_e=pygame.transform.rotate(pygame.transform.scale(self.heart_e,(20,20)),0)
        guess = 0
        guess_bool = True
        # Generating wolf position randomly
        if guess_bool:
            guess = random.randint(1,8)
            guess_bool = False

        # Showing wolf position
        if guess == 1:
            WIN.blit(self.wolf,(118,365))
        elif guess == 2:
            WIN.blit(self.wolf,(218,315))
        elif guess == 3:
            WIN.blit(self.wolf,(318,415))
        elif guess == 4:
            WIN.blit(self.wolf,(418,365))
        elif guess == 5:
            WIN.blit(self.wolf,(518,315))
        elif guess == 6:
            WIN.blit(self.wolf,(618,415))
        elif guess == 7:
            WIN.blit(self.wolf,(718,365))
        elif guess == 8:
            WIN.blit(self.wolf,(818,415))
        # Show bush positon
        if grass1:
            WIN.blit(self.grass,(100,350))
        if grass2:
            WIN.blit(self.grass,(200,300))
        if grass3:
            WIN.blit(self.grass,(300,400))
        if grass4:
            WIN.blit(self.grass,(400,350))
        if grass5:
            WIN.blit(self.grass,(500,300))
        if grass6:
            WIN.blit(self.grass,(600,400))
        if grass7:
            WIN.blit(self.grass,(700,350))
        if grass8:
            WIN.blit(self.grass,(800,400))


        # Text of player
        Player_txt = font30.render('PLAYER :', True, 'black')
        WIN.blit(Player_txt, (60, 7))

        # Text of score
        score_txt = font30.render('Score : '+str(your_score), True, 'green')
        WIN.blit(score_txt, (350, 7))

        # Text of highscore
        score_txt = font30.render('Highscore : '+str(score), True, 'red')
        WIN.blit(score_txt, (350, 545))


        # Showing hearts
        if player_hearts>=1:
            WIN.blit(self.heart,(200,10))
        if player_hearts>=2:
            WIN.blit(self.heart,(230,10))
        if player_hearts==3:
            WIN.blit(self.heart,(260,10))
        
        # Empty hearts
        WIN.blit(self.heart_e,(200,10))
        WIN.blit(self.heart_e,(230,10))
        WIN.blit(self.heart_e,(260,10))

        # Wolf text
        Player_txt = font30.render('WOLF :', True, 'black')
        WIN.blit(Player_txt, (530, 7))

        # Showing wolf hearts
        if wolf_hearts>=1:
            WIN.blit(self.heart,(650,10))
        if wolf_hearts>=2:
            WIN.blit(self.heart,(680,10))
        if wolf_hearts==3:
            WIN.blit(self.heart,(710,10))

        # Empty hearts
        WIN.blit(self.heart_e,(650,10))
        WIN.blit(self.heart_e,(680,10))
        WIN.blit(self.heart_e,(710,10))

        # Making the bush appear and disappear
        if not grass1 or not grass2 or not grass3 or not grass4 or not grass5 or not grass6 or not grass7 or not grass8:
            grass1 = True
            grass2 = True
            grass3 = True
            grass4 = True
            grass5 = True
            grass6 = True
            grass7 = True
            grass8 = True
           
            pygame.display.update()
            time.sleep(1)
            guess_bool = True