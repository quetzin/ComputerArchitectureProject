import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def read_array_from_file(filename):
    with open(filename, 'r') as file:
        arr = [int(line.strip()) for line in file.readlines()]
    return arr

def write_array_to_file(arr, filename):
    with open(filename, 'w') as file:
        for number in arr:
            file.write(f"{number}\n")

# Driver code
input_filename = 'unsorted_numbers.txt'
output_filename = 'sorted_numbers.txt'

start_time = time.time()

arr = read_array_from_file(input_filename)
bubble_sort(arr)
write_array_to_file(arr, output_filename)

end_time = time.time()
total_time = end_time - start_time

print(f"Total time taken: {total_time:.6f} seconds")
