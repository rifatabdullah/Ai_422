# import math 
# import random 

# def random_path(no_of_destination):
#     random_paths = []
    
#     for i in range(5):
#         random_pathx = list(range(0, no_of_destination))
        
#         random.shuffle(random_pathx)
#         #random_pathx =  random_pathx
#         random_paths.append(random_pathx)
#     return random_paths


# # x = random_path(5)
# # print(x)

# def choose_survivors(points, old_gen):
#     survivors = []
#     random.shuffle(old_gen)
#     midpoint = len(old_gen) // 2
    
#     for i in range(midpoint):
#         if total_
    
    
    
    
''' Consider the function of maximizing the function: 
        f(x) = x^2 ; x is max range is 0 to 31
'''







# ------------------------------------------

#summer24

import random 

# fitness 
def fitness_function(chromosome, n, t):
        overlap=0
        consistency=0
        
        slots=[]
        
        for i in range(t):
                start = i * n 
                end = start + n
                slots.append(chromosome[start:end])
        
        # overlap        
        for x in slots:
                one = x.count("1")
                
                if one > 1:
                        overlap += one - 1
                        
        #consistency 
        
        for course in range(n):
                count = 0
                
                for x in slots:
                        if x[course] == "1":
                                count += 1
                consistency += abs(count-1)
                
        return -(overlap+consistency)
        
        
               
                
                
                
        
        
# chromosome

def create_chromosome(n,t):
        
        length = n*t
        chromosome =""
        
        for i in range(length):
                chromosome += random.choice("01")
                
        return chromosome

def create_population(p_size, n,t):
        population=[]
        
        for i in range(p_size):
                chromosome = create_chromosome(n,t)
                population.append(chromosome)
        return population


# parent selection 

def select_parents(population):
        p1, p2 = random.sample(population,2)
        
        return p1, p2

# Single-point Crossover

def crossover(p1,p2):
        
        point = random.choice(range(1,len(p1)))
        
        c1 = p1[point:] + p2[:point]
        c2 = p2[point:] + p1[:point]
        
        return c1, c2

# Mutation 

def mutation(chromosome):
        chromosome = list(chromosome)
        x = random.randint(0,len(chromosome)-1)
        
        if chromosome[x] == '1':
                chromosome[x] = '0'
        else:
                chromosome[x] = '1'
        
        return "".join(chromosome)



# Ga

def genetic_algorithm(n,t,p_size,it=100):
        
        population = create_population(p_size,n,t)
        
        best_chromosome = None
        high_fitness = -100000000000000000000
        
        for i in range(it):
                for chromosome in population:
                        current_fitness = fitness_function(chromosome,n,t)
                        
                        if current_fitness > high_fitness:
                                high_fitness = current_fitness
                                best_chromosome = chromosome
                                
                if high_fitness == 0:
                        break
                
                new_population = []
                
                while len(new_population) < p_size:
                        p1, p2 = select_parents(population)
                        
                        c1,c2 = crossover(p1,p2)
                        
                        c1 = mutation(c1)
                        c2 = mutation(c2)
                        
                        # adding child's to next generation
                        new_population.append(c1)
                        
                        if len(new_population) < p_size:
                                new_population.append(c2)
                # add child to new generation        
                population = new_population
                
        return high_fitness,best_chromosome
                                
                
                
                
# n,t = map(int, input().split())
# courses = []

# for i in range(n):
#         courses.append(input().strip())
n = 3
t = 3
best_chromosome, high_fitness = genetic_algorithm(n,t,100)

print(best_chromosome)
print(high_fitness)        
                        
        

#-- part 2

def select_parent(population):
        p1, p2 = random.sample(population, 2)
        print(f"Parent_1: {p1}\nParent_2: {p2}\n")
        return p1, p2

def crossover(p1, p2):
        
        point1 = random.choice(range(1, len(p1)//2))
        point2 = random.choice(range(len(p1)//2+2, len(p1)-1))
        print(f"Point1: {point1}\nPoint2: {point2}")
        c1 = p1[:point1]+p2[point1:point2]+p1[point2:]
        c2 = p2[:point1]+p1[point1:point2]+p2[point2:]
        
        return c1, c2


population = create_population(10,3,3)
p1, p2 = select_parent(population)
c1, c2 = crossover(p1,p2)

print(f"Child_1: {c1}\nChild_2: {c2}\n")






























