import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
COLUMNS, ROWS = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

# Game variables
grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
current_piece = None

# Tetrimino class
class Tetrimino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = COLUMNS // 2 - len(shape[0]) // 2
        self.y = 0

    def draw(self, surface):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(surface, self.color, pygame.Rect((self.x + j) * GRID_SIZE, (self.y + i) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Function to spawn new piece
def new_piece():
    global current_piece
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    current_piece = Tetrimino(shape, color)

# Main loop
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
new_piece()
running = True

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_piece.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
