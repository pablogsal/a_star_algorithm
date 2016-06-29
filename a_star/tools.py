
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


