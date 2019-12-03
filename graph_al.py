class Edge:
    def __init__(self, item, weight, dest):
        self.item = item
        self.weight = weight
        self.next = dest


class GraphAL:

    
    def __init__(self, vertices, directed, weighted= False):
        self.al = [None] * vertices
        self.directed = directed
        self.weighted = weighted
        self.representation = 'AL'

    
    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)

    
    def add_vertex(self):
        self.al.append(None)
        return len(self.al) - 1  

    def insert_edge(self, src, dest, weight=1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.al[src] = Edge(dest, weight, self.al[src])

        if not self.directed:
            self.al[dest] = Edge(src, weight, self.al[dest])

    
    def delete_edge(self, src, dest):
        self.__delete_edge(src, dest)

        if not self.directed:
            self.__delete_edge(dest, src)

    
    def num_vertices(self):
        return len(self.al)

    
    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        temp = self.al[src]

        while temp is not None:
            reachable_vertices.add(temp.item)
            temp = temp.next

        return reachable_vertices

   
    def vertex_indegree(self, v):
        if not self.is_valid_vertex(v):
            return

        in_degree_count = 0

        for i in range(len(self.al)):
            temp = self.al[i]

            while temp is not None:
                if temp.item == v:
                    in_degree_count += 1
                    break

                temp = temp.next

        return in_degree_count


    def compute_indegree_every_vertex(self):

        indegrees = []
        for i in range(len(self.al)):
            indegrees.append(self.vertex_indegree(i))

        return indegrees

    
