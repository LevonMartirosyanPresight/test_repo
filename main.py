from datetime import datetime
import os
import platform

print(f"Hello from Levon! Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Running on: {platform.system()} {platform.release()}")
print(f"Python version: {os.sys.version}")

# Add error handling
try:
    result = 10 / 2
    print(f"Calculation result: {result}")
except Exception as e:
    print(f"Error occurred: {e}")
