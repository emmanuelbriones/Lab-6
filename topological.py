from graph_al import GraphAL
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def topological_sort(graph):

    all_in_degrees = graph.compute_indegree_every_vertex()
    sort_result = []

    q = Queue()

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.enqueue(i)

    while not q.is_empty():
        u = q.dequeue()

        sort_result.append(u)

        for adj_vertex in graph.vertices_reachable_from(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                q.enqueue(adj_vertex)

    if len(sort_result) != graph.num_vertices():
        return None

    return sort_result