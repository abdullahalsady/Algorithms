arr = [101, 10, 1, 1022, 23, 123, 234]
n = len(arr)

# Iterate through the array starting from the second element
for i in range(1, n):
    # Store the current element in a temporary variable
    current = arr[i]
    
    # Find the correct position for the current element in the sorted subarray
    j = i - 1
    
    # Shift elements greater than the current element to the right
    while (j >= 0 and arr[j] > current):
        arr[j + 1] = arr[j]
        j = j - 1
    
    # Insert the current element at its correct position
    arr[j + 1] = current

# Print the sorted array
print(arr)
