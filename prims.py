INF = 9999999
# number of vertices in graph
N = 5
#creating graph by adjacency matrix method
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]
selected_node = [0, 0, 0, 0, 0]
no_edge = 0
selected_node[0] = True # tells us that we have selected a 1st node i.e node A

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    # n and i are iterator variables for our for loops
    for i in range(N):
        if selected_node[i]:
            for n in range(N):
                if ((not selected_node[n]) and G[i][n]):  
                    # if node not selected and there is an edge
                    if minimum > G[i][n]:
                        minimum = G[i][n]
                        a = i
                        b = n
    
    print(str(a) + "-" + str(b) + ":" + str(G[a][b] ))
    selected_node[b] = True
    no_edge += 1