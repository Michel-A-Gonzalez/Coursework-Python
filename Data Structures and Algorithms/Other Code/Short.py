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

                label = self.Vertices[i].get_label ()

                neighbors.append(label)

        return neighbors
 

    # finds the lowest cost to get to every vertex form a
    # given starting vertex, returns a list of costs

    def shortest_path (self, start_vertex):

        nVert = len (self.Vertices)
        
        inf = 1000000

        # creates a table of all other vertecies

        table = []

        for i in range (nVert):

            current = self.Vertices[i].get_label()

            if (current == start_vertex):

                continue

            else:

                table.append(current)

        # creates the memo table

        table_len = len (table)

        # initialize the table 

        memo = [inf for i in range (table_len)]

        # mark the startng vertex as visited

        start_index = self.get_index (start_vertex)

        self.Vertices[start_index].visited = True

        current_vertex = start_vertex

        # uses two costs to keep track of
        # previous weight from the previous vertex
        # to the current vertex and the weight current vertex
        # to the next vertex

        cost = 0

        cost_prev = 0

        for i in range (table_len):

            # gets the next possible vertices

            neighbors = self.get_neighbors (current_vertex)

            # checks that the starting vertex is not
            # a choice when finding neighbors

            if(start_vertex in neighbors):

                neighbors.remove(start_vertex)

            # iterates through each neighbor and gets the
            # weight value 
                
            for j in neighbors:

                weight = self.get_edge_weight (current_vertex, j) + cost_prev

                cost += weight

                m_index = table.index (j)

                if (cost < memo[m_index]):

                    memo[m_index]= cost

                    cost -= weight

                else:

                    cost -= weight

            copy_memo = memo[:]

            for k in table:

                check_idx = self.get_index (k)

                if (self.Vertices[check_idx].visited == True):

                    pop_idx = table.index (k)

                    copy_memo[pop_idx] = inf

                else:

                    continue

            next_value = min(copy_memo)

            cost_prev = next_value

            next_index = copy_memo.index(next_value)

            current_vertex = table[next_index]

            index_current = self.get_index (current_vertex)

            self.Vertices[index_current].visited = True

        return memo
            
                    
def main():

    # create the Graph object

    letters = Graph()

    # read the number of vertices

    line = sys.stdin.readline()

    line = line.strip()

    num_vertices = int(line)

    # read the vertices and insert them into the graph

    for i in range (0, num_vertices):

        line = sys.stdin.readline()

        letter = line.strip()

        letters.add_vertex (letter)

    # read the number of edges

    line = sys.stdin.readline()

    line = line.strip()

    num_edges = int(line)

    # read the edges and insert them into the graph

    for i in range(0, num_edges):

        line = sys.stdin.readline()

        line = line.strip()

        edge = line.split()
        
        start = int (edge[0])

        finish = int (edge [1])

        weight = int (edge[2])

        letters.add_directed_edge (start, finish, weight)

    # print the adjacency matrix

    print("\nAdjacency Matrix")

    for i in range (0, num_vertices):

        for j in range (0, num_vertices):

            print(letters.adjMat[i][j], end = " ")

        print ()

    print()

    # get the starting vertex

    line = sys.stdin.readline()

    start_vertex = line.strip()

    print('list of shortest distances from' + ' ' + "'" + start_vertex + "'")
    print(letters.shortest_path (start_vertex))

main ()
