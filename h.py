# Function to print Fibonacci series up to n terms
def fibonacci_series(n):
    # First two terms of Fibonacci series
    a, b = 0, 1
    print("Fibonacci series up to", n, "terms:")
    
    # Loop to print the Fibonacci series
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update a and b for the next term

# Input from the user
n_terms = int(input("Enter the number of terms in Fibonacci series: "))

# Call the function to print Fibonacci series
fibonacci_series(n_terms)
