from collections import deque


def heuristicSolver():
    n,m = map(int,input().split())
    a,b = map (int, input().split())
    
    graph = {}
    for i in range(n):
        x,y = map(int,input().split())
        graph[x] = y 
    
    
    adj = {}
    
    for i in range(1,n+1):
        adj[i] = []
        
    for i in range(m):
        u,v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        
        
    dist = {}
    for i in range(1,n+1):
        dist[i] = float("inf")
        
    
    dist[b] = 0
    queue = deque([b])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in adj[current]:
            if dist[neighbor] == float("inf"):
                true_dist[neighbor] = dist[current]+1
                queue.append(neighbor)
                
    
    inadmissible = []
    for node in range(1,n+1):
        if h[node] > dist[node]:
            inadmissible.append(node)
            
    if not inadmissible:
        print(1)
        
    else:
        print(0)
        if len(inadmissible) == 1:
            print("Here node " + str(inadmissible[0]) + " is inadmissible.")
        else:
            # Build list of string representations for joining
            node_strings = []
            for node in inadmissible[:-1]:
                node_strings.append(str(node))

            nodes_str = ", ".join(node_strings)
            last_node = str(inadmissible[-1])

            print(
                "Here nodes "
                + nodes_str
                + " and "
                + last_node
                + " are inadmissible."
            )
                        
heuristicSolver()       
        
        
    
    
    
        
        
        
        