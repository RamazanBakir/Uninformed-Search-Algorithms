graph = {'S': ['A', 'G'],
         'A': ['S','B', 'C'],
         'B': ['A', 'D'],
         'C': ['A','D','G'],
         'D': ['B','C','G'],
         'G': ['D']}
def bfs_connected_component(graph, start):
    explored = []
    queue = [start]
    levels = {}        
    levels[start]= 0   
    visited= [start]     

    while queue:

        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]
        
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                levels[neighbour]= levels[node]+1
    #print(levels)
    print(explored)
visited = [] 
def dfs(visited, graph, node):
    if node not in visited:
        print (node,end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("DFS \n")
dfs(visited, graph, 'S')
print("\n BFS \n")
ans = bfs_connected_component(graph,'S') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
print(ans)
