import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j +1] = key    

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
insertion_sort(arr)
write_array_to_file(arr, output_filename)

end_time = time.time()
total_time = end_time - start_time

print(f"Total time taken: {total_time:.6f} seconds")
