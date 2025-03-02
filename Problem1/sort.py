import time
import matplotlib.pyplot as plt
import random

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Function to measure sorting times
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

# Larger predefined list size to test varying levels of sortedness
predefined_size = 20000
sortedness_levels = [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]  # Proportion of elements that are sorted
test_runs = 5  # Define the number of test runs

# Previously used list generation functions (commented out)
# def generate_random_list(size):
#     return [random.randint(0, 10000) for _ in range(size)]

# def generate_sorted_list(size):
#     return list(range(size))

# def generate_reversed_list(size):
#     return list(range(size, 0, -1))

# Function to generate partially sorted lists
def generate_partially_sorted_list(size, sortedness):
    arr = list(range(size))
    num_unsorted = int(size * (1 - sortedness))
    indices_to_shuffle = random.sample(range(size), num_unsorted)
    random.shuffle(indices_to_shuffle)
    shuffled_values = [arr[i] for i in indices_to_shuffle]
    random.shuffle(shuffled_values)
    for idx, val in zip(indices_to_shuffle, shuffled_values):
        arr[idx] = val
    return arr

# Testing and graphing
def run_experiment():
    insertion_times_avg = []
    merge_times_avg = []
    
    for sortedness in sortedness_levels:
        insertion_times = []
        merge_times = []
        
        print(f"\nSortedness {sortedness*100:.0f}%:")
        print(f"\t{'Insertion Sort':<20}{'Merge Sort'}")
        
        for _ in range(test_runs):
            arr = generate_partially_sorted_list(predefined_size, sortedness)
            insertion_time = measure_time(insertion_sort, arr[:])
            merge_time = measure_time(merge_sort, arr[:])
            insertion_times.append(insertion_time)
            merge_times.append(merge_time)
            print(f"\t{insertion_time:.6f}s{'':10}{merge_time:.6f}s")
        
        avg_insertion = sum(insertion_times) / test_runs
        avg_merge = sum(merge_times) / test_runs
        insertion_times_avg.append(avg_insertion)
        merge_times_avg.append(avg_merge)
        print(f"\tAverage: {avg_insertion:.6f}s{'':6}{avg_merge:.6f}s\n")

    # Plot results
    plt.figure(figsize=(8, 5))
    plt.plot(sortedness_levels, insertion_times_avg, label='Insertion Sort (Avg)', marker='o')
    plt.plot(sortedness_levels, merge_times_avg, label='Merge Sort (Avg)', marker='s')
    plt.xlabel('Proportion Sorted')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Performance vs. Sortedness Level')
    plt.legend()
    plt.show()

# Run experiment
run_experiment()