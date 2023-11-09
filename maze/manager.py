from .generator import MazeGenerator
import random

class MazeManager:
    def __init__(self, width, height):
        self.maze_generator = MazeGenerator(width, height)
        self.maze = self.maze_generator.generate_initial_maze()
        self.width = width
        self.height = height

    def get_wall_neighbors(self, x, y):
        neighbors = []
        if x > 1:
            neighbors.append((x - 2, y))
        if x < self.width - 2:
            neighbors.append((x + 2, y))
        if y > 1:
            neighbors.append((x, y - 2))
        if y < self.height - 2:
            neighbors.append((x, y + 2))
        return neighbors

    def move_walls(self):
        # Find all movable walls (i.e., walls that have unoccupied space on opposite sides)
        movable_walls = []
        for y in range(1, self.height, 2):
            for x in range(1, self.width, 2):
                if self.maze[y, x]:
                    neighbors = self.get_wall_neighbors(x, y)
                    for nx, ny in neighbors:
                        if self.maze[ny, nx] == False:
                            movable_walls.append((x, y))
                            break
            self.pathfinder.recalculate_path()#IMPLEMENT LATER


        # Randomly select a wall and move it
        if movable_walls:
            wall_x, wall_y = random.choice(movable_walls)
            neighbors = self.get_wall_neighbors(wall_x, wall_y)
            random.shuffle(neighbors)
            for nx, ny in neighbors:
                if self.maze[ny, nx] == False:
                    # Move the wall
                    self.maze[wall_y, wall_x] = False
                    self.maze[ny, nx] = True
                    break  # Break after moving one wall

    def update_maze(self, screen, cell_size):
        # Logic to redraw only the changed cells in the maze
        for y in range(self.maze.shape[0]):
            for x in range(self.maze.shape[1]):
                color = (0, 0, 0) if self.maze[y, x] else (255, 255, 255)
                pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
