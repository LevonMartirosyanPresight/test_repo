from datetime import datetime
import sys

def main():
    """Main entry point for the application."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello from Levon! Current time: {current_time}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
