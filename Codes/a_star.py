

# graph = {
#     'A': [('B', 75), ('C', 118), ('E', 140)],
#     'B': [],
#     'C': [('D', 111)],
#     'D': [],
#     'E': [('G', 80), ('F', 99)],
#     'F': [('I', 211)],
#     'G': [('H', 97)],
#     'H': [('I', 101)],
#     'I': []
# }

# heuristic = {
#     'A': 366,
#     'B': 374,
#     'C': 329,
#     'D': 244,
#     'E': 253,
#     'F': 178,
#     'G': 193,
#     'H': 98,
#     'I': 0
# }

# import heapq

# def astar(start, goal):
#     li=[] # will be visiting 
#     heapq.heappush(li,(heuristic[start],start) ) # pushes a tuple into the li list - in tuple first will the value the the node name ** otherwise there will be an error
    
#     g = {start:0}
#     parent = {start:None}
    
#     while li:
#         b, a = heapq.heappop(li) # (366,'A')
        
#         print('Visiting:', a)
        
#         if a == goal:
#             path = []
#             while a is not None:   
#               path.append(a)
#               current = parent[a]
#             path.reverse()
#             return path, g[goal]
        
        
#         else:
#             for neighbor, cost in graph[a]:
#                 new_g = g[a]+cost 
                
#                 if neighbor not in g or new_g < g[neighbor]: # saves neighbor if not previosuly visitied or have a less path cost than previously saved one 
                    
#                     g[neighbor] = new_g
#                     parent[neighbor] = a
#                     new_f = new_g + heuristic[neighbor]
#                     heapq.heappush(li, (new_f,neighbor))
#     return None
        
        
# path, cost = astar('A','I')
# print("\nShortest Path:", path)
# print("\nTotal Cost: ", cost)

                
                



##--------------------------

# import heapq
                
# # Main Part            
# n,m = map(int, input().split())
# a,b = map(int, input().split())
# start = (a,b)

# c,d = map(int, input().split())
# end = (c,d)

# maze = []
# for i in range(n):
#     inp = input()
#     maze.append(inp)
    

# def heuristic(position, goal):
#     pa,pb = position
#     gc,gd = goal 
    
#     return abs(pa-gc)+abs(pb-gd)

# def get_neighbors(position, maze, n,m):
#     na,nb = position 
#     moves = [
#         (-1,0),
#         (1,0),
#         (0,-1),
#         (0,1)
#     ]
#     neighbor = []
#     for i, j in moves:
#         ma = na + i
#         mb = nb + j
        
#         if  0 <= ma < n and 0 <= mb < m:
#             if maze[ma][mb] == '0':
#                 neighbor.append((ma,mb))
#     return neighbor

# def astar(start,goal,maze,n,m):
    
#     open_list = []
#     g_cost = {start:0}
#     parent = {start:None}
    
#     h = heuristic(start, goal)
#     f = g_cost+h
    
#     heapq.heappush(open_list,(f,start))
    
#     while open_list:
#         current_f, current = heapq.heappop(open_list)
        
#         for neighbor in get_neighbors(current, maze, n, m):
#             new_g = g_cost[current]+1
            
            
    

def mazeSolver():
    import heapq
                
# Main Part            
    n,m = map(int, input().split())
    a,b = map(int, input().split())
    start = (a,b)

    c,d = map(int, input().split())
    end = (c,d)

    maze = []
    for i in range(n):
       inp = input()
       maze.append(inp)
       
    def heuristic(x,y):
        return abs(x-c) + abs(y-d)
    
    pq = []
    h = heuristic(a,b)
    heapq.heappush(pq,(h,0,a,b,""))
    
    g_cost = {(a,b):0}
    
    dir = [(-1,0,'U'),
           (1,0,'D'),
           (0,-1,'L'),
           (0,1,'R')]
    
    flag = False 
    
    while pq:
        
        f,g,r,c, path = heapq.heappop(pq)
        if (r,c) == (c,d):
            print(c)
            print(path)
            flag = True
            break
        
        if g > g_cost.get((r,c), float("inf")):
            continue
        
        for dr, dc, move in dir:
            nr = r + dr
            nc = c + dc 
            
            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == '0':
                
                new_g = g + 1 
                if new_g < g_cost.get((nr,nc), float("inf")):
                    g_cost[(nr,nc)] = new_g
                    
                    new_f = new_g + heuristic(nr,nc)
                    heapq.heappush(pq, (new_f,new_g,nr,nc,path+move))
                    
        if flag == False:
            print(-1)
            
mazeSolver()      

































