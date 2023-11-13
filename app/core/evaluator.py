import sympy as sp

def evaluate_expression(expression):
    try:
        return sp.sympify(expression)
    except Exception as e:
        return f"Error: {e}"