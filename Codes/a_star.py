

graph = {
    'A': [('B', 75), ('C', 118), ('E', 140)],
    'B': [],
    'C': [('D', 111)],
    'D': [],
    'E': [('G', 80), ('F', 99)],
    'F': [('I', 211)],
    'G': [('H', 97)],
    'H': [('I', 101)],
    'I': []
}

heuristic = {
    'A': 366,
    'B': 374,
    'C': 329,
    'D': 244,
    'E': 253,
    'F': 178,
    'G': 193,
    'H': 98,
    'I': 0
}

import heapq

def astar(start, goal):
    li=[] # will be visiting 
    heapq.heappush(li,(heuristic[start],start) ) # pushes a tuple into the li list - in tuple first will the value the the node name ** otherwise there will be an error
    
    g = {start:0}
    parent = {start:None}
    
    while li:
        b, a = heapq.heappop(li)
        
        print('Visiting:', a)
        
        if a == goal:
            path = []
            while a is not None:   
              path.append(a)
              current = parent[a]
            path.reverse()
            return path, g[goal]
        
        
        else:
            for neighbor, cost in graph[a]:
                new_g = g[a]+cost 
                
                if neighbor not in g or new_g < g[neighbor]: # saves neighbor if not previosuly visitied or have a less path cost than previously saved one 
                    
                    g[neighbor] = new_g
                    parent[neighbor] = a
                    new_f = new_g + heuristic[neighbor]
                    heapq.heappush(li, (new_f,neighbor))
    return None
        
        
path, cost = astar('A','I')
print("\nShortest Path:", path)
print("\nTotal Cost: ", cost)

                
                

                
            
    

