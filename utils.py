#!/usr/bin/env python3
"""
Utility functions for the test repository application.

This module contains helper functions for common operations
including file handling, data validation, and system utilities.
"""

import os
import sys
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Any, Optional


def get_file_size(filepath: str) -> int:
    """Get the size of a file in bytes."""
    try:
        return os.path.getsize(filepath)
    except OSError:
        return 0


def calculate_file_hash(filepath: str, algorithm: str = 'md5') -> Optional[str]:
    """Calculate hash of a file using specified algorithm."""
    try:
        hash_obj = hashlib.new(algorithm)
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except (OSError, ValueError):
        return None


def validate_json_file(filepath: str) -> bool:
    """Validate if a file contains valid JSON."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json.load(f)
        return True
    except (json.JSONDecodeError, OSError):
        return False


def get_system_info() -> Dict[str, str]:
    """Get system information as a dictionary."""
    return {
        'platform': sys.platform,
        'python_version': sys.version.split()[0],
        'current_dir': os.getcwd(),
        'user': os.environ.get('USER', 'unknown'),
        'timestamp': datetime.now().isoformat()
    }


def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"


def backup_file(filepath: str, backup_dir: str = 'backups') -> bool:
    """Create a backup of a file."""
    try:
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = os.path.basename(filepath)
        backup_path = os.path.join(backup_dir, f"{filename}_{timestamp}.bak")
        
        with open(filepath, 'rb') as src, open(backup_path, 'wb') as dst:
            dst.write(src.read())
        return True
    except OSError:
        return False


def list_files_by_extension(directory: str, extension: str) -> List[str]:
    """List all files with a specific extension in a directory."""
    try:
        extension = extension.lower().lstrip('.')
        return [
            f for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(f'.{extension}')
        ]
    except OSError:
        return []


def create_summary_report(directory: str = '.') -> Dict[str, Any]:
    """Create a summary report of files in a directory."""
    stats = {
        'total_files': 0,
        'total_size': 0,
        'file_types': {},
        'largest_file': {'name': '', 'size': 0},
        'generated_at': datetime.now().isoformat()
    }
    
    try:
        for root, dirs, files in os.walk(directory):
            # Skip hidden directories and .git
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                if file.startswith('.'):
                    continue
                    
                filepath = os.path.join(root, file)
                size = get_file_size(filepath)
                
                stats['total_files'] += 1
                stats['total_size'] += size
                
                # Track file types
                ext = os.path.splitext(file)[1].lower() or 'no_extension'
                stats['file_types'][ext] = stats['file_types'].get(ext, 0) + 1
                
                # Track largest file
                if size > stats['largest_file']['size']:
                    stats['largest_file'] = {'name': file, 'size': size}
    
    except OSError:
        pass
    
    stats['total_size_formatted'] = format_file_size(stats['total_size'])
    return stats


if __name__ == '__main__':
    # Demo utility functions
    print("=== Utility Functions Demo ===")
    
    # System info
    sys_info = get_system_info()
    print(f"\nSystem Info:")
    for key, value in sys_info.items():
        print(f"  {key}: {value}")
    
    # Directory summary
    print(f"\nDirectory Summary:")
    summary = create_summary_report('.')
    print(f"  Total files: {summary['total_files']}")
    print(f"  Total size: {summary['total_size_formatted']}")
    print(f"  Largest file: {summary['largest_file']['name']} ({format_file_size(summary['largest_file']['size'])})")
    print(f"  File types: {summary['file_types']}")
