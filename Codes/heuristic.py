from collections import deque



def heuristicSolver():
    n,m = map(int,input().split())

    a,b = map (int, input().split())
    

    heu = {}

    for i in range(n):

        x,y = map(int,input().split())

        heu[x] = y 
    
    
    graph = {}
    

    for i in range(1,n+1):
        graph[i] = []
    for i in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    queue = deque([b])
    
    distance = {b:0}
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if neighbor not in distance:
                distance[neighbor] = distance[current]+1
                
                queue.append(neighbor)
                
                
    inadmissible = []
    
    for node in range(1, n+1):
        if heu[node] > distance[node]:
            inadmissible.append(node)
            
    if len(inadmissible) == 0:
        print(1)
        
    else:
        print(0)
        print(*inadmissible)
        
        
        
        