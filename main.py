import pygame
import numpy
import time

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
FPS = 60

WIDTH, HEIGHT = 800,800
SQUARE_SIZE = WIDTH // 10
ROWS = WIDTH // SQUARE_SIZE
COLS = HEIGHT // SQUARE_SIZE
PADDING = 2

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("snake")


class Board():
    def create_board(self):
        WIN.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(WIN,BLACK,(row *SQUARE_SIZE,col * SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE),PADDING)

class Snake:
    def __init__(self,x,y,color,width,height,):
        self.x = x
        self.y = y
        self.x_vel = SQUARE_SIZE
        self.y_vel = SQUARE_SIZE
        self.color = color
        self.width = width
        self.height = height
        self.squars = []

    def create_snake_head(self):
        pygame.draw.rect(WIN,self.color,(self.x,self.y,self.width,self.height))
        pygame.display.update()

    def move_snake_head(self):
        time.sleep(0.5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))
            self.y -= self.y_vel
        if keys[pygame.K_DOWN]:
            pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))
            self.y += self.y_vel
        if keys[pygame.K_LEFT]:
            pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))
            self.x -= self.x_vel
        if keys[pygame.K_RIGHT]:
            pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))
            self.x += self.x_vel
        pygame.display.update()


def main():
    snake = Snake(SQUARE_SIZE * 5 +PADDING, SQUARE_SIZE * 5 +PADDING,GREEN,SQUARE_SIZE -PADDING*2,SQUARE_SIZE -PADDING*2)
    board = Board()
    run = True
    clock = pygame.time.Clock()
    board.create_board()
    while run:
        clock.tick(FPS)
        snake.create_snake_head()
        snake.move_snake_head()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #if event.type == pygame.KEYUP

if __name__ == '__main__':
    main()