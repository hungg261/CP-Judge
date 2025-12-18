import os

def FilenameSet(directory):
    stems = set()

    for name in os.listdir(directory):
        full_path = os.path.join(directory, name)

        if os.path.isfile(full_path):
            stem, _ = os.path.splitext(name)
            stems.add(stem)

    return stems

def Scan(directory, outputSet):
    files = os.listdir(directory)
    
    if not files:
        print(f"The directory {directory} is empty.")
    
    files.sort()
    
    for file in files:
        file_name, file_path = os.path.splitext(file)
        print(file_name, file_path)
        
        print(outputSet.insert)
        

# Example usage with a corrected path
directory_path = "src/data/inputs"  # Use forward slashes or double backslashes
Scan(directory_path)
