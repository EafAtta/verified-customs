#!/usr/bin/env python3
import os
import subprocess
import shutil

def main():
    # Folder where processed (moved) files will be stored
    processed_dir = "_processed"
    os.makedirs(processed_dir, exist_ok=True)
    
    # Get the current working directory (where both files and extraction folders reside)
    cwd = os.getcwd()
    
    for filename in os.listdir(cwd):
        full_path = os.path.join(cwd, filename)
        
        # Process only files that have no extension.
        if os.path.isfile(full_path) and os.path.splitext(filename)[1] == '':
            print(f"Running: onyx extract '{full_path}'")
            
            # Run the extraction command
            result = subprocess.run(["/Applications/Onyx.app/Contents/MacOS/onyx", "extract", full_path])
            
            if result.returncode == 0:
                print(f"Extraction succeeded for: {filename}")
                
                # Move the original file to the _processed folder.
                dest_file = os.path.join(processed_dir, filename)
                shutil.move(full_path, dest_file)
                print(f"Moved file '{filename}' to '{processed_dir}'")
                
                # The extraction process creates a folder with the file's name plus "_extract".
                extraction_folder = os.path.join(cwd, f"{filename}_extract")
                if os.path.isdir(extraction_folder):
                    # New name: remove the "_extract" suffix.
                    new_folder_name = os.path.join(cwd, filename)
                    
                    # Check to avoid renaming if something with the target name already exists.
                    if os.path.exists(new_folder_name):
                        print(f"Warning: Cannot rename '{extraction_folder}' to '{new_folder_name}' because the target already exists.")
                    else:
                        os.rename(extraction_folder, new_folder_name)
                        print(f"Renamed extraction folder from '{extraction_folder}' to '{new_folder_name}'")
                else:
                    print(f"Warning: Expected extraction folder '{filename}_extract' not found.")
            else:
                print(f"Extraction failed for: {filename}")

if __name__ == "__main__":
    main()
