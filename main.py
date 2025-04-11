from src.Interpreter import forth_interpreter
import sys
import os

# Ensure a file argument is provided
if len(sys.argv) < 2:
    print("Usage: python main.py <file>")
    sys.exit(1)

file_path = sys.argv[1]

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

# Read source file
with open(file_path, 'r') as f:
    source = f.read()

# Run the interpreter
forth_interpreter(source,sys.argv)
