class kruskal_graph:

    edges = []
    weight = []
    vertices = []

    
    def __init__(self, edge_list, weight):
        self.edges.append(edge_list)
        self.weight.append(weight)


    def kruskal(self):
        self.sort()
        self.make_set()
        count = 0
        i = 0
        while len(self.vertices) > 1:
            if self.find(self.edges[i][0]) != self.find(self.edges[i][1]):
                print((self.edges[i][0], self.edges[i][1]), " edge selected")
                count += 1
                self.union(self.edges[i][0], self.edges[i][1])
            i += 1

    def add(self, edges, weight):
        self.edges.append(edges)
        self.weight.append(weight)
    
    def sort(self):
        if len(self.edges) != len(self.weight):
            return
        for i in range(1, len(self.weight)):
            temp_weight = self.weight[i]
            temp_edge = self.edges[i]
            current = i - 1
            while current >= 0 and temp_weight < self.weight[current]:
                self.weight[current + 1] = self.weight[current]
                self.edges[current + 1] = self.edges[current]
                current -= 1
            self.weight[current + 1] = temp_weight
            self.edges[current + 1] = temp_edge

    
    def make_set(self):
        for i in range(len(self.edges)):
            for j in range(len(self.edges[i])):
                if self.edges[i][j] not in self.vertices:
                    self.vertices.append(self.edges[i][j])

        for k in range(len(self.vertices)):
            self.vertices[k] = [self.vertices[k]]

    
    def find(self, vertex):
        for i in range(len(self.vertices)):
            for element in self.vertices[i]:
                if element == vertex:
                    return i
        return None

    
    def union(self, vertex1, vertex2):
        index1 = self.find(vertex1)
        index2 = self.find(vertex2)
        for element in self.vertices[index2]:
            self.vertices[index1].append(element)
        self.vertices.pop(index2)

    
    def print(self):
        print("Edges:")
        print(self.edges)
        print("Weight for each edge:")
        print(self.weight)