import collections
import heapq


def heuristic(a, b):
    """
    The heuristic function of the A* algorithm. In this case the Manhattan distance.

    :param a: Tuple of two ints ( Point A)
    :param b: Tuple of two ints ( Point B)
    :returns: integer ( Distance between A nd B )
    """
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


class DijkstraHeap(list):
    """
    An augmented heap for the A* algorithm. This class encapsulated the residual logic of
    the A* algorithm like for example how to manage elements already visited that remain
    in the heap, elements already visited that are not in the heap and from where we came to
    a visited element.

    This class will have three main elements:

        - A heap that will act as a cost queue (self).
        - A visited dict that will act as a visited set and as a mapping of the form  point:came_from
        - A costs dict that will act as a mapping of the form point:cost_so_far
    """
    def __init__(self, first_node = None):
        self.visited = dict()
        self.costs = dict()

        if first_node is not None:
            self.insert(first_node)

    def insert(self, element):
        """
        Insert an element into the Dijkstra Heap.

        :param element: A Node object.
        :return: None
        """

        if element.point not in self.visited:
            heapq.heappush(self,element)

    def pop(self):
        """
        Pop an element from the Dijkstra Heap, adding it to the visited and cost dicts.

        :return: A Node object
        """

        while self and self[0].point in self.visited:
            heapq.heappop(self)

        if self:
            next_elem = heapq.heappop(self)
            self.visited[next_elem.point] = next_elem.came_from
            self.costs[next_elem.point] = next_elem.cost
            return next_elem




Node = collections.namedtuple("Node","cost point came_from")

def a_star(graph, start, end):
    """
    Calculates the shortest path from start to end.

    :param graph: A graph object. The graph object can be anything that implements the following methods:

        graph.neighbors( (x:int, y:int) ) : Iterable( (x:int,y:int), (x:int,y:int), ...)
        graph.cost( (x:int,y:int) ) : int

    :param start: Tuple of two ints representing the starting point.
    :param end: Tuple of two ints representing the ending point.
    :returns: A DijkstraHeap object.

    """

    frontier = DijkstraHeap( Node(0, start, None) )

    while frontier:

        current_node = frontier.pop()

        if not current_node: #or current_node.point == end:
            return frontier

        for neighbor in graph.neighbors( current_node.point ):

            new_cost = ( current_node.cost
                         + graph.cost(current_node.point, neighbor)
                         + heuristic( neighbor, end) )

            new_node = Node(new_cost, neighbor, current_node.point)

            frontier.insert(new_node)

