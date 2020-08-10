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
        self.vertices[vertex_id] = set()  #Edges.

    def add_edge(self, v1, v2): 
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]  

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()              #create an empty queue and enqueue a starging vertex
        q.enqueue(starting_vertex)
        visited = set()          #create a set so store the visited vertices.
        while q.size() > 0:      #Repeat until queue is empty
            v = q.dequeue()      #dequeue the first vertex
            if v not in visited: #if vertex has not been visited
                print(v)         #debug
                visited.add(v)   #visited
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()              #create an empty stack and push a starting vertex
        s.push(starting_vertex)
        visited = set()          #mark the vertex as visited.
        while s.size() > 0:      #track of visited nodes.
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)   #Mark visited
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

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
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
            visited.add(path[-1])  
            for v in self.get_neighbors(path[-1]):
                new_path = list(path)
                new_path.append(v)
                q.enqueue(new_path)
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        s = Stack()               #starting vertex
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)
        return None  

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
                neighbor_path = self.dfs_recursive(neighbor,
                                                   destination_vertex,
                                                   visited,
                                                   new_path)
                if neighbor_path:
                    return neighbor_path
        return None