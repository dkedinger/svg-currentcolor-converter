# SVG CurrentColor Converter for React

This Python script is designed to optimize and modify SVG files for use in React applications. It adjusts SVG attributes to make them compatible with React components and ensures a consistent appearance by using the `currentColor` property. Additionally, the script cleans up file names by removing spaces and capitalizing each word for improved organization.

## Features

- **Dynamic Color Handling**:
  - Replaces all `fill` and `stroke` attributes in SVG files with `currentColor` to allow color inheritance from parent components in React.
  - If an SVG has no `fill="currentColor"` anywhere, it adds `fill="currentColor"` to the root `<svg>` tag so the icon still inherits the current text color.

- **File Renaming**:
  - Removes spaces in file names and capitalizes each word for a cleaner naming convention.
  - Example: `my icon.svg` becomes `MyIcon.svg`.

- **Batch Processing**:
  - Processes all SVG files in the specified folder.
  - Skips files without changes and logs the result.

## Usage

### Prerequisites

- Python 3.x

### Instructions

1. Clone this repository or download the script file `svg_currentColor_Converter.py`.

2. Run the script. With no arguments it processes all SVG files in the current directory (`./`):

```bash
python3 svg_currentColor_Converter.py
```

3. The script will process the targeted SVG files, applying the changes and renaming files if needed.

### Specifying Files or Folders

You can pass one or more SVG files and/or folders as arguments. Folders are scanned for SVG files, and individual files are processed directly:

```bash
# A single folder
python3 svg_currentColor_Converter.py /path/to/your/svg/files

# Specific files
python3 svg_currentColor_Converter.py icon-one.svg icon-two.svg

# A mix of files and folders
python3 svg_currentColor_Converter.py ./icons logo.svg
```

## macOS Finder Quick Action

You can run the converter directly from Finder by right-clicking selected SVG files or a folder.

1. Open **Automator** → File → New → **Quick Action**.

2. At the top of the workflow, set:
   - "Workflow receives current" → **files or folders**
   - "in" → **Finder**

3. Add a **Run Shell Script** action and set:
   - **Shell:** `/bin/zsh`
   - **Pass input:** **as arguments**

4. Paste this into the script box (adjust the path to where the script lives):

   ```bash
   /usr/bin/python3 "/path/to/svg_currentColor_Converter.py" "$@"
   ```

   Because input is passed *as arguments*, `"$@"` forwards every selected file/folder to the script.

5. Save (⌘S) with a name like **Convert SVG to currentColor**.

6. Use it: right-click any SVG(s) or a folder in Finder → **Quick Actions** → **Convert SVG to currentColor**.

> **Note:** Finder Quick Actions don't display a terminal, so the script's printed output isn't shown when run this way.

The script uses only the Python standard library, so it runs under the system Python (`/usr/bin/python3`) with no extra installation. If you rely on a Homebrew or pyenv Python, substitute its full path (find it with `which python3`).

## Example Output

### Input
- File: `example icon.svg`
- Content:
  ```svg
  <svg fill="#000000" stroke="#FF5733">
  </svg>
  ```

### Output
- Renamed File: `ExampleIcon.svg`
- Modified Content:
  ```svg
  <svg fill="currentColor" stroke="currentColor">
  </svg>
  ```

## Logging

When run from the command line, the script prints its operations:
- Files modified: `"Changes made to the file: \"ExampleIcon.svg\""`
- Files where `fill="currentColor"` was added: `"Added fill=\"currentColor\" to the file: \"ExampleIcon.svg\""`
- Files without changes: `"No changes made to the file: \"ExampleIcon.svg\""`
- Files renamed: `"Renamed: \"example icon.svg\" -> \"ExampleIcon.svg\""`

(This output is not visible when run via the Finder Quick Action.)

## Notes

- Ensure your SVG files are backed up before running the script.
- The script is case-insensitive when checking file extensions (e.g., `.SVG` is treated the same as `.svg`).

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this script.

---

For questions or contributions, feel free to open an issue or submit a pull request!

