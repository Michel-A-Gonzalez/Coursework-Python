#  File: TopoSort.py

#  Description: 

#  Student Name: Michel Gozalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 08/10/2021

#  Date Last Modified: 08/10/2021

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

        index_start = self.get_index (start)

        index_finish = self.get_index (finish)

        self.adjMat[index_start][index_finish] = weight

    # add weighted undirected edge to graph

    def add_undirected_edge (self, start, finish, weight = 1):

        index_start = self.get_index (start)

        index_finish = self.get_index (finish)

        self.adjMat[index_start][index_finish] = weight

        self.adjMat[index_finish][index_start] = weight

    # return an unvisited vertex adjacent to vertex v (index)

    def get_adj_unvisited_vertex (self, v):

        nVert = len (self.Vertices)

        for i in range (nVert):

            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):

                return i

        return -1

    # gets all neighboring vertices from current vertex

    def get_neighbors (self, vertexLabel):

        nVert = len(self.Vertices)

        neighbors = []

        index_v = self.get_index (vertexLabel)

        for i in range (nVert):

            if (self.adjMat[index_v][i] > 0):

                neighbors.append(i)

        return neighbors

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none

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

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
        
    def has_cycle (self):

        nVert = len (self.Vertices)

        # the for loop will let every vertex be a starting point

        for i in range (nVert):

            # creates a list of visited vertecies as well as

            seen_before = []

            start = self.Vertices[i].get_label ()

            seen_before.append(start)

            self.Vertices[i].visited = True

            for j in range (nVert):

                # gets the current index and the index it will go to

                index = self.get_index (start)

                index_un = self.get_adj_unvisited_vertex (index)

                # if the index_un == -1 then the graph has completed a path
                # but it checks if it has neighbors and checks if a letter has
                # been seen before by looking through the seen_before list
                # if it has then it returns True 

                if (index_un == -1):

                    neighbors = self.get_neighbors (start)

                    for k in neighbors:

                        letter_n = self.Vertices[k].get_label()

                        if (letter_n in seen_before):

                            return True

                else:

                    # gets the label of an unvisited adjacent vertex

                    start = self.Vertices[index_un].get_label ()

                    # marks tht adjacent vertex visited

                    self.Vertices[index_un].visited = True

            # resets the graph for the next starting vertex

            for t in range (nVert):

                (self.Vertices[t]).visited = False

        return False
    
    # return a list of vertices after a topological sort
    # this function should not print the list

    def toposort (self):

        # create a Queue

        theQueue = Queue()

        # to sort topologically the program enqueues
        # all vertices with an in_degree of 0, so while
        # the there are vertices the while loop will
        # run

        while len(self.Vertices) != 0:

            # get the current number of vertices

            nVert = len (self.Vertices)

            # create a list of in_degrees
        
            topo_lst = []

            # gets the in_degrees of each vertex

            for i in range (nVert):

                count = 0

                letter = self.Vertices[i].get_label ()

                # this will count all edges going to the
                # current letter by using the adjMat

                for j in range (nVert):

                    if (self.adjMat[j][i] > 0):

                        count += 1

                    else:

                        continue

                # gets the in_degree of all vertices

                topo_lst.append(count)

            # adds all 0 in_degree vertices to the queue
            # and deletes them from the graph

            i = 0

            while (i < len (topo_lst)):

                if (topo_lst[i] == 0):

                    # enqueues all 0 in_degree vertices and begins the
                    # sorting process

                    theQueue.enqueue(self.Vertices[i].get_label())

                    self.delete_vertex (self.Vertices[i].get_label())

                    topo_lst.pop(i)

                else:

                    i += 1
                    
        sorted_lst = []

        while theQueue.is_empty() != True:

            # creates a topo sorted list from the queue

            sorted_lst.append(theQueue.dequeue())

        return sorted_lst
    
def main():
    # create the Graph object

    theGraph = Graph()

    # read the number of vertices

    line = sys.stdin.readline()

    line = line.strip()

    num_vertices = int (line)

    # read the vertices to the list of Vertices

    for i in range (num_vertices):

        line = sys.stdin.readline()

        letter = line.strip()

        theGraph.add_vertex (letter)

    # read the number of edges

    line = sys.stdin.readline()

    line = line.strip()

    num_edges = int (line)

    # read each edge and place it in the adjacency matrix
    for i in range (num_edges):

        line = sys.stdin.readline()

        edge = line.strip()

        edge = edge.split()

        start = (edge[0])

        finish = (edge[1])

        theGraph.add_directed_edge (start, finish)

    # test if a directed graph has a cycle

    if (theGraph.has_cycle()):

        print ("The Graph has a cycle.")

    else:

        print ("The Graph does not have a cycle.")

    # test topological sort

    if (not theGraph.has_cycle()):

        vertex_list = theGraph.toposort()

        print ("\nList of vertices after toposort")

        print (vertex_list)
        
if __name__ == "__main__":

    main()
