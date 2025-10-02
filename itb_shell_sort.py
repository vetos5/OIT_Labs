import time
import random

def shell_sort_with_stats(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    start_time = time.time()
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap:
                comparisons += 1
                if arr[j - gap] <= temp:
                    break
                arr[j] = arr[j - gap]
                swaps += 1
                j -= gap
            
            arr[j] = temp
        
        gap //= 2
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return arr, comparisons, swaps, execution_time

def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

def main():
    sizes = [10, 100, 1000]
    
    print("Shell Sort Performance Analysis")
    print("=" * 60)
    
    for size in sizes:
        print(f"\nArray size: {size} elements")
        print("-" * 40)
        
        test_array = generate_random_array(size)
        original_array = test_array.copy()
        
        sorted_array, comparisons, swaps, exec_time = shell_sort_with_stats(test_array)
        
        is_sorted_correctly = sorted_array == sorted(original_array)
        
        print(f"Execution time: {exec_time:.6f} seconds")
        print(f"Number of comparisons: {comparisons}")
        print(f"Number of swaps: {swaps}")
        print(f"Sorting correct: {'Yes' if is_sorted_correctly else 'No'}")

if __name__ == "__main__":
    main()
