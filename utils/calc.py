def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b

def my_calc(a, b, operator):
  if operator == "+":
    return add(a, b)
  elif operator == "-":
    return subtract(a, b)
  elif operator == "*":
    return multiply(a, b)
  elif operator == "/":
    return divide(a, b)
  else:
    return None
    