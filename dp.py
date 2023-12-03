

# A recursive Python3 program for
# partition problem
 
# A utility function that returns
# true if there is a subset of
# arr[] with sum equal to given sum
import time
import json
import tracemalloc

def findPartition(arr, n):
    sum = 0
    i, j = 0, 0
 
    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]
 
    if sum % 2 != 0:
        return False
 
    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]
 
    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True
 
    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False
 
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):
 
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
 
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
   
    return part[sum // 2][n]
 





# Read lists from text files
with open('random_list_10.txt', 'r') as file:
    list_10 = json.loads(file.read())

with open('random_list_40.txt', 'r') as file:
    list_40 = json.loads(file.read())

with open('random_list_80.txt', 'r') as file:
    list_80 = json.loads(file.read())

for lst in [list_10,list_40,list_80]:
  

  # Driver code

    start_time = time.time()
    tracemalloc.start()  

       

     
# Driver Code

    n = len(lst)
    
    # Function call
    if findPartition(lst, n) == True:
        print("Can be divided into two",
              "subsets of equal sum")
    else:
        print("Can not be divided into ",
              "two subsets of equal sum")

  
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.clear_traces()

    print(f"Peak memory usage: {peak / 10**6} MB")
    end_time = time.time()

    print(f"Time taken with dataset list_{n}: {(end_time - start_time) * 1000} ms")
