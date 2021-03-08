# Python program for Bubble Sort. Bubble sort is a n^2 algorithm.
# Bubble Sort is a sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
# You look at the first and second element first and swap them. Then you look at the 2nd and 3rd element and swap them.


# define the function
def bubbleSort(arr):
    n = len(arr) # len of arr = 7

    # Traverse through all array elements. You use n - 1  since range starts from 0
    for i in range(n - 1): # (7 - 1) -> range(6) -> [0, 1, 2, 3, 4, 5, 6]


        # loop through the entire array first. Then you loop through the entire array - 1 since the last element of
        # the array will be the largest element
        for j in range(0, n - i - 1): # (0, 7  - 0 - 1) -> (0, 6)
                                      # (0, 7 - 1  - 1) -> (0, 5))

            # check if the current element is larger than the next element
            if arr[j] > arr[j + 1]:
                # if true, swap the two elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# create an array and pass it into the bubbleSort function
arr = [5, 6, 33, 12, 2, 18, 9]

# call bubbleSoft on arr
bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)): # range (7)
    print("%d" % arr[i])
