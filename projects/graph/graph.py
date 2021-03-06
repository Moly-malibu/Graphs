"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices
    mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() #Created edge 
        print(vertex_id)
    def add_edge(self, v1, v2): 
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertice is not found")
        print(v1,v2)
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]  
#QUEUE
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue_start = Queue()              #create an empty queue and enqueue a starging vertex
        queue_start.enqueue(starting_vertex)
        visited = set()          #create a set so store the visited vertices.
        while queue_start.size() > 0:      #Repeat until queue is empty
            first_vertex = queue_start.dequeue()      #dequeue the first vertex
            if first_vertex not in visited: #if vertex has not been visited
                print(first_vertex)         #debug
                visited.add(first_vertex)   #visited
                for next_vertex in self.get_neighbors(first_vertex):
                    queue_start.enqueue(next_vertex)
        print(starting_vertex)
#STACK
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        up_stack = Stack()              #create an empty stack and push a starting vertex
        up_stack.push(starting_vertex)
        visited = set()          #mark the vertex as visited.
        while up_stack.size() > 0:      #track of visited nodes.
            visited_node = up_stack.pop()
            if visited_node not in visited:
                print(visited_node)
                visited.add(visited_node)   #Mark visited
                for next_vertex in self.get_neighbors(visited_node):
                    up_stack.push(next_vertex)
        print(next_vertex)
#VISITED
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for next_vertex in self.get_neighbors(starting_vertex):
            if next_vertex not in visited:
                self.dft_recursive(next_vertex, visited)
        print(next_vertex, visited)
#QUEUE
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue_path = Queue()
        queue_path.enqueue([starting_vertex])
        visited = set()
        while queue_path.size() > 0:
            path = queue_path.dequeue()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
            visited.add(path[-1])  
            for vertex in self.get_neighbors(path[-1]):
                new_path = list(path)
                new_path.append(vertex)
                queue_path.enqueue(new_path)
        return None
        print(new_path)

#STACK
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        depth_first = Stack()               #starting vertex
        depth_first.push([starting_vertex])
        visited = set()
        while depth_first.size() > 0:
            path = depth_first.pop()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for next_vertex in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vertex)
                    depth_first.push(new_path)
        return None  
        print(depth_first)
#VISITED
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        new_path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return new_path
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if neighbor_path:
                    return neighbor_path
        return None
        print(path)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))