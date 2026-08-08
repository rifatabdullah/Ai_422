# a = [ 2,34,5,2, 'ff', 'gg',32]

# print(a[2:]) # 5, 2,'ff','gg',32

# print(a[::2]) 

# for i in range(0, len(a), 2):
#     print(a[i], end=" ")


# print(type(a)) # <class 'list'>



#-------------------------
# my_dict = {'Biscuit':20,'Chocolate':30,'Guns':150,'perfume':50}

# print(my_dict.items())


# list_of_students = ['Johaier','Afra','Omor','Arham','Saifan','Sumaiya']
# set_of_students = set(list_of_students)
# print(set_of_students)
# print("-------")
# print(list_of_students)

# print(dir(list_of_students)) # display attributes and methods

# help() # inside it write anything 
# dir() # display attributes and methods


''' .split():

# Default whitespace split
"hello   world \n python".split()  
# Output: ['hello', 'world', 'python']

# Custom separator & split limit
"a-b-c-d".split("-", maxsplit=2)  
# Output: ['a', 'b', 'c-d']

# '''
# a = "hgh lsdkfj-f dfkkjsdfk dflkjk-fjf"
# print(a.split('-',maxsplit=5))

''' map() method:
# Applying int() to convert strings
numbers = map(int, ["10", "20", "30"])
print(numbers)        # Output: <map object at ...>
print(list(numbers))  # Output: [10, 20, 30]

# Multiple iterables (2^3 and 3^2)
powers = list(map(pow, [2, 3], [3, 2])) 
# Output: [8, 9]

'''

# a = [65.4, 734.1, 10]
# print(list(map(str,a)))


''' random.sample()
import random

deck = ["Ace", "King", "Queen", "Jack", "10", "9"]

# Deal 3 unique cards
hand = random.sample(deck, 3)

print(hand)  # Output e.g., ['Queen', 'Ace', '10']
print(deck)  # Original list remains completely unchanged

'''
# can't put 0 inside random.Choice(0,2) X
'''
import random

# Using randint
num1 = random.randint(1, 6) -- better as it needs less function 

# Equivalent using choice (note the +1 because range upper bound is exclusive)
num2 = random.choice(range(1, 7))
'''


''' "".join(chromosome) -- 110011001 -- return chromosome in this way but str() can't

def format_chromosome(chromosome):
    return "".join(chromosome)

# DNA base list
dna_list = ['A', 'T', 'C', 'G', 'A']
print(format_chromosome(dna_list))
# Output: "ATCGA"

# Binary gene list
bit_list = ['1', '0', '1', '1', '0']
print(format_chromosome(bit_list))
# Output: "10110"

'''


##### OOP



# class waiter:
#     def __init__(self):
#         self.tables = []
    
#     def add_tables(self, table_number):
#         self.tables.append(table_number)
        
        
# don = waiter()
# sam = waiter()

# don.add_tables(1)
# sam.add_tables(2)

# print(don.tables)


# s = 'rabit'
# print(s[-2:-1])




# class car:
#     def __init__(self,model,year,reg):
#         self.model = model
#         self.year = year 
#         self.reg = reg
        
#     def details(self):
#         print(f"{self.model} was produced in {self.year} and {"registered" if self.reg else "not registered"}")
        
#     def info(self):
#         print(f"{self.model} is in Service center")
        

# class engine(car):
#     def engine_no(self):
#         print(f"here's the engine number: {self.model[0:2]+str(self.year)[-3:-1]}")
#     def info(self):
#         self.engine_no
        
        
# class chassis(car):
#     def chassis_no(self):
#         print(f"here's the chassis number: {self.model[-3:-1]+str(self.year)[0:2]}")
#     def info(self):
#         self.chassis_no
        


# mercedez = chassis("sclass",2020,True)
# bmw = car("rtype",2001,False)

# print()
# mercedez.details()
# print()

# mercedez.info()


# li = []

# li.append('a')
# li.append('b')
# li.append('c')

# print(li)

# li.pop()
# print(li)


# from collections import deque

# stack = deque()

# stack.append('q')
# stack.append('w')
# stack.append('e')

# print(stack)

# stack.pop()
# print(stack)

 
# from collections import deque
# stack = deque()
# a = "We will conquere COVID-19"

# for i in range(len(a)):
#     stack.append(a[i])
# print(f"Original text: \n{a}")

# print(f"Reversed text: ")
# for j in range(len(a)):
#     print(stack.pop(), end="")
    
    
    
    
# from collections import deque 

# class stack:
#     def __init__(self):
#         self.x = deque()
        
#     def push(self, val):
#         self.x.append(val)
    
#     def pop(self):
#         return self.x.pop()
    
#     def peek(self):
#         return self.x[-1]
    
#     def is_empty(self):
#         return len(self.x) == 0
    
#     def size(self):
#         return len(self.x)
    
#     def reverse(self,a):
#         st = stack()
        
#         for i in a:
#             st.push(i)
        
#         rev=''
#         while st.size() != 0:
#             rev += st.pop()
            
#         return rev
    
# s = stack()

# m = s.reverse("We will conquere COVID-19")
# print(m)


    
    
    
    
## Valid Parentheses 

# class vaPa:
#     def isValid(self, inp: str):
#         dic = {')':'(', '}':'{', ']':'['}
#         stack = []
        
#         for i in inp:
#             if i not in dic:
#                 stack.append(i) # only opening Brackets 
#             else:
#                 if stack == 0:
#                     return False
#                 else:
#                     pop = stack.pop() # (, {, [
#                     if pop != dic[i]: # ( = dic[')']
#                         return False
#                     else:
#                         return True
                    
        
# s = vaPa()
# print(s.isValid("({[]})"))                        



# from collections import deque

# price_q = deque()

# price_q.appendleft(1)
# price_q.appendleft(2)
# price_q.appendleft(3)


# print(price_q)
# price_q.pop()

# print(price_q)



# from collections import deque

# class queue:
    
#     def __init__(self):
#         self.x = deque()
        
#     def enqueue(self, val):
#         self.x.appendleft(val)
        
#     def dequeue(self):
#         self.x.pop()
        
#     def isEmpty(self):
#         return len(self.x) == 0
    
#     def size(self):
#         return len(self.x)
    
    
# pq = queue()

# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.01 AM',
#     'price': 131.10
# })
# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.02 AM',
#     'price': 132
# })
# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.03 AM',
#     'price': 135
# })

# print(pq.size())
# print(list(pq.x))
# print()
# pq.dequeue()

# print(list(pq.x))



###

# num = [0,1,2,4,5,6,7,8,9]

# print(num[:-3]) # except last three
#print(num[-3:]) # from -3 to last 

# print(num[::-1])

# num[1:1] = [11,22] ## Inserting elements at a certain Index

# print(num)

# del num[1:2]

# print(num)



# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# # First element (two ways)
# print(lst[0])
# print(lst[-len(lst)]) # -len(lst) = -10 (first element)

# # Last element (two ways)
# print(lst[-1])
# print(lst[len(lst) - 1]) # len(lst)-1 = 9 (last element)




# import random
# def single_point_crossover(p1,p2):
#     point = random.randint(1,len(p1)-1)
    
#     c1 = p2[:point] + p1[point:]
#     c2 = p1[:point] + p2[point:]
    
#     return c1,c2

# p1 = [1,0,1,0,1]
# p2 = [0,0,1,1,0]
# c1,c2 = single_point_crossover(p1,p2)
# print(c1)
# print(c2)


# a = {1:'a',2:'b',3:'c',4:'d'}
# b = {13:'a',21:'b',32:'c',43:'d'}

# print(b[1])

# for i in a:
#     print(i, end=" ")
# print()
# for i, j in a.items():
#     print(f"Key: {i}, Value: {j}")
    
# print()

# for i in a.values():
#     print(i, end=" ")
    
    
# merge = a | b
# print(merge)


# def invert_dict(a):
#     invereted = {}
#     for i, j in a.items():
#         invereted[j] = i
#     return invereted

# print(a)
# print(invert_dict(a))



# def build_dict_from_lists(keys, values):
#     result = {}
#     for i in range(len(keys)):
#         result[keys[i]] = values[i]
#     return result

# key_list   = ['x', 'y', 'z']
# value_list = [10,  20,  30 ]
# d = build_dict_from_lists(key_list, value_list)
# print(d) 



# population = [
#     {'genes': [1, 0, 1, 1, 0],  'fitness': 3},
#     {'genes': [0, 1, 1, 0, 0],  'fitness': 2},
#     {'genes': [1, 1, 1, 1, 1],  'fitness': 5},
# ]




''' Heap Functions and their Methods'''



# import heapq

# nums = [110, 20, 115, 30, 40]

# heapq.heapify(nums) # sorts in min-heap order but not fully in min to max order
# print("Heap Queue:", nums)
# heapq.heappop(nums) # pops the first element of the list 
# heapq.heappush(nums, 4) # pushed an element to the heap
# print(nums)



# n largest & smallest 

# import heapq

# h = [100,20,90,10,2,1,23]

# heapq.heapify(h)
# print(h)
# print()
# largest = heapq.nlargest(3,h)
# print("3 largest Elements:", largest )
# print()
# smallest = heapq.nsmallest(3, h)
# print("3 Smallest Elements:", smallest)

# heapq.heappushpop(h,4) # pops smallest element and push the given element 

# print(h)

                
# import heapq

# pq = []

# heapq.heappush(pq, (10, "A"))
# heapq.heappush(pq, (5, "B"))
# heapq.heappush(pq, (20, "C"))

# print(pq)







# import heapq

# nums = [10, 20, 15, 30, 40]

# # Convert into a max-heap by inverting values
# max_heap = []
# for n in nums:
#     max_heap.append(-n)

# heapq.heapify(max_heap)
# heaped = []
# for n in max_heap:
#     heaped.append(-n)

# print(heaped)
# # Access largest element (invert sign again)
# largest = -max_heap[0]
# print("Largest element:", largest)





### Recursion 

# def backward(n):
#     if n == 0:
#         return 
#     print(n)
#     backward(n-1)
    
# backward()


# print(min(2,3))




# num = [22,3,4,5,21]

# # # num.pop()

# # # print(num)


# # for i in num:
# #     print(i, end=" ")


# num.sort()

# print(num)

# num.sort(reverse=True)

# print(num)


# def minmax(tree,is_max):
    
#     if type(tree) != list:
#         return tree
    
#     if is_max:
#         best = float('-inf')
        
#         for child in tree:
#             value = minmax(child, False)
#             best = max(best, value)
            
#         return best 
    
#     else:
#         best = float('inf')
        
#         for child in tree:
#             value = minmax(child, False)
#             best = max(best, value)
            
#         return best

# tree = [
#     [[3, 5], [6, 9]],
#     [[1, 2], [0, -1]]
# ]

# print("Best value:", minmax(tree, True))






## MinMax















