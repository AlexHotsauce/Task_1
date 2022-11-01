#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Завдання 1: Написати програму розв’язування систем 3 лінійних рівнянь з 3 невідомими, та вказати
# розв’язок X системи AX= B, де


# In[1]:


import numpy as np
A = np.array([[1, 2, 3], [0, 1, 2], [2, 0, 0]])
B = np.array([1, 1, 0])
X = np.linalg.solve(A, B)
print('X = ', X)


# In[ ]:


# ● Код програми, котра приймає інші значення матриць A і B


# In[2]:


n, m = map(int, input('Enter the number of rows and columns of matrix A through a space: ').split())
A = []
for i in range(n):
    print(i+1, 'rows:')
    r = [int(j) for j in input('Enter a row of the matrix A through a space: ').split()]
    A.append(r)
s, d = map(int, input('Enter the number of rows and columns of matrix B through a space: ').split())
B = []
for i in range(s):
    print(i+1, 'rows:')
    r_2 = [int(h) for h in input('Enter a row of the matrix B through a space: ').split()]
    B.append(r_2)
print('Matrix A: ', A)
print('Matrix B: ', B)
X = np.linalg.solve(A, B)
print('X = ', X)

