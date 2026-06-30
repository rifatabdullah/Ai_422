# a = [ 2,34,5,2, 'ff', 'gg',32]

# print(a[2:]) # 5, 2,'ff','gg',32

# print(a[::2]) 

# for i in range(0, len(a), 2):
#     print(a[i], end=" ")
    


# my_dict = {'Biscuit':20,'Chocolate':30,'Guns':150,'perfume':50}

# print(my_dict.items())


# list_of_students = ['Johaier','Afra','Omor','Arham','Saifan','Sumaiya']

# set_of_students = set(list_of_students)

# print(set_of_students)
# print("-------")
# print(list_of_students)


# help() # inside it write anything 
# dir() # display attributes and methods


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


from collections import deque

class queue:
    
    def __init__(self):
        self.x = deque()
        
    def enqueue(self, val):
        self.x.appendleft(val)
        
    def dequeue(self):
        self.x.pop()
        
    def isEmpty(self):
        return len(self.x) == 0
    
    def size(self):
        return len(self.x)
    
    
pq = queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.size())
print(list(pq.x))
print()
pq.dequeue()

print(list(pq.x))