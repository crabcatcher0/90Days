"""
Binary Search:
Here we use:::>>>
while loop to continue the process of comparing the key
 and splitting the search space in two halves.
"""

def binary_search(arr, low, high, x):

    while low <= high:
        mid = low + (high - low)

        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore the left half
        elif arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore the right half
        else:
            high = mid - 1

    # If we reach here, then the element was not present
    return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40, 50]
    x = 4
    result = binary_search(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Not found")
