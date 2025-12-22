import shutil
from pathlib import Path

def cleanup_subworkspaces(root_folder, pattern = "*"):
    root = Path(root_folder)
    for path in root.rglob(pattern):
        if path.is_dir():
            shutil.rmtree(path)

def cleanup_workspaces(pattern="*"):
    cleanup_subworkspaces("src/data", pattern)
    cleanup_subworkspaces("src/scripts", pattern)
    
if __name__ == "__main__":
    cleanup_workspaces()