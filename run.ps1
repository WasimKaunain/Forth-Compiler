



# #!/bin/bash

# # Check if a file argument is provided

# if [ $# -ne 1 ]; then
#     echo "Usage: $0 <file>"
#     exit 1
# fi
# FILE=$1

# # Check if the file exists
# if [ ! -f "$FILE" ]; then
#     echo "Error: File '$FILE' not found."
#     exit 1
# fi

# # Run the program using the interpreter
# python3 main.py "$FILE"


# Check if a file argument is provided
if ($args.Count -ne 1) {
    Write-Host "Usage: .\run.ps1 <file>"
    exit 1
}

$file = $args[0]

# Check if the file exists
if (-Not (Test-Path $file)) {
    Write-Host "Error: File '$file' not found."
    exit 1
}

# Run the program using the interpreter
python main.py $file
