from datetime import datetime
import sys
from logger import setup_logger

def factorial(n):
    """Calculate factorial of a non-negative integer.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    """Main entry point for the application."""
    logger = setup_logger()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello from Levon! Current time: {current_time}")
    
    # Demonstrate factorial functionality
    test_numbers = [5, 10, 0, 1]
    for num in test_numbers:
        try:
            result = factorial(num)
            message = f"Factorial of {num} is {result}"
            print(message)
            logger.info(message)
        except ValueError as e:
            error_message = f"Error calculating factorial of {num}: {str(e)}"
            print(error_message)
            logger.error(error_message)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())