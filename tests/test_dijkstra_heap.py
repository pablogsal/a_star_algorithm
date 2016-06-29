
import unittest
import a_star




class DijkstraHeapTests(unittest.TestCase):

    def test_sorted_unique(self):

        test_data = [a_star.Node(x,x,None) for x in (5,7,3,2,5,3,5,7,2,1,3,1)]
        sorted_unique = sorted(set(test_data))

        # Prepare and insert elements in DijkstraHeap

        frontier = a_star.DijkstraHeap()
        for elem in test_data:
            frontier.insert(elem)

        # get out elements from the DijkstraHeap

        result = []
        while frontier:
            elem = frontier.pop()
            if elem:
                result.append(elem)

        self.assertTrue( result == sorted_unique  )

    def test_delete_repeated(self):

        test_data = [a_star.Node(x,x,None) for x in (1,1,1,1,1,1,1,1,1)]

        # Prepare and insert elements in DijkstraHeap

        frontier = a_star.DijkstraHeap()
        for elem in test_data:
            frontier.insert(elem)

        # get out elements from the DijkstraHeap

        result = []
        while frontier:
            elem = frontier.pop()
            if elem:
                result.append(elem)
        self.assertTrue( result == [a_star.Node(1,1,None)]  )


    def test_came_from(self):

        test_data = [a_star.Node(x,x,x+1) for x in range(10)]

        # Prepare and insert elements in DijkstraHeap

        frontier = a_star.DijkstraHeap()
        for elem in test_data:
            frontier.insert(elem)

        # Drain the DijkstraHeap

        while frontier:
            frontier.pop()

        came_from_dic = { x:x+1 for x in range(10) }


        self.assertTrue( came_from_dic == frontier.visited )

    def test_came_from_unique(self):

        test_data = [a_star.Node(x,x,x+1) for x in [0,1,2,3,2,4,1]]

        # Prepare and insert elements in DijkstraHeap

        frontier = a_star.DijkstraHeap()
        for elem in test_data:
            frontier.insert(elem)

        # Drain the DijkstraHeap

        while frontier:
            frontier.pop()

        came_from_dic = { x:x+1 for x in range(5) }


        self.assertTrue( came_from_dic == frontier.visited )

if __name__ == "__main__":
    unittest.main()
