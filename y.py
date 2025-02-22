# Function 1: Using 1 iteration (simple multiplication)
def multiply_using_iteration(N, M):
    return N * M

# Function 2: Using N iterations (manual addition)
def multiply_using_n_iterations(N, M):
    result = 0
    for _ in range(N):
        result += M
    return result

# Example usage:
N = 5
M = 3

# Using iteration (direct multiplication)
result1 = multiply_using_iteration(N, M)
print(f"Result using iteration: {result1}")

# Using N iterations (manual addition)
result2 = multiply_using_n_iterations(N, M)
print(f"Result using {N} iterations: {result2}")
