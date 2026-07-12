"""Collatz Conjecture Steps Calculator"""

def steps(number):
    """Calculate the number of steps taken for a positive integer to 
    reach 1 according to Collatz Conjecture rules.

    Args:
        number (int): A positive integer greater than 0

    Raises:
        ValueError: If number is negative or 0.

    Returns:
        int: The total number of steps taken to reach 1
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    total_steps = 0

    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        total_steps += 1

    return total_steps
