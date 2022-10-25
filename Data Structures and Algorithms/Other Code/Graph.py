import sys

class Stack (object):

    def __init__ (self):

        self.stack = []

    def push (self, item):

        self.stack.append (item)

    def pop (self):

        return self.stack.pop()

    def peek (self):

        return self.stack[-1]

    def is_empty (self):

        return (len(self.stack) == 0)

    def size (self):

        return len(self.stack)

class Queue (object):

    def __init__ (self):

        self.queue = []

    def enqueue (self, item):

        self.queue.append (item)

    def dequeue (self):

        return self.queue.pop(0)

    def is_empty (self):

        return (len (self.queue) == 0)

    def size (self):

        return (len(self.queue))

class Vertex (object):

    def __init__ (self, label):

        self.label = label

        self.visited = False

    # determine if a vertex was visited

    def was_visited (self):

        return self.visited

    # determine the label of the vertex

    def get_label (self):

        return self.label

    # string representation of the vertex

    def __str__ (self):

        return str(self.label)

class Graph (object):

    def __init__ (self):

        self.Vertices = []      # a list of Vertex objects

        self.adjMat = []        # adjacency matrix of edges

    # check if a vertex is already in the graph

    def has_vertex (self, label):

        nVert = len (self.Vertices)

        for i in range (0, nVert):

            if (label == (self.Vertices[i]).get_label()):

                return True

        return False

    # given a label get the index of a vertex

    def get_index (self, label):

        nVert = len (self.Vertices)

        for i in range (0, nVert):

            if (label == (self.Vertices[i]).get_label()):

                return i

        return -1

    # add a vertex with a given label to the graph

    def add_vertex (self, label):

        if (not self.has_vertex(label)):

            self.Vertices.append (Vertex(label))

            # add a new column in the adjacency matrix

            nVert = len (self.Vertices)

            for i in range (0, nVert - 1):

                (self.adjMat[i]).append (0)

            # add a new row for the new Vertex

            new_row = []

            for i in range (0, nVert):

                new_row.append (0)

            self.adjMat.append (new_row)

    # add weighted directed edge to graph

    def add_directed_edge (self, start, finish, weight = 1):

        self.adjMat[start][finish] = weight

    # add weighted indirected edge to graph

    def add_undirected_edge (self, start, finish, weight = 1):

        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)

    def get_adj_unvisited_vertex (self, v):

        nVert = len (self.Vertices)

        for i in range (0, nVert):

            if ((self.adjMat[v][i] > 0) and (not(self.Vertices[i].was_visited()))):

                return i

        return -1

    # do the depth first search in a graph from vertex v (index)

    def dfs (self, v):

        #create the Stack

        theStack = Stack()

        # make the vertex v as visited and push it on the stack

        (self.Vertices[v]).visited = True

        print (self.Vertices[v])

        theStack.push (v)

        # visit the other vertices according to depth

        while (not theStack.is_empty()):

            # get an adjacent unvisited vertex

            u = self.get_adj_unvisited_vertex (theStack.peek())

            if (u == -1):

                u = theStack.pop()

            else:

                (self.Vertices[u]).visited = True

                print (self.Vertices[u])

                theStack.push (u)

        # the stack is empty, let us reset the flags

        nVert = len(self.Vertices)

        for i in range (0, nVert):

            (self.Vertices[i]).visited = False

    # do the breadth fisrt search in a graph

    def bfs (self, v):

        return

def main():

    # create the Graph object

    cities = Graph()

    # read the number of vertices

    line = sys.stdin.readline()

    line = line.strip()

    num_vertices = int(line)

    print (num_vertices)

    # read the vertices and insert them into the graph

    for i in range (0, num_vertices):

        line = sys.stdin.readline()

        city = line.strip()

        print (city)

        cities.add_vertex (city)

    # read the number of edges

    line = sys.stdin.readline()

    line = line.strip()

    num_edges = int(line)

    print (num_edges)

    # read the edges and insert them into the graph

    for i in range(0, num_edges):

        line = sys.stdin.readline()

        line = line.strip()

        edge = line.split()

        print (edge)

        start = int (edge[0])

        finish = int (edge [1])

        weight = int (edge[2])

        cities.add_directed_edge (start, finish, weight)

    # print the adjacency matrix

    print("\nAdjacency Matrix")

    for i in range (0, num_vertices):

        for j in range (0, num_vertices):

            print(cities.adjMat[i][j], end = " ")

        print ()

    print()

    # read the starting vertex for dfs and bfs

    line = sys.stdin.readline()

    start_vertex = line.strip()

    print (start_vertex)

    # get the index of the starting vertex

    start_index = cities.get_index (start_vertex)

    print (start_index)

    # do the deapth dirst search

    print("\nDepth First search from " + start_vertex)

    cities.dfs (start_index)

main ()


        
