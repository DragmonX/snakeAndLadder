import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 150)

display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snakeandladder')

image = pygame.image.load('download.jpg')
dice1 = pygame.image.load('dice1.png')
dice2 = pygame.image.load('dice2.png')
dice3 = pygame.image.load('dice3.png')
dice4 = pygame.image.load('dice4.png')
dice5 = pygame.image.load('dice5.png')
dice6 = pygame.image.load('dice6.png')
car = pygame.image.load('cars.jpg')
cycle = pygame.image.load('bike.jpg')
bike = pygame.image.load('motor.jpg')
air = pygame.image.load('airplane.jpg')

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)
	
def snake(pos):
    snakepos = []
    i = 1

    while i <= 100:
	    snakepos.append(i)
	    i += 1

    snakepos[15] = 6
    snakepos[46] = 26
    snakepos[48] = 11
    snakepos[61] = 19
    snakepos[63] = 60
    snakepos[86] = 24
    snakepos[92] = 73
    snakepos[94] = 75
    snakepos[97] = 78

    return snakepos[pos - 1]

def ladder(pos):
    ladderpos = []
    i = 1

    while i <= 100:
	    ladderpos.append(i)
	    i += 1
		
    ladderpos[0] = 38
    ladderpos[3] = 14
    ladderpos[8] = 31
    ladderpos[20] = 42
    ladderpos[27] = 84
    ladderpos[35] = 44
    ladderpos[50] = 67
    ladderpos[70] = 91
    ladderpos[79] = 100
	
    return ladderpos[pos - 1]	

def position(pos, turn):
    posi = []
    i = 1
    line = 1	

    x = 0
    y = [520, 532, 544, 556]

    while i <= 100:
	    temp = [] 
	    if x == 520 and line % 2 == 1:
		    y[turn] -= 52
		    line += 1
	    elif x == 52 and line % 2 == 0:
		    y[turn] -= 52
		    line += 1
	    elif line % 2 == 1:
		    x += 52
	    elif line % 2 == 0:
		    x  -= 52

	    temp.append(x)
	    temp.append(y[turn])

	    posi.append(temp)
	    i += 1

    return posi[pos - 1][0], posi[pos - 1][1]


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def message(msg, color, a, b):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [a, b])
	
def button(text, p1, p2, textcolor, x, y, l, b, color):
    pygame.draw.rect(gameDisplay, color, [x, y, l, b])
    message(text, textcolor, p1, p2)

def game():
    players = 2

    lead_x = [0, 0, 0, 0]
    lead_y = [520, 532, 544, 556]
    win = [0, 0, 0, 0]
    nowin = 0
    count = 1
	
    color = [car, bike, cycle, air]

    line = 1
    gameEnd = False
    gameOver = False

    dice = 0
    dis = dice
    con = dice
    pos = [0, 0, 0, 0]
	
    screenescape = False
	
    turn = 0
	
    while not screenescape:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    gameEnd = True
			    screenescape = True
		    if event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_2:
				    players = 2
				    screenescape = True
			    elif event.key == pygame.K_3:
				    players = 3
				    screenescape = True
			    elif event.key == pygame.K_4:
				    players = 4
				    screenescape = True
				
	    gameDisplay.fill(red)
	    message("How many players are there (between 2 and 4)", white, 100, 300)
	    pygame.display.update()

    while not gameEnd:
	
	    mouse = pygame.mouse.get_pos()
	
	    while gameOver == True:
		    mouse = pygame.mouse.get_pos()
			
		    gameDisplay.fill(white)
			
		    if 260 < mouse[0] < 360 and 260 < mouse[1] < 285:
			    button("Play Again", 270, 270, white, 260, 260, 100, 25, red)
			
		    else:
			    button("Play again", 270, 270, white, 260, 260, 100, 25, black)	
			
		    if 260 < mouse[0] < 360 and 315 < mouse[1] < 340:
			    button("Quit", 300, 325, white, 260, 315, 100, 25, red)
			
		    else:
			    button("Quit", 300, 325, white, 260, 315, 100, 25, black)

		    pygame.display.update()

		    for event in pygame.event.get():
			    if event.type == pygame.QUIT:
				    gameOver = False
				    gsmeEnd = True
			    if event.type == pygame.MOUSEBUTTONDOWN: 
				    if 260 < mouse[0] < 360 and 260 < mouse[1] < 285:
					    game()
			    if event.type == pygame.MOUSEBUTTONDOWN: 
				    if 260 < mouse[0] < 360 and 315 < mouse[1] < 340:
					    gameOver = False
					    gameEnd = True	

			
	    con = 0
	    if win[turn] == 0:
		    for event in pygame.event.get():
			    if event.type == pygame.QUIT:
				    gameEnd = True
			    if 260 < mouse[0] < 360 and 0 < mouse[1] < 25:
				    if event.type == pygame.MOUSEBUTTONDOWN:
					    dice = round(random.randrange(1, 7)/1.0) * 1.0
					    dis = dice
					    con = dice
					    if pos[turn] + dice > 100: #checking cheating
						    break

					    while dice > 0: #moving the piece

						    dice -= 1
						    pos[turn] += 1

#displaying in screen

		    gameDisplay.fill(white)
		    gameDisplay.blit(image, (0, 0))

		    
			
			
		    if pos[turn] == 100: #win
			    message("Player %s comes %s" % (turn + 1, count), blue, 250, 300)
			    win[turn] = count
			    nowin += 1	
			    count += 1
			
		    if pos[turn] != 0: #coordinates of piece
			    pos[turn] = ladder(pos[turn])	
			    pos[turn] = snake(pos[turn])
			    lead_x[turn], lead_y[turn] = position(pos[turn], turn)
		
		    j = 0
			
		    while j < players:
			    gameDisplay.blit(color[j], (lead_x[j], lead_y[j]))
			    j += 1

				
		    message("Player %s turn" % (turn + 1), red, 200, 580)	
		    
		    clock.tick(11)


		    if 260 < mouse[0] < 360 and 0 < mouse[1] < 25:
			    button("Roll", 270, 0, white, 260, 0, 100, 25, red)
			
		    else:
			    button("Roll", 270, 0, white, 260, 0, 100, 25, green)
				
		    if(dis == 1):
			    gameDisplay.blit(dice1, (338, 0))
		    elif(dis == 2):
			    gameDisplay.blit(dice2, (338, 0))
		    elif(dis == 3):
			    gameDisplay.blit(dice3, (338, 0))
		    elif(dis == 4):
			    gameDisplay.blit(dice4, (338, 0))
		    elif(dis == 5):
			    gameDisplay.blit(dice5, (338, 0))
		    else:
			    gameDisplay.blit(dice6, (338, 0))
				
		    pygame.display.update()
		
		  
			
	    if (con > 0 and con != 6) or win[turn] != 0:
		    turn = (turn + 1) % players
				
	    if nowin == players - 1:
		    gameOver = True
			
		    
    pygame.quit()
    quit()

#initialising game
game()