import re
import os
import sys

def rewrite_svg_file(completePath):
    file = os.path.basename(completePath)
    file_path = os.path.dirname(completePath)
    # Make sure it's an SVG file
    if file[-4:] == (".svg"):
            content = open(completePath, 'r')
            
            # Read the content of the file
            innerContent = content.read()
            
            # Replace the fill and stroke color with currentColor
            updated_content = re.sub(r'fill="#?[a-zA-Z0-9]{1,20}"', 'fill="currentColor"', innerContent)
            updated_content = re.sub(r'stroke="#?[a-zA-Z0-9]{1,20}"', 'stroke="currentColor"', updated_content)

            # If the SVG has no fill="currentColor" anywhere, add it to the root <svg> tag
            # so the icon inherits the current text color.
            fill_added = False
            if 'fill="currentColor"' not in updated_content:
                updated_content, fill_added = re.subn(
                    r'<svg\b(?![^>]*\bfill=)',
                    '<svg fill="currentColor"',
                    updated_content,
                    count=1,
                )
                fill_added = bool(fill_added)
            # Close the file
            content.close()

            # Open the file in write mode

            # Write the updated content back to the file
            if updated_content != innerContent:
                content = open(completePath, 'w')
                content.write(updated_content)
                if fill_added:
                    print(f'Added fill="currentColor" to the file: "{file}"')
                else:
                    print(f'Changes made to the file: "{file}"')

                # Close the file
                content.close()
            else:
                print(f'No changes made to the file: "{file}"')

            # Erasing any blank space in the file name and capitalize the first letter of each word
            reName = ' '.join([word.capitalize() for word in file.split()])
            reName = reName.replace(" ", "")
            
            # if the file name has a space, it will be removed
            if reName != file:
                newPath = os.path.join(file_path, reName)
                os.rename(completePath, newPath)
                print(f'Renamed : "{file}" -> "{reName}"')

def process_path(path):
    if os.path.isdir(path):
        # Process every SVG inside the folder
        for file in os.listdir(path):
            rewrite_svg_file(os.path.join(path, file))
    else:
        # Process a single file
        rewrite_svg_file(path)

# Paths come from Finder/command line; fall back to the current folder.
paths = sys.argv[1:] or ['./']
for path in paths:
    process_path(path)