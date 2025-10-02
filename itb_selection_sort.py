import time
import random

def selection_sort_with_stats(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    start_time = time.time()
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
	    swaps += 1

end_time = time.time()
	execution_time = end_time - start_time

	return arr, comparisons, swaps, execution_time

	def generate_random_array(size):
		return [random.randint(1, 10000) for _ in range(size)]

		def main():
			sizes = [10, 100, 1000]

			print("Selection Sort Performance Analysis")
			print("=" * 60)

			for size in sizes:
			print(f"\nArray size: {size} elements")
			print("-" * 40)

	test_array = generate_random_array(size)
original_array = test_array.copy()

sorted_array, comparisons, swaps, exec_time = selection_sort_with_stats(test_array)

is_sorted_correctly = sorted_array == sorted(original_array)

	print(f"Execution time: {exec_time:.6f} seconds")
        print(f"Number of comparisons: {comparisons}")
        print(f"Number of swaps: {swaps}")
        print(f"Sorting correct: {'Yes' if is_sorted_correctly else 'No'}")
        
        theoretical_comparisons = size * (size - 1) // 2
        print(f"Theoretical comparisons (n(n-1)/2): {theoretical_comparisons}")
        print(f"Actual/Theoretical ratio: {comparisons/theoretical_comparisons:.3f}")

if __name__ == "__main__":
    main()
