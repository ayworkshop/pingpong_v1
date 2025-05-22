import pygame
pygame.init()


#set up the screen 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong")


#set frame rate 
clock = pygame.time.Clock()
FPS = 60 

#set game variables 
GREEN = (136, 231, 136)
WHITE = (255, 255, 255) 
RED = (255, 127, 127)
BLUE = (135, 206, 235)
ORANGE = (255, 153, 28)

class Table:

    def draw(self):
        screen.fill(GREEN)
        for i in range (10, SCREEN_HEIGHT, SCREEN_HEIGHT//20): 
            if i % 2 == 0: 
                pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH//2 - 5, i, 10, SCREEN_HEIGHT//20))




class Paddle: 
    def __init__ (self, x, y, color):
        self.rect = pygame.Rect(0, 0, 20, 100)
        self.rect.centerx = x
        self.rect.centery = y 
        self.color = color 
        self.vel = 10
        self.move_up = False 
        self.move_down = False 
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self): 
        if self.move_up == True and self.rect.top >= 0: 
            self.rect.centery -= self.vel 
        if self.move_down == True and self.rect.bottom <= SCREEN_HEIGHT: 
            self.rect.centery += self.vel 


class Ball: 
    def __init__(self, x, y, x_vel, y_vel): 
        self.x = x
        self.y = y 
        self.x_vel = x_vel 
        self.y_vel = y_vel 
        self.radius = 10
        self.color = ORANGE 
        self.max_vel = 3 

    def draw(self): 
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel 
        self.y += self.y_vel 

    def handle_collision(self): 
        if self.y - self.radius <= 0: 
            self.y_vel *= -1 
        elif self.y + self.radius >= SCREEN_HEIGHT:
            self.y_vel *= -1

        if self.x_vel <= 0:
            if self.y >= left_player.rect.top and self.y <= left_player.rect.bottom:
                if self.x - self.radius <= left_player.rect.right: 
                    self.x_vel *= -1 
                    difference_in_y = left_player.rect.centery - self.y
                    y_vel = difference_in_y / (left_player.rect.height/2) * self.max_vel
                    self.y_vel = -1 * y_vel


        else:
            if self.y >= right_player.rect.top and self.y <= right_player.rect.bottom:
                if self.x + self.radius >= right_player.rect.left: 
                    self.x_vel *= -1 
                    difference_in_y = right_player.rect.centery - self.y
                    y_vel = difference_in_y / (right_player.rect.height/2) * self.max_vel
                    self.y_vel = -1 * y_vel

    def check_ball_reset(self):  
        if self.x < 0 or self.x > SCREEN_WIDTH: 
            pygame.time.delay(1000)
            self.x = SCREEN_WIDTH / 2
            self.y = SCREEN_HEIGHT / 2
            self.x_vel *= -1 
 





#game loop 
run = True 
gametable = Table()
left_player = Paddle(20, SCREEN_HEIGHT//2, RED)
right_player = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT//2, BLUE)
gameball = Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 5, 0)


while run: 

    clock.tick(FPS) 

    left_player.move()
    right_player.move()
    gameball.move()
    gameball.handle_collision()
    gameball.check_ball_reset()

    gametable.draw() 
    left_player.draw() 
    right_player.draw()
    gameball.draw() 


    pygame.display.update()



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False 

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w: 
                left_player.move_up = True
            if event.key == pygame.K_s: 
                left_player.move_down = True        
            if event.key == pygame.K_UP: 
                right_player.move_up = True
            if event.key == pygame.K_DOWN: 
                right_player.move_down = True  
            
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_w: 
                left_player.move_up = False
            if event.key == pygame.K_s: 
                left_player.move_down = False        
            if event.key == pygame.K_UP: 
                right_player.move_up = False 
            if event.key == pygame.K_DOWN: 
                right_player.move_down = False   
    


pygame.quit()

