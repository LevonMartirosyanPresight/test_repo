from datetime import datetime
import sys
from logger import setup_logger

def fibonacci(n):
    """Calculate the nth Fibonacci number.
    
    Args:
        n (int): Non-negative integer representing position in Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Iterative approach for efficiency
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_sequence(limit):
    """Generate Fibonacci sequence up to given limit.
    
    Args:
        limit (int): Generate sequence up to this position
        
    Returns:
        list: List of Fibonacci numbers up to limit
    """
    sequence = []
    for i in range(limit + 1):
        sequence.append(fibonacci(i))
    return sequence

def main():
    """Main entry point for the application."""
    logger = setup_logger()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello from Levon! Current time: {current_time}")
    
    # Demonstrate Fibonacci functionality
    test_numbers = [0, 1, 2, 3, 4, 5, 10, 15, 20]
    print("\n=== Fibonacci Calculations ===")
    for num in test_numbers:
        try:
            result = fibonacci(num)
            message = f"Fibonacci({num}) = {result}"
            print(message)
            logger.info(message)
        except ValueError as e:
            error_message = f"Error calculating Fibonacci({num}): {str(e)}"
            print(error_message)
            logger.error(error_message)
    
    # Generate and display Fibonacci sequence
    print("\n=== Fibonacci Sequence (first 10 numbers) ===")
    sequence = fibonacci_sequence(9)
    sequence_str = ", ".join(map(str, sequence))
    print(f"Sequence: {sequence_str}")
    logger.info(f"Generated Fibonacci sequence: {sequence_str}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())