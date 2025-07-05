import os
import re

def rename_folders():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get all subdirectories
    subdirs = [d for d in os.listdir(script_dir) 
               if os.path.isdir(os.path.join(script_dir, d))]
    
    # Pattern to match existing drawing folders (drawing followed by 4 digits)
    pattern = r'^drawing(\d{4})$'
    
    # Find existing drawing folders and their numbers
    existing_numbers = []
    folders_to_rename = []
    
    for folder in subdirs:
        match = re.match(pattern, folder)
        if match:
            # This folder already follows the pattern
            existing_numbers.append(int(match.group(1)))
            print(f"Found existing: {folder}")
        else:
            # This folder needs to be renamed
            folders_to_rename.append(folder)
    
    # Sort existing numbers to find the next available number
    existing_numbers.sort()
    
    # Find the next available number
    next_number = 1
    for num in existing_numbers:
        if num == next_number:
            next_number += 1
        else:
            break
    
    print(f"\nStarting renaming from drawing{next_number:04d}")
    print(f"Folders to rename: {len(folders_to_rename)}")
    
    # Rename folders that don't follow the pattern
    for i, folder in enumerate(folders_to_rename):
        old_path = os.path.join(script_dir, folder)
        new_name = f"drawing{next_number + i:04d}"
        new_path = os.path.join(script_dir, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: '{folder}' -> '{new_name}'")
        except OSError as e:
            print(f"Error renaming '{folder}': {e}")
    
    print(f"\nRenaming complete!")

if __name__ == "__main__":
    print("Folder Renamer Script")
    print("=" * 30)
    
    # Ask for confirmation before proceeding
    response = input("This will rename folders in the current directory. Continue? (y/n): ")
    if response.lower() in ['y', 'yes']:
        rename_folders()
    else:
        print("Operation cancelled.")