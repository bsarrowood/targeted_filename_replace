
This Python script was made to more effienctly batch rename files from those with a fairly repeat naming schemes into something more desired and structured.
It has the capabilitiy to find specific text within the file name to replace with a different set string, add text to the beginning of file names, and
inject text at set a character count within file names. It also has the ability to do this for a single folder path or use recursive to search all sub-folders for file names to rename.

This Python script has 6 main variables:
  * folder_path = Set the path to the folder or parent folder
  * text_to_find = Set the text that the script will search for in the file names
  * replacement_text = Set what you want to replace the found text above
  * recursive = Set False if you only want the script to search the target folder or True if you want it to search all sub-folders
  * add_as_header = Set to True and the text_to_find is ignored while the replacement_text as added to the beginning of every file
  * injection = Set to True and the script will do a character count from the text_to_find string and inject the replacement_text after that many characters in the file names

The add_as_header and injection modifiers can be individually run with the recursive variable, but I've put a safety stop if both add_as_header and injection are set to True.
