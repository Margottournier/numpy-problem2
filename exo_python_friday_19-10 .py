# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:07:28 2023

@author: Msi
"""
#Problem numpy 2

#ex1:Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
import numpy as np


for i in range(21):
    vect=np.arange(0,21)
    if i>=9 and i<15:
        vect[i]=-vect[i]
    print(vect[i])
    
#or more simple:
import numpy as np
vect = np.arange(0, 21)
vect[9:16] = -vect[9:16]
print(vect)


 #ex2: Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
import numpy as np
vector = np.arange(15, 56)
print(vector[1:-1])

#ex3:Write a NumPy program to create a 3X4 array and iterate over it.

mat=np.zeros((3,4))

for i in range(3):
    for j in range(4):
        mat[i,j]=int(input("Enter a value"))
print(mat)
for i in mat:
    for j in i:
        print(j)
        
#ex4:Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
vect=np.linspace(5,50,10)
print(vect)

#ex5: Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
vect=np.random.randint(0,10,size=5)
print(vect)

#for an other example with an array
import numpy as np
matrix = np.random.randint(0, 11, size=(3, 4))
print(matrix)

#ex6:Write a NumPy program to multiply the values of two given vectors.
n=int(input("Enter the size for your vectors:"))
vect1=np.empty(n, dtype=int)
vect2=np.empty(n, dtype=int)

for i in range(n):
    vect1[i]=int(input("Enter the value for vect1:"))
    vect2[i]=int(input("Enter the value for vect2:"))

print(vect1*vect2)

#ex7:Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
values=np.arange(10,22)
print(values)
mat=values.reshape(3,4)
print(mat)

#ex8:Write a NumPy program to find the number of rows and columns in a given matrix.
mat= np.array([[2,4,7,10,11],[2,6,3,0,2],[2,6,8,4,9]])
row=len(mat)
column=len(mat[0])
print("The nb of row is {} and the nb of column is {}".format(row,column))

#ex9: Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.
mat=np.full((4,4),1)
for i in range(4):
    mat[i,i]=0
print(mat)

#ex10:Write a NumPy program to find common values between two arrays.Expected Output:Array1: [ 0 10 20 40 60]Array2: [10, 30, 40]Common values between two arrays:[10 40]
array1=np.array([0, 10, 20, 40 ,60])
array2=np.array([10, 30, 40])
list=[]
print(array1,array2)
for i in range (len(array1)):
    for j in range (len(array2)):
        if array1[i]==array2[j]:
            list.append(array1[i])
print(list)

#ex11:Write a NumPy program to get the unique elements of an array.Expected Output:Original array:[10 10 20 20 30 30] Unique elements of the above array:[10 20 30]Original array:[[1 1][2 3]]Unique elements of the above array:[1 2 3]
array=np.array([10, 10, 20, 20 ,30 ,30])
unique_e=[]

for i in array:
    if i not in unique_e:
        unique_e.append(i)
        
print(unique_e)

#ex12:Write a NumPy program to compute the cross product of two given vectors 
array1=[1,5,7]
array2=[3,8,4] 
cross_product=np.cross(array1,array2)  
print(cross_product)

#EX14:
import numpy as np

original_array=[ 0, 1, 2 ,3, 4 ,5, 6 ,7, 8 ,9 ,10, 11, 12, 13, 14, 15, 16, 17 ,18 ,19, 20 ,21 ,22 ,23, 24,
25, 26, 27 ,28, 29, 30, 31 ,32, 33 ,34 ,35, 36, 37, 38, 39, 40 ,41 ,42, 43, 44 ,45, 46 ,47 ,48, 49,
50, 51 ,52, 53 ,54, 55, 56 ,57 ,58, 59, 60, 61 ,62, 63, 64, 65, 66 ,67 ,68, 69 ,70, 71, 72, 73, 74,
75, 76, 77 ,78, 79, 80, 81, 82, 83, 84 ,85 ,86, 87, 88 ,89, 90, 91 ,92 ,93 ,94, 95, 96, 97, 98 ,99]


given_scalar = float(input("Enter a float value: "))  

closest_value = None
min_difference = float('inf')

for value in original_array:
    difference = abs(value - given_scalar)
    if difference < min_difference:
        min_difference = difference
        closest_value = value

print("Tableau d'origine :")
print(original_array)
print(f"Valeur la plus proche de {given_scalar} : {closest_value}")





