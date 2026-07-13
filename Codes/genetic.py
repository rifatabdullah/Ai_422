import math 
import random 

def random_path(no_of_destination):
    random_paths = []
    
    for i in range(5):
        random_pathx = list(range(0, no_of_destination))
        
        random.shuffle(random_pathx)
        #random_pathx =  random_pathx
        random_paths.append(random_pathx)
    return random_paths


x = random_path(5)
print(x)