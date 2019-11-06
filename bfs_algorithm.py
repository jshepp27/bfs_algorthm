"""
Breadth First Search Algorithm, Traversal Graph data-strucutre 

Psuedo Form:
------------
procedure BFS(G,start_v):
    let Q be a queue
    label start_v as discovered
    Q.enqueue(start_v)
    while Q is not empty
        v = Q.dequeue()
        if v is the goal:
            return v
        for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as discovered:
                label w as discovered
                w.parent = v
                Q.enqueue(w) 
Where: The Q queue contains the frontier along which the algorithm is currently searching.

Implementation
--------------
Undirected Graph(V, E) => Graph(10, 11)
Classes: Vertex; Graph 

"""

# Add Vertex and add Neighbours
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbours = list()

        # Initialise distance, discovered
        self.distance = 9999
        self.colour = "black"

    def add_neighbours(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

# Construct Graph: verticies and edges
class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            # Add key
            self.vertices[vertex.name] = vertex 
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                # Add neighbours
                if key == u:
                    value.add_neighbours(v)
                if key == v:
                    value.add_neighbours(u)
            return True
        else:
            return False

    def print_graph(self):
        for key, value in self.vertices.items():
            print(key + str(self.vertices[key].neighbours) + " " + str(self.vertices[key].distance))

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.colour = "red"
        for v in vert.neighbours:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)
        
        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.colour = "red"
    
            for v in node_u.neighbours:
                node_v = self.vertices[v]
                if node_v.colour == "black":
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1


# Driver
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for v in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(v)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

# g.print_graph()
print("\n")
g.bfs(a)
g.print_graph()

