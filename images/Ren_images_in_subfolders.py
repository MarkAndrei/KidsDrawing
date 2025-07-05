import os
import shutil

def get_image_files(directory):
    """Get all image files from a directory"""
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.tif', '.webp'}
    image_files = []
    
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            _, ext = os.path.splitext(file)
            if ext.lower() in image_extensions:
                image_files.append(file)
    
    return image_files

def rename_images_in_folder(folder_path, folder_name):
    """Rename images in a single folder"""
    print(f"\nProcessing folder: {folder_name}")
    
    # Get all image files
    image_files = get_image_files(folder_path)
    
    if not image_files:
        print(f"  No images found in {folder_name}")
        return
    
    print(f"  Found {len(image_files)} images")
    
    # Separate files that start with "00_" from others
    original_files = [f for f in image_files if f.startswith('00_')]
    other_files = [f for f in image_files if not f.startswith('00_')]
    
    # Sort other files for consistent ordering
    other_files.sort()
    
    # Rename files starting with "00_" to "original.png"
    for i, file in enumerate(original_files):
        old_path = os.path.join(folder_path, file)
        
        if i == 0:
            # First 00_ file becomes "original.png"
            new_name = "original.png"
        else:
            # Additional 00_ files become "original_2.png", "original_3.png", etc.
            new_name = f"original_{i + 1}.png"
        
        new_path = os.path.join(folder_path, new_name)
        
        try:
            # Check if target file already exists
            if os.path.exists(new_path):
                print(f"  Warning: {new_name} already exists, skipping {file}")
                continue
                
            os.rename(old_path, new_path)
            print(f"  Renamed: {file} -> {new_name}")
        except OSError as e:
            print(f"  Error renaming {file}: {e}")
    
    # Rename other files to ai1.png, ai2.png, etc.
    for i, file in enumerate(other_files, 1):
        old_path = os.path.join(folder_path, file)
        new_name = f"ai{i}.png"
        new_path = os.path.join(folder_path, new_name)
        
        try:
            # Check if target file already exists
            if os.path.exists(new_path):
                print(f"  Warning: {new_name} already exists, skipping {file}")
                continue
                
            os.rename(old_path, new_path)
            print(f"  Renamed: {file} -> {new_name}")
        except OSError as e:
            print(f"  Error renaming {file}: {e}")

def rename_all_images():
    """Main function to rename images in all subfolders"""
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Get all subdirectories
    subdirs = [d for d in os.listdir(script_dir) 
               if os.path.isdir(os.path.join(script_dir, d))]
    
    if not subdirs:
        print("No subfolders found in the current directory.")
        return
    
    print(f"Found {len(subdirs)} subfolders to process")
    
    # Process each subfolder
    for subfolder in subdirs:
        subfolder_path = os.path.join(script_dir, subfolder)
        rename_images_in_folder(subfolder_path, subfolder)
    
    print(f"\nImage renaming complete!")

if __name__ == "__main__":
    print("Image Renamer Script")
    print("=" * 30)
    print("This script will:")
    print("- Rename images starting with '00_' to 'original.png'")
    print("- Rename all other images to 'ai1.png', 'ai2.png', etc.")
    print("- Process all subfolders in the current directory")
    print()
    
    # Ask for confirmation before proceeding
    response = input("Continue with image renaming? (y/n): ")
    if response.lower() in ['y', 'yes']:
        rename_all_images()
    else:
        print("Operation cancelled.")