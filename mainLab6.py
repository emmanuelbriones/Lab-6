from graph_al import GraphAL
from topological import topological_sort
from Kruskal import kruskal_graph

def main():
    print("Topological Sort")
    al = GraphAL(8, True)
    al.insert_edge(0, 1)
    al.insert_edge(1, 7)
    al.insert_edge(1, 3)
    al.insert_edge(3, 2)
    al.insert_edge(2, 5)
    al.insert_edge(2, 4)
    al.insert_edge(2, 6)
    al.insert_edge(4, 7)
    al.insert_edge(6, 4)
    print("Arranged Vertices:")
    for i in range(len(al.al)):
        print(i)
    top_sort = topological_sort(al)
    print("\nAfter Topological Sort: ")
    for j in top_sort:
        print(j)
    print()
    print("Kruskal's Algorithm")
    graph = kruskal_graph([0, 1], 5)
    graph.add([0, 2], 1)
    graph.add([0, 4], 3)
    graph.add([1, 5], 2)
    graph.add([1, 2], 2)
    graph.add([3, 4], 1)
    graph.add([2, 3], 6)
    graph.add([3, 5], 4)
    graph.add([4, 2], 2)
    print("Edges Selected: ")
    graph.kruskal()
    print("The edges and their weights: ")
    graph.print()
    


main()