
import random
import time

# Insertion Sort
def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        return arr


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Measure execution time
def measure_time(sort_function, data):
    start = time.perf_counter()

    result = sort_function(data)

    end = time.perf_counter()

    assert result == sorted(data), "Sorting result is incorrect!"

    return end - start


# Generate different input types
def generate_data(size):
    random_data = [random.randint(0, 10000) for _ in range(size)]

    return {
        "Random": random_data,
        "Sorted": sorted(random_data),
        "Reversed": sorted(random_data, reverse=True)
    }


# Main Benchmark
def run_benchmark():
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Built-in Sort": sorted
    }

    sizes = [100, 500, 1000, 5000, 10000]

    results = {}

    for size in sizes:
        print(f"\nInput Size: {size}")

        data_types = generate_data(size)

        for data_name, data in data_types.items():
            print(f"\n{data_name} Data:")

            for name, algorithm in algorithms.items():

                if name == "Insertion Sort" and size > 10000:
                    continue

                execution_time = measure_time(
                    algorithm, data
                )

                results.setdefault(name, []).append(
                    (size, data_name, execution_time)
                )

                print(
                    f"{name}: {execution_time:.6f} seconds"
                )

    return results


# Plot Results
def plot_results(results):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nInstall matplotlib to display graphs:")
        print("pip install matplotlib")
        return

    for algorithm, measurements in results.items():
        plt.figure()

        for data_type in ["Random", "Sorted", "Reversed"]:
            sizes = [
                size for size, kind, _ in measurements
                if kind == data_type
            ]

            times = [
                elapsed for _, kind, elapsed in measurements
                if kind == data_type
            ]

            plt.plot(
                sizes,
                times,
                marker="o",
                label=data_type
            )

        plt.title(algorithm)
        plt.xlabel("Input Size")
        plt.ylabel("Execution Time (seconds)")
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    benchmark_results = run_benchmark()
    plot_results(benchmark_results)
