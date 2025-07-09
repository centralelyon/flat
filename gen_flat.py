import os
import json


def list_items_in_directory(directory_path):
    try:
        items = []
        for entry in os.listdir(directory_path):
            if entry.startswith('.'):
                continue  # Ignore les fichiers cachés
            full_path = os.path.join(directory_path, entry)
            items.append({
                "name": entry,
                "path": full_path,
                "is_file": os.path.isfile(full_path),
                "is_dir": os.path.isdir(full_path)
            })
        # Structure avec le nom du dossier racine
        result = items
        with open("flat_dir_1_file_txt.json", "w") as json_file:
            json.dump(result, json_file, indent=4)
    except Exception as e:
        print(f"Erreur : {e}")

def compare_json_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)
            if data1 == data2:
                print("Les fichiers JSON sont identiques.")
            else:
                print("Les fichiers JSON sont différents.")
    except Exception as e:
        print(f"Erreur lors de la comparaison : {e}")

if __name__ == "__main__":
    folder_path = "dir_1_file_txt"  # Dossier à lister
    list_items_in_directory(folder_path)
    compare_json_files("flat_dir_1_file_txt.json", "flat_dir_1_file_txt_result.json")

