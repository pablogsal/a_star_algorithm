

import unittest
import a_star
from a_star.tools import GridWithWeights


def backtrack( came_from_dict , start, end):

    current = end
    yield current
    while current != start:
        current = came_from_dict[current]
        yield current

class MazeTests(unittest.TestCase):

    def test_maze_1(self):
        maze = GridWithWeights(4,4)
        walls = [(1,1),(2,2)]
        maze.walls = walls
        weights = {(1,0):20,(3,0) : 2}
        maze.weights = weights
        my_solution = [(3,0),(3,1),(3,2),(3,3),(2,3),(1,3),(1,2),(0,2)]
        end = (3,0)
        start = (0,2)

        # Call the A* algorithm and get the frontier
        frontier = a_star.a_star_search(graph = maze, start=start, end=end)
        solution = list(backtrack(frontier.visited,start,end))
        self.assertTrue( solution == my_solution  )


    def test_2(self):
        maze = GridWithWeights(4,4)
        walls = []
        maze.walls = walls
        weights = {(0,0): 3, (0,1):1, (1,1): 4, (2,1):5,(3,1):1,(0,2): 2, (1,2):3, (2,2):3, (3,2): 2}
        maze.weights = weights

        start = (0,1)
        end = (3,1)

        # Call the A* algorithm and get the frontier
        frontier = a_star.a_star_search(graph = maze, start=start, end=end)
        maze.draw(width=3, point_to = frontier.visited, start=start, goal=end)
        maze.draw(width=3, number = frontier.costs, start=start, goal=end)
        print(frontier.visited)


if __name__ == "__main__":
    unittest.main()
