
#include <stdio.h> 

void swap(int *xp, int *yp) 
{ 
	int temp = *xp; 
	*xp = *yp; 
	*yp = temp; 
} 
void bubbleSort(int arr[], int n) 
{ 
    for (int i = 0; i < n-1; i++)	 
        for (int j = 0; j < n-i-1; j++) 
            if (arr[j] > arr[j+1]) 
                swap(&arr[j], &arr[j+1]); 
} 

void printArray(int arr[], int size) 
{ 
	for (int i=0; i < size; i++) 
		printf("%d ", arr[i]); 
	printf("\n"); 
} 

int main() 
{ 
	int arr[] = {6, 2, 8, 4, 10}; 
	int n = sizeof(arr)/sizeof(arr[0]); 
	bubbleSort(arr, n); 
	printf("Sorted array: \n"); 
	printArray(arr, n); 
	return 0; 
} 
// Output: Sorted array: 2 4 6 8 10

