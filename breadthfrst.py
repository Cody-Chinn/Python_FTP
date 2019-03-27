from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u,v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
                  " (starting from vertex 1)")
g.BFS(1)

# graph_two = {
#     "A" : [["B",5]],
#     "B" : [["A",5], ["C",10]],
#     "C" : [["B",10], ["D",5]],
#     "D" : [["C",5], ["E",15], ["G",10]],
#     "E" : [["G",5], ["D",15], ["F",20]],
#     "F" : [["E",20], ["G",5]],
#     "G" : [["F",5], ["E",5], ["D", 10]]
# }
# graph_one = {
#     "A" : [["B",10], ["D",5]],
#     "B" : [["A",10], ["C",5]],
#     "C" : [["B",5], ["D",15]],
#     "D" : [["C",15],["A",5]]
# }
# test_tree = {
#                 "A" : ["B","C"],
#                 "B" : ["D"],
#                 "C" : [],
#                 "D" : []
#             }
