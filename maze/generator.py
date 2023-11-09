# maze/generator.py
import numpy as np
import random

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_initial_maze(self):
        # Using a simple Randomized Prim's algorithm for maze generation
        maze = np.zeros((self.height, self.width), dtype=bool)
        
        # Start with a grid full of walls
        maze[::2, ::2] = True
        walls = set()

        # Random starting point
        x, y = random.randrange(2, self.width - 1, 2), random.randrange(2, self.height - 1, 2)
        maze[y, x] = True
        
        # Add walls to the list
        if x > 2:
            walls.add((x - 1, y))
        if x < self.width - 2:
            walls.add((x + 1, y))
        if y > 2:
            walls.add((x, y - 1))
        if y < self.height - 2:
            walls.add((x, y + 1))

        while walls:
            wall = walls.pop()
            wx, wy = wall

            # Check if the wall divides two cells
            px, py = (wx // 2) * 2, (wy // 2) * 2
            opposite = (wx + (px - wx) * 2, wy + (py - wy) * 2)

            if maze[opposite] == False:
                maze[wy, wx] = True
                maze[opposite] = True

                # Add neighboring walls of the cell
                if opposite[0] > 2:
                    walls.add((opposite[0] - 1, opposite[1]))
                if opposite[0] < self.width - 2:
                    walls.add((opposite[0] + 1, opposite[1]))
                if opposite[1] > 2:
                    walls.add((opposite[0], opposite[1] - 1))
                if opposite[1] < self.height - 2:
                    walls.add((opposite[0], opposite[1] + 1))

        return maze
