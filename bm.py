def calculate_series_resistance(resistances):
    # Total resistance in a series circuit is the sum of all resistances
    return sum(resistances)

def calculate_parallel_resistance(resistances):
    # Total resistance in a parallel circuit is the reciprocal of the sum of reciprocals
    reciprocal = 0
    for r in resistances:
        reciprocal += 1 / r
    return 1 / reciprocal if reciprocal != 0 else float('inf')

def main():
    print("Circuit Solver")
    circuit_type = input("Ent
