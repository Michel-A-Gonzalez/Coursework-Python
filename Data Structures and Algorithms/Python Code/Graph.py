#  File: Graph.py

#  Description: The purpose of this program is to familiarize
#               ourselves with graphs by creating different functions
#               for the Graph class and implementing the depth first and
#               bread first searching algorithms

#  Student Name: Michel Gonzalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86110

#  Date Created: 08/08/2021

#  Date Last Modified: 08/08/2021

# Most of these funstions were discussed in class
# and code was provided during our lecture on graphs

import sys

class Stack (object):
    
    def __init__ (self):

        self.stack = []

    # add an item to the top of the stack
    
    def push (self, item):

        self.stack.append (item)

    # remove an item from the top of the stack
    
    def pop (self):

        return self.stack.pop()

    # check the item on the top of the stack

    def peek (self):

        return self.stack[-1]

    # check if the stack if empty

    def is_empty (self):

        return (len (self.stack) == 0)

    # return the number of elements in the stack

    def size (self):

        return (len (self.stack))

class Queue (object):

    def __init__ (self):

        self.queue = []

    # add an item to the end of the queue

    def enqueue (self, item):

        self.queue.append (item)

    # remove an item from the beginning of the queue

    def dequeue (self):

        return (self.queue.pop(0))

    # check if the queue is empty

    def is_empty (self):

        return (len (self.queue) == 0)

    # return the size of the queue

    def size (self):

        return (len (self.queue))

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

        return str (self.label)

class Graph (object):

    def __init__ (self):

        self.Vertices = []

        self.adjMat = []

    # check if a vertex is already in the graph

    def has_vertex (self, label):

        nVert = len (self.Vertices)

        for i in range (nVert):

            if (label == (self.Vertices[i]).get_label()):

                return True

        return False

    # given the label get the index of a vertex

    def get_index (self, label):

        nVert = len (self.Vertices)

        for i in range (nVert):

            if (label == (self.Vertices[i]).get_label()):

                return i

        return -1

    # add a Vertex with a given label to the graph

    def add_vertex (self, label):

        if (self.has_vertex (label)):

              return

        # add vertex to the list of vertices

        self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix

        nVert = len (self.Vertices)

        for i in range (nVert - 1):

          (self.adjMat[i]).append (0)

        # add a new row for the new vertex

        new_row = []

        for i in range (nVert):

          new_row.append (0)

        self.adjMat.append (new_row)

    # add weighted directed edge to graph

    def add_directed_edge (self, start, finish, weight = 1):

        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph

    def add_undirected_edge (self, start, finish, weight = 1):

        self.adjMat[start][finish] = weight

        self.adjMat[finish][start] = weight

    # get edge weight between two vertices
    # return -1 if edge does not exist
    
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):

        index_from = self.get_index (fromVertexLabel)

        index_to = self.get_index (toVertexLabel)

        # checks if the edge exists

        if (self.adjMat[index_from][index_to] > 0):

            return self.adjMat[index_from][index_to]

        else:

            return -1 

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    
    def get_neighbors (self, vertexLabel):

        nVert = len(self.Vertices)

        neighbors = []

        index_v = self.get_index (vertexLabel)

        for i in range (nVert):

            if (self.adjMat[index_v][i] > 0):

                neighbors.append(i)

        return neighbors

    # return an index to an unvisited vertex adjacent to vertex v (index)

    def get_adj_unvisited_vertex (self, v):

        nVert = len (self.Vertices)

        for i in range (nVert):

            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):

                return i

        return -1

    # get a copy of the list of Vertex objects

    def get_vertices (self):

        copy_lst = self.Vertecies

        return copy_lst

    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    
    def delete_edge (self, fromVertexLabel, toVertexLabel):

        index_from = self.get_index (fromVertexLabel)

        index_to = self.get_index (toVertexLabel)

        from_weight = self.get_edge_weight (fromVertexLabel, toVertexLabel)

        to_weight = self.get_edge_weight (toVertexLabel, fromVertexLabel)

        # checks if it is undirected

        if (from_weight == to_weight):

            self.adjMat[index_from][index_to] = 0

            self.adjMat[index_to][index_from] = 0

        # the edge is directed

        else:

            self.adjMat[index_from][index_to] = 0

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):

        nVert = len (self.Vertices)

        # deleting the edges

        # deletes the column of edges on the
        # adjacent matrix

        v_index = self.get_index(vertexLabel)

        nVert = len (self.Vertices)

        i = 0

        while i < nVert:

            self.adjMat[i].pop(v_index)

            i += 1

        # deletes the row of edeges on the
        # adjacent matrix

        self.adjMat.pop(v_index)

        # delets the vertix from the
        # vertecies list

        self.Vertices.pop(v_index)
         

    # do a depth first search in a graph

    def dfs (self, v):

        # create the Stack

        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack

        (self.Vertices[v]).visited = True

        print (self.Vertices[v])

        theStack.push (v)

        # visit all the other vertices according to depth

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

        nVert = len (self.Vertices)

        for i in range (nVert):

            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    
    def bfs (self, v):

        # create a Queue

        theQueue = Queue()

        # add vertex v into the Queue

        theQueue.enqueue(v)

        # mark v as visited

        self.Vertices[v].visited = True

        # create a travered list

        traversed_lst = []

        # while the queue is not empty
        # dequeue a vertex from the queue
        # and add it into a list of traversed
        # vertices

        while (theQueue.is_empty() != True):

            index = theQueue.dequeue()

            vertex = self.Vertices[index]

            traversed_lst.append(vertex)

            # creates neighbors list

            neighbors = self.get_neighbors(vertex.get_label())

            # for each neighbor of u
            # if it has not been visited
            # add that neighbor into the
            # queue and mark that neighbor
            # as visited

            for i in neighbors:

                if (self.Vertices[i].visited == False):

                    theQueue.enqueue(i)

                    self.Vertices[i].visited = True

                else:

                    continue

        # the queue is empty, let us reset the flags

        nVert = len (self.Vertices)

        for i in range (nVert):

            (self.Vertices[i]).visited = False

        for i in range (len(traversed_lst)):

            print(traversed_lst[i].get_label())

def main():

    # create the Graph object

    cities = Graph()

    # read the number of vertices

    line = sys.stdin.readline()

    line = line.strip()

    num_vertices = int (line)

    # read the vertices to the list of Vertices

    for i in range (num_vertices):

        line = sys.stdin.readline()

        city = line.strip()

        cities.add_vertex (city)

    print (len(cities.adjMat))

    # read the number of edges

    line = sys.stdin.readline()

    line = line.strip()

    num_edges = int (line)

  # read each edge and place it in the adjacency matrix

    for i in range (num_edges):

        line = sys.stdin.readline()

        edge = line.strip()

        edge = edge.split()

        start = int (edge[0])

        finish = int (edge[1])

        weight = int (edge[2])

        cities.add_directed_edge (start, finish, weight)

    # read the starting vertex for dfs and bfs

    line = sys.stdin.readline()

    start_vertex = line.strip()

    # get the index of the starting vertex

    start_index = cities.get_index (start_vertex)

    # get the from_label and to_label

    line = sys.stdin.readline()

    lst = line.split()

    from_label = lst[0].strip()

    to_label = lst[1].strip()

    # get the vertex to delete

    line = sys.stdin.readline()

    deleted_vertex = line.strip()

    print (cities.adjMat)
    
    # test depth first search

    print ('Depth First Search')

    cities.dfs (start_index)

    print ()

    # test breadth first search

    print ('Breadth First Search')

    cities.bfs (start_index)

    print()

    # test deletion of an edge

    print ('Deletion of an edge')

    cities.delete_edge (from_label, to_label)

    print()

    print('Adjacency Matrix')

    for i in range (0, num_vertices):

        for j in range (0, num_vertices):

            # for formating the last number has
            # no trailing spaces

            if (j == num_vertices - 1):

                print (cities.adjMat[i][j], end = '')

            else:

                print(cities.adjMat[i][j], end = " ")

        print ()

    print()

    # test deletion of a vertex

    print ('Deletion of a vertex')

    cities.delete_vertex (deleted_vertex)

    print()

    # print the list to show the
    # city was deleted

    print('List of Vertices')

    for i in range (num_vertices - 1):

        print(cities.Vertices[i])

    print()

    # since a city was deleted
    # the number of vertices goes down
    # by one

    num_vertices -= 1

    print('Adjacency Matrix')

    for i in range (0, num_vertices):

        for j in range (0, num_vertices):

            # for formating the last number has
            # no trailing spaces

            if (j == num_vertices - 1):

                print (cities.adjMat[i][j], end = '')

            else:

                print(cities.adjMat[i][j], end = " ")

        print ()

    print()

if __name__ == "__main__":

    main()
