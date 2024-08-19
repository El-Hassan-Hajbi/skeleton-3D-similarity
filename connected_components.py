def find_connected_components(V, Adj, return_CC=False):
    """
    Finds the number of connected components in an undirected graph.

    Args:
        V: A set of vertices.
        Adj: An adjacency list representation of the graph.

    Returns:
        The number of connected components.
    """

    visited = {}
    component_count = 0

    for v in V:
        visited[v] = False
    CC=[]
    for v in V:
        if not visited[v]:
            Component=[]
            dfs(v, Adj, visited, Component)
            CC.append(Component)
            component_count += 1

    if return_CC : return component_count, CC
    else : return component_count

def dfs(v, Adj, visited, Component):
    """
    Performs depth-first search from vertex v.

    Args:
        v: The starting vertex.
        Adj: An adjacency list representation of the graph.
        visited: A dictionary to track visited vertices.
    """
    visited[v] = True
    Component.append(v)
    for neighbor in Adj[v]:
        if not visited[neighbor]:
            dfs(neighbor, Adj, visited, Component)


import unittest

class TestFindConnectedComponents(unittest.TestCase):
    def test_empty_graph(self):
        V = []
        Adj = {}
        result = find_connected_components(V, Adj)
        self.assertEqual(result, 0)

    def test_single_node(self):
        V = [1]
        Adj = {1: []}
        result = find_connected_components(V, Adj)
        self.assertEqual(result, 1)

    def test_two_connected_nodes(self):
        V = [1, 2]
        Adj = {1: [2], 2: [1]}
        result = find_connected_components(V, Adj)
        self.assertEqual(result, 1)

    def test_two_disconnected_nodes(self):
        V = [1, 2]
        Adj = {1: [], 2: []}
        result = find_connected_components(V, Adj)
        self.assertEqual(result, 2)

    def test_multiple_connected_components(self):
        V = [i for i in range(1,13)]
        Adj = { 1: [2,3,4],
                2: [1,3], 
                3: [1,2,5,6], 
                4: [1,5],
                5: [3,4], 
                6: [3],
                7: [8,9],
                8: [7],
                9: [7],
                10: [11,12],
                11: [10],
                12: [10],
                }
        result, CC = find_connected_components(V, Adj, return_CC=True)
        print(CC)
        self.assertEqual(result, 3)


if __name__ == '__main__':
  unittest.main()