# helper.py

def perform_calculation(value1, value2, operation):
    if operation == 'addition':
        return value1 + value2
    elif operation == 'subtraction':
        return value1 - value2
    elif operation == 'multiplication':
        return value1 * value2
    elif operation == 'division':
        if value2 != 0:
            return value1 / value2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError(f"Unsupported operation: {operation}")

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")

