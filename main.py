import pygame
import numpy

BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 60

WIDTH, HEIGHT = 800,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("snake")

class Board():
    def __init__(self,internal_board):
        self.internal_board = internal_board

    def create_internal_board(self):
        self.internal_board = numpy.zeros((10,10))
        print(self.internal_board)

    def create_visual_board(self):
        for i in range(self.internal_board):
            for j in range(self.internal_board[i]):
                pygame.draw.rect(WIN,BLACK,(HEIGHT /10 * i,HEIGHT /10 * i))

class Snake(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y,color):
        super().__init__()

def main():

    board = Board()
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        WIN.fill(WHITE)
        board.create_internal_board()
        board.create_visual_board()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #if event.type == pygame.KEYUP

if __name__ == '__main__':
    main()