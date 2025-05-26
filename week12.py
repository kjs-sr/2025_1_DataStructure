from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

#깊이 우선
def dfs(g, i, visited):
    visited[i] = True
    print(chr(ord('A')+i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == True and not visited[j]:
            dfs(g, j, visited)

#너비 우선
def bfs(g, i, visited):
    queue = deque([i])
    visited[i] = 1
    #while len(queue) != 0:
    while queue:
        i = queue.popleft()
        print(chr(ord('A') + i), end=' ')
        for j in range(len(graph)):
            if g[i][j] == True and not visited[j]:
                queue.append(j)
                visited[j] = 1

visited_dfs = [False for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 3, visited_dfs)
print()
bfs(graph, 4, visited_bfs)