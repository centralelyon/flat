import os
import json

def list_items_in_directory(directory_path):
    try:
        items = []
        for entry in os.listdir(directory_path):
            full_path = os.path.join(directory_path, entry)
            items.append({
                "name": entry,
                "path": full_path,
                "is_file": os.path.isfile(full_path),
                "is_dir": os.path.isdir(full_path)
            })

        with open("flat.json", "w") as json_file:
            json.dump(items, json_file, indent=4)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder_path = "."  # Current directory
    list_items_in_directory(folder_path)
