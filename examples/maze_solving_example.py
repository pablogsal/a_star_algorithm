

def from_id_width(point, width):
    """
    Helper function to truncate a int to a point in a grid.

    :param point: integer
    :param width: integer
    :returns: Tuple of two ints
    """
    return (point % width, point // width)

if __name__ == '__main__':

     import a_star
     from a_star.tools import GridWithWeights
     import random

     # Construct a cool wall collection from this aparently arbitraty points.
     WALLS = [from_id_width(point, width=30) for point in [21, 22, 51, 52, 81, 82, 93, 94, 111, 112,
                                                    123, 124, 133, 134, 141, 142, 153, 154, 163,
                                                    164, 171, 172, 173, 174, 175,183, 184, 193,
                                                    194, 201, 202, 203, 204, 205, 213, 214, 223,
                                                    224, 243, 244, 253, 254, 273, 274, 283, 284,
                                                    303, 304, 313, 314, 333, 334, 343, 344, 373,
                                                    374, 403, 404, 433, 434]]

     # Instantiate a grid of 10 x 10
     graph = GridWithWeights(10, 10)

     # Set the walls of the grid
     graph.walls = set(WALLS)

     # Set the weighs of some points in the maze
     graph.weights = {location: random.randint(1,10) for location in [(3, 4), (3, 5), (4, 1), (4, 2),
                                            (4, 3), (4, 4), (4, 5), (4, 6),
                                            (4, 7), (4, 8), (5, 1), (5, 2),
                                            (5, 3), (5, 4), (5, 5), (5, 6),
                                            (5, 7), (5, 8), (6, 2), (6, 3),
                                            (6, 4), (6, 5), (6, 6), (6, 7),
                                            (7, 3), (7, 4), (7, 5)]}

     # Call the A* algorithm and get the frontier
     frontier = a_star.a_star_search(graph = graph, start=(1, 4), end=(7, 8))

     # Print the results

     graph.draw(width=5, point_to = frontier.visited, start=(1, 4), goal=(7, 8))

     print("[costs]")

     costs_so_far = { k: v - a_star.heuristic(k, (7, 8)) for k,v in frontier.costs.items() }
     graph.draw(width=5, number = costs_so_far, start=(1, 4), goal=(7, 8))

     print("[total cost estimates]")

     graph.draw(width=5, number = frontier.costs, start=(1, 4), goal=(7, 8)) #  cost estimates
