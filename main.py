import pygame
import numpy
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

FPS = 120

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 10
ROWS = WIDTH // SQUARE_SIZE
COLS = HEIGHT // SQUARE_SIZE
PADDING = 2

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")

DIRECTION_DICT = dict()
DIRECTION_DICT['right'] = (1, 0)
DIRECTION_DICT['left'] = (-1, 0)
DIRECTION_DICT['up'] = (0, -1)
DIRECTION_DICT['down'] = (0, 1)


class Board:
    def __init__(self):
        self.clear_board()

    def clear_board(self):
        WIN.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(WIN, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), PADDING)


class Snake:
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.x_vel = SQUARE_SIZE
        self.y_vel = SQUARE_SIZE
        self.color = color
        self.width = width
        self.height = height
        self.direction = DIRECTION_DICT['right']
        self.snake_cells = [(self.x, self.y)]

    # def eat(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_a]:
    #         last_cell = self.snake_parts[-1]
    def update_snake(self):
        snake_cells = []
        direction_x, direction_y = self.direction
        for cell_x, cell_y in self.snake_cells:
            new_cell = (cell_x + direction_x * self.x_vel, cell_y + direction_y * self.y_vel)
            snake_cells.append(new_cell)
        self.snake_cells = snake_cells

    def delete_last(self):
        last_snake_cell = self.snake_cells[-1]
        pygame.draw.rect(WIN, WHITE, (last_snake_cell[0], last_snake_cell[1], self.width, self.height))

    def draw(self):
        self.delete_last()
        self.update_snake()

        for cell_x, cell_y in self.snake_cells:
            pygame.draw.rect(WIN, self.color, (cell_x, cell_y, self.width, self.height))
        pygame.display.update()

    def change_snake_direction(self):
        time.sleep(0.1)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = DIRECTION_DICT['up']
        elif keys[pygame.K_DOWN]:
            self.direction = DIRECTION_DICT['down']
        elif keys[pygame.K_LEFT]:
            self.direction = DIRECTION_DICT['left']
        elif keys[pygame.K_RIGHT]:
            self.direction = DIRECTION_DICT['right']

    def get_head_x_y(self):
        x = self.x
        y = self.y
        return x, y


def main():
    snake = Snake(SQUARE_SIZE * 5 + PADDING, SQUARE_SIZE * 5 + PADDING, GREEN, SQUARE_SIZE - PADDING * 2,
                  SQUARE_SIZE - PADDING * 2)
    board = Board()
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        snake.change_snake_direction()
        snake.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # if event.type == pygame.KEYUP


if __name__ == '__main__':
    main()
