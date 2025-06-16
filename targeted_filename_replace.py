# Created by:       Brad Arrowood
# Created on:       2025.06.05
# Last updated:     2025.06.15
# Script name:      targeted_filename_replace.py
# Version:          4.0
# Description:      Set the target root folder, the text to target and what to replace it with
#                   The 2.0 version targets a root folder and recursively searches all sub-folders (can be disabled)
#                   The 3.0 version allows you to set the replacement_text to be added at the start of the filename (can be disabled)
#                   The 4.0 version adds the ability to inject text at a specific position in filenames (can be disabled)

######################################################################
######################################################################
# Set your root folder path here
folder_path = r"C:\path\to\your\folder"

# Set the text you want to find and replace
# text_to_find is ignored if add_as_header=True or injection=True
text_to_find = "TEXT TO FIND"
replacement_text = "TEXT TO REPLACE WITH"

# Configuration options
# recursive Set whether to process subfolders (True) or just the specified folder (False)
# add_as_header adds replacement_text as prefix
# injection adds replacement_text after X characters (length of text_to_find)
recursive = False
add_as_header = False
injection = False
######################################################################
######################################################################

import os

def replace_in_filenames(folder_path, text_to_find, replacement_text, recursive=False, add_as_header=False, injection=False):
    """
    Replaces specified text in all filenames, adds as prefix, or injects at position in the given folder and optionally its subfolders.
    
    Args:
        folder_path (str): Path to the folder containing files
        text_to_find (str): Text to find in filenames (used to determine position if injection=True)
        replacement_text (str): Text to replace with, add as prefix, or inject
        recursive (bool): Whether to process subfolders recursively (default: False)
        add_as_header (bool): Whether to add replacement_text as prefix (default: False)
        injection (bool): Whether to inject replacement_text after text_to_find length (default: False)
    """
    # Verify the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found - {folder_path}")
        return
    
    renamed_count = 0
    
    print("\nFiles to be renamed:")
    print("-" * 50)
    
    # First pass: show what will be renamed
    for root, dirs, files in os.walk(folder_path):
        if not recursive and root != folder_path:
            continue
            
        for filename in files:
            new_filename = filename
            if add_as_header:
                new_filename = f"{replacement_text}{filename}"
                renamed_count += 1
            elif injection:
                # Calculate position to inject (after text_to_find length)
                inject_pos = len(text_to_find)
                if inject_pos <= len(filename):
                    new_filename = f"{filename[:inject_pos]}{replacement_text}{filename[inject_pos:]}"
                    renamed_count += 1
            elif text_to_find in filename:
                new_filename = filename.replace(text_to_find, replacement_text)
                renamed_count += 1
            
            if new_filename != filename:
                # Get full paths for old and new names
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                
                print(f"{os.path.join(root, filename)}  →  {new_filename}")
    
    if renamed_count == 0:
        print("No matching files found for the specified operation.")
        return
    
    print("\n" + "-" * 50)

    if renamed_count > 0 and recursive == True:
        confirm = input(f"\nAbout to rename {renamed_count} files. Continue? (y/n): ").strip().lower()
        
        if confirm != 'y':
            print("Operation cancelled.")
            return
    
    # Second pass: actually rename the files
    renamed_count = 0
    for root, dirs, files in os.walk(folder_path):
        if not recursive and root != folder_path:
            continue
            
        for filename in files:
            new_filename = filename
            if add_as_header:
                new_filename = f"{replacement_text}{filename}"
            elif injection:
                inject_pos = len(text_to_find)
                if inject_pos <= len(filename):
                    new_filename = f"{filename[:inject_pos]}{replacement_text}{filename[inject_pos:]}"
            elif text_to_find in filename:
                new_filename = filename.replace(text_to_find, replacement_text)
            
            if new_filename != filename:
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                
                try:
                    os.rename(old_path, new_path)
                    renamed_count += 1
                except Exception as e:
                    print(f"Error renaming {os.path.join(root, filename)}: {e}")
    
    print(f"\nSuccessfully renamed {renamed_count} files.")

if __name__ == "__main__":
    
    if add_as_header and injection:
        print("\nWarning: Both add_as_header and injection are set as True. Please only set one to True at a time")
        exit

    # Run the replacement function
    replace_in_filenames(folder_path, text_to_find, replacement_text, recursive, add_as_header, injection)
