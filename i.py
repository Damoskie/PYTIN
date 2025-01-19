# Base class for all expressions
class Expression:
    def evaluate(self):
        raise NotImplementedError("Subclasses must implement this method")


# Class for a constant value
class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


# Class for binary operations like addition, subtraction, etc.
class BinaryOperation(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        raise NotImplementedError("Subclasses must implement this method")


# Class for addition operation
class Add(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()


# Class for subtraction operation
class Subtract(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()


# Class for multiplication operation
class Multiply(BinaryOperation):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()


# Class for division operation
class Divide(BinaryOperation):
    def evaluate(self):
        # Prevent division by zero
        if self.right.evaluate() == 0:
            raise ValueError("Cannot divide by zero")
        return self.left.evaluate() / self.right.evaluate()


# Class for handling a mathematical expression
class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        result = self.expression.evaluate()
        return result


# Example usage:
if __name__ == "__main__":
    # (3 + 5) * 2
    expr = Multiply(Add(Constant(3), Constant(5)), Constant(2))
    solver = ExpressionSolver(expr)
    result = solver.solve()
    print(f"Result: {result}")
