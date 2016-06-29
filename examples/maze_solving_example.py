
class SquareGrid():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = set()

    def is_inside(self, point):
        """ Helper function to know if a given point is inside the Grid.

            :param point: Tuple of two ints
            :return: Boolean
        """
        x, y = point
        return 0 <= x < self.width and 0 <= y < self.height

    def is_wall(self, point):
        """ Helper function to know if a given point is a wall.

            :param point: Tuple of two ints
            :return: Boolean
        """
        return point not in self.walls

    def neighbors(self, point):
        """ Yields the valid neighbours of a given point.

            :param point: Tuple of two ints
            :return: Generator of tuples of ints
        """

        x, y = point
        candidates = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        candidates = filter(self.is_inside, candidates)
        candidates = filter(self.is_wall, candidates)
        yield from candidates

    def _draw_tile(self, point, style, width):
        """ Returns a symbol for the current point given the style dictionary and the drawing width.

            :param point: Tuple of two ints
            :param style: Hash map of the form (int,int) : int or (int,int) : (int,int)
            :param width: Integer representing the width of the graph
            :return: string (character)
        """

        character = "."
        if 'number' in style and point in style['number']:
            character = "%d" % style['number'][point]
        if 'point_to' in style and style['point_to'].get(point, None) is not None:
            (x1, y1) = point
            (x2, y2) = style['point_to'][point]
            if x2 == x1 + 1:
                character = "\u2192"
            if x2 == x1 - 1:
                character = "\u2190"
            if y2 == y1 + 1:
                character = "\u2193"
            if y2 == y1 - 1:
                character = "\u2191"
        if 'start' in style and point == style['start']:
            character = "S"
        if 'goal' in style and point == style['goal']:
            character = "E"
        if 'path' in style and point in style['path']:
            character = "@"
        if point in self.walls:
            character = "#" * width
        return character

    def draw(self, width=2, **style):
        """
        Draws the grid given the style dictionary and the width of the drawin.
        :param style: Hash map of the form (int,int) : int or (int,int) : (int,int)
        :param width: Integer representing the width of the graph
        :return: None
        """
        for y in range(self.height):
            for x in range(self.width):
                print("%%-%ds" % width %
                      self._draw_tile((x, y), style, width), end="")
            print()


class GridWithWeights(SquareGrid):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        """
        Gives the cost of going from from_node to to_node.

        :param from_node: Tuple of two ints
        :param to_node: Tuple of two ints
        :returns: int
        """
        return self.weights.get(to_node, 1)


def from_id_width(point, width):
    """
    Helper function to truncate a int to a point in a grid.

    :param point: integer
    :param width: integer
    :returns: Tuple of two ints
    """
    return (point % width, point // width)

if __name__ == '__main__':

     import a_star.a_star as a_star
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
     frontier = a_star.a_star(graph = graph, start=(1, 4), end=(7, 8))

     # Print the results

     graph.draw(width=5, point_to = frontier.visited, start=(1, 4), goal=(7, 8))

     print()

     graph.draw(width=5, number = frontier.costs, start=(1, 4), goal=(7, 8))
