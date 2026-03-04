"""Utility functions for the test repository.

Code Review Comments Added:
- Enhanced documentation with detailed docstrings
- Added hash algorithm validation
- Improved error handling suggestions
- Added implementation notes for future enhancements
"""

import os
import sys
import platform
from datetime import datetime
import hashlib
import json
from typing import Dict, Any, List, Optional

def get_system_info() -> Dict[str, str]:
    """Get comprehensive system information.
    
    Returns:
        Dict[str, str]: System information including platform, architecture, Python version
        
    Note: Consider adding try-except for platform-specific failures
    """
    return {
        'platform': platform.system(),
        'platform_release': platform.release(),
        'platform_version': platform.version(),
        'architecture': platform.machine(),
        'hostname': platform.node(),
        'processor': platform.processor(),
        'python_version': platform.python_version(),
        'python_implementation': platform.python_implementation()
    }


def format_timestamp(timestamp: Optional[datetime] = None) -> str:
    """Format timestamp as human-readable string.
    
    Args:
        timestamp: Optional datetime object, defaults to current time
        
    Returns:
        str: Formatted timestamp string
        
    Note: Could add timezone support for enterprise use
    """
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime('%Y-%m-%d %H:%M:%S')


def calculate_file_hash(filepath: str, algorithm: str = 'md5') -> str:
    """Calculate hash of a file.
    
    Args:
        filepath: Path to the file to hash
        algorithm: Hash algorithm to use (default: md5)
        
    Returns:
        str: Hexadecimal hash of the file
        
    Raises:
        FileNotFoundError: If file does not exist
        ValueError: If hash algorithm is unsupported
    
    Note: Excellent memory-efficient approach using 4096-byte chunks
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    # Add hash algorithm validation for better error handling (Review Suggestion)
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")
    
    hash_obj = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


def save_system_info(filepath: str = 'system_info.json') -> Dict[str, Any]:
    """Save system information to JSON file.
    
    Args:
        filepath: Output file path for system information (default: 'system_info.json')
        
    Returns:
        Dict[str, Any]: Complete system information with timestamp
    """
    info = get_system_info()
    info['timestamp'] = format_timestamp()
    info['script_path'] = os.path.abspath(__file__)
    
    with open(filepath, 'w') as f:
        json.dump(info, f, indent=2)
    
    return info


def validate_python_version(min_version: str = '3.7') -> bool:
    """Validate Python version meets minimum requirements.
    
    Args:
        min_version: Minimum Python version required (default: '3.7')
        
    Returns:
        bool: True if current version meets or exceeds minimum
        
    Note: Consider logging current version for debugging
    """
    current = sys.version_info
    required = tuple(map(int, min_version.split('.')))
    return current >= required


def get_directory_size(directory: str) -> int:
    """Calculate total size of directory in bytes.
    
    Args:
        directory: Path to the directory to calculate size for
        
    Returns:
        int: Total size in bytes
        
    Note: Proper directory traversal with safety checks.
          Could add progress callback for large directories
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.exists(filepath):
                total_size += os.path.getsize(filepath)
    return total_size


def format_bytes(size: int) -> str:
    """Format bytes into human-readable format.
    
    Args:
        size: Size in bytes to format
        
    Returns:
        str: Human-readable formatted size
        
    Note: Clean human-readable formatting.
          Could extend to include file count in directory stats
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"


def main():
    """Demonstrate utility functions.
    
    Note: Excellent demonstration of all utilities.
          Could add error handling for file I/O operations.
    """
    print("=== System Information Utility ===")
    print("Code Review: Enhanced with inline comments and suggestions")
    
    # Display system info
    info = get_system_info()
    print(f"Platform: {info['platform']} {info['platform_release']}")
    print(f"Python: {info['python_version']} ({info['python_implementation']})")
    print(f"Architecture: {info['architecture']}")
    print(f"Hostname: {info['hostname']}")
    
    # Validate Python version
    if validate_python_version():
        print("✅ Python version meets requirements")
    else:
        print("❌ Python version below minimum requirements")
    
    # Calculate directory size with proper handling
    current_dir = '.'
    size = get_directory_size(current_dir)
    print(f"Current directory size: {format_bytes(size)}")
    
    # Save system info
    try:
        saved_info = save_system_info()
        print(f"System info saved to: system_info.json")
        print(f"Generated at: {saved_info['timestamp']}")
    except Exception as e:
        print(f"Error saving system info: {e}")

if __name__ == '__main__':
    main()
