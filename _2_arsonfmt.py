#!/usr/bin/env python3
import os
import subprocess

def main():
    # Starting directory (current working directory)
    root_dir = os.getcwd()

    # Walk through all subdirectories
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # Check for .dta files (case insensitive)
            if filename.lower().endswith(".dta"):
                full_path = os.path.join(dirpath, filename)
                print(f"Running: arsonfmt '{full_path}'")
                # Run the external command arsonfmt on the file.
                result = subprocess.run(["/Users/jnack/Documents/GitHub/arson/target/debug/arson-fmt", full_path])
                
                if result.returncode != 0:
                    print(f"Error: arsonfmt failed on '{full_path}'")
                else:
                    print(f"Successfully processed '{full_path}'")

if __name__ == "__main__":
    main()
