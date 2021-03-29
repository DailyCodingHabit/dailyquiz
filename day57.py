

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        x = step - 1
        while x >= 0 and key < array[x]:
            array[x + 1] = array[x]
            x = x - 1
        array[x + 1] = key

data = [9, 6, 5, 8, 2]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data) #[2, 5, 6, 8, 9]


