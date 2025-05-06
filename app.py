from sympy import symbols, Eq, solve, diff, integrate, sympify

x = symbols('x')

# Base class
class MathSolver:
    def __init__(self, expression):
        self.expression = sympify(expression)

    def evaluate(self):
        return self.expression.evalf()

# Derived class for algebraic equations
class AlgebraSolver(MathSolver):
    def solve_equation(self):
        equation = Eq(self.expression, 0)
        return solve(equation, x)

# Derived class for calculus
class CalculusSolver(MathSolver):
    def differentiate(self):
        return diff(self.expression, x)

    def integrate(self):
        return integrate(self.expression, x)

# Example usage
def main():
    print("🔢 Welcome to Math Solver (OOP Version)")
    expr = input("Enter an expression (e.g. x**2 + 2*x + 1): ")
    print("Choose mode:\n1. Evaluate\n2. Solve Algebraic Equation\n3. Differentiate\n4. Integrate")
    choice = input("Enter choice (1-4): ")

    try:
        if choice == '1':
            solver = MathSolver(expr)
            print("Result:", solver.evaluate())
        elif choice == '2':
            solver = AlgebraSolver(expr)
            print("Roots:", solver.solve_equation())
        elif choice == '3':
            solver = CalculusSolver(expr)
            print("Derivative:", solver.differentiate())
        elif choice == '4':
            solver = CalculusSolver(expr)
            print("Integral:", solver.integrate())
        else:
            print("Invalid choice.")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
