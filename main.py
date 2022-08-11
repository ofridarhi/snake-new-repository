import pygame
import numpy

BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 60

WIDTH, HEIGHT = 800,800
SQUARE_SIZE = WIDTH // 10
ROWS = WIDTH // SQUARE_SIZE
COLS = HEIGHT // SQUARE_SIZE

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("snake")


class Board():
    def create_board(self):
        WIN.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(WIN,BLACK,(row *SQUARE_SIZE,col * SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE),2)



def main():

    board = Board()
    run = True
    clock = pygame.time.Clock()
    board.create_board()
    while run:
        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #if event.type == pygame.KEYUP

if __name__ == '__main__':
    main()