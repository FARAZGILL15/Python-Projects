# automation_script_intermediate.py
import os
from pathlib import Path

folder = Path("./files")  # Folder with files to organize
if not folder.exists():
    folder.mkdir()

for file in folder.iterdir():
    if file.is_file():
        ext = file.suffix[1:] or "other"  # Get file extension
        dest = folder / ext
        dest.mkdir(exist_ok=True)
        file.rename(dest / file.name)

print("Files have been organized by type!")
