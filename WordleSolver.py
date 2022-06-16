from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

class WordleSolver:
    def __init__(self):
        self.website = 'https://www.powerlanguage.co.uk/wordle/'
        self.path = self.path
        
        hub = open('sgb-words.txt', 'r')
        self.words = hub.read().strip().split('\n')

        self.driver = webdriver.Chrome()
        self.driver.get(self.website)
        self.driver.implicitly_wait(5)
    
        self.board = self.driver.find_element_by_name('board')
    

# import sympy
# # print(list(sympy.primerange(2, 102)))
# q = int(input())
# for _ in range(q):
#     a, b, k = map(int, input().split())
#     x = False
#     for p in range(a, b+1):
#         if len(list(sympy.primerange(a, p+1))) == k:
#             print(p)
#             x = True
#             break
#     if not x:
#         print(-1)

# import sympy
# # print(list(sympy.primerange(2, 102)))
# q = int(input())
# for _ in range(q):
#     a, b, k = map(int, input().split())
#     if list(filter(lambda p: len(list(sympy.primerange(a, p+1)))==k,range(a,b+1))): print(p)
#     else: print(-1)

# q = int(input())
# def x(p):
#     if len(list(sympy.primerange(a, p+1)))==k:
#         global pq
#         pq = p
#         return p
# for _ in range(q):
#     a, b, k = map(int, input().split())
#     if list(filter(x(p),range(a,b+1))): print(pq)
#     else: print(-1)

# def firstKMax(arr,n,k):
#     b = arr.copy()
#     res = []
#     a = True
#     for _ in range(k):
#         if not a:
#             break
#         for _ in range(b.count(arr.pop(arr.index(max(arr))))):
#             if k>len(arr):
#             	a = False
#                 break
#             res.append(str(b.index(max(arr))))
#     return res

import numpy
# def substrings(n, x):
#     return numpy.fromfunction(lambda i, j: x[i + j], (len(x) - n + 1, n), dtype = int)
# print(substrings(2, 'abc'))

# def substrings(n, x):
#   return numpy.fromfunction(lambda i, j: x[i + j], (len(x) - n + 1, n), 
#                             dtype=int)


# def perms(array, n):
#     permutations = list((array[j:j + n] for j in range(0, len(array) - (n - 1))))
#     return permutations
# perm = perms('abced', 3)
# print(list(zip(perm)))