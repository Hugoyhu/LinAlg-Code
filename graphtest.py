from matrix import Graph

M = [
    [1, -1, 0, 0, 0],
    [1, 0, -1, 0, 0],
    [1, 0, 0, -1, 0],
    [0, 1, -1, 0, 0],
    [0, 1, 0, -1, 0],
    [0, 1, 0, 0, -1],
    [0, 0, 1, -1, 0],
]

x = Graph()
x.list_dataloader(M)
x.inc_graph()

newM = x.inc_matrix_from_graph(x.Graph)

print(x.data == newM)
