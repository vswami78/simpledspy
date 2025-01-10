#!/usr/bin/env python3
import sys
import argparse
from simpledspy import pipe

def main():
    parser = argparse.ArgumentParser(description="SimpleDSPy command line interface")
    parser.add_argument('inputs', nargs='+', help="Input strings to process")
    parser.add_argument('-d', '--description', help="Description of the processing task")
    
    args = parser.parse_args()
    
    # Process inputs
    result = pipe(*args.inputs, description=args.description)
    
    # Print results
    if isinstance(result, tuple):
        for i, res in enumerate(result, 1):
            print(f"Output {i}: {res}")
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
