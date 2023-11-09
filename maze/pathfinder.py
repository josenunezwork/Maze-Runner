import networkx as nx

class Pathfinder:
    def __init__(self, maze_manager):
        self.maze_manager = maze_manager
        self.G = nx.grid_graph(dim=(maze_manager.width, maze_manager.height))
        self.start = (0, 0)  # Entrance 
        self.end = (maze_manager.width - 1, maze_manager.height - 1)  # Exit
        self.path = []

    def recalculate_path(self):
        self.G = self.maze_manager.to_graph()
        # Use Dijkstra's algorithm to find the shortest path
        try:
            self.path = nx.dijkstra_path(self.G, self.start, self.end)
        except nx.NetworkXNoPath:
            print("No path found.")
            self.path = []
