import pygame
from maze.manager import MazeManager
from display import Display

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Maze Runner Visualization')
    clock = pygame.time.Clock()

    # Create a maze manager instance
    maze_manager = MazeManager(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)
    display = Display(screen, maze_manager, CELL_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw the maze
        maze_manager.move_walls()  # This moves the walls in the maze
        display.draw_maze()  # This draws the updated maze onto the screen

        pygame.display.flip()
        clock.tick(10)  # Limit to 10 frames per second for slow wall movement

    pygame.quit()

if __name__ == '__main__':
    main()
