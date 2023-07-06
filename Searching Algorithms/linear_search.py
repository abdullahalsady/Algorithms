# Linear search implementation without a function
numbers = [5, 2, 7, 1, 9, 3]
target_number = 7

found = False
index = -1

for i in range(len(numbers)):
    if numbers[i] == target_number:
        found = True
        index = i
        break

if found:
    print("Element found at index", index)
else:
    print("Element not found")

    