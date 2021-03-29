
def selectionSort(uA):
    for i in range(len(uA)): 
        min_index = i 
        for j in range(i+1, len(uA)): 
            if uA[min_index] > uA[j]: 
                min_index = j 
        uA[i], uA[min_index] = uA[min_index], uA[i] 
  
unsortedArray = [9, 6, 5, 8, 2] 
selectionSort(unsortedArray)

print(unsortedArray) # [2, 5, 6, 8, 9]

