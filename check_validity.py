import os
import json



def check_directory_validity(dir_path: str, filename="directory.json") -> bool:
    if "." not in filename:
        filename += ".json"
    directory_path = os.path.join(dir_path, filename)

    if not os.path.isfile(directory_path):
        raise ValueError(f"Expected a file at {directory_path}, but found a directory or invalid file type.")
    
    try:
        with open(directory_path, 'r') as file:
            data:dict = json.load(file)
            if not isinstance(data, dict):
                raise ValueError(f"JSON file {directory_path} does not contain a valid JSON object.")
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in {directory_path}: {e}")
    
    if "directory" not in data:
        raise ValueError(f"JSON file {directory_path} does not contain the required 'directory' key.")

    path:str = data["directory"]
    if not isinstance(path, str):
        raise ValueError(f"Expected 'directory' to be a string, but found {type(path).__name__} in {directory_path}.")
    
    paths = path.split("/")
    if paths[-1].lower() not in ["file", "files", ""]:
        raise ValueError(f"The last part of the path '{paths[-1]}' in {directory_path} is not a valid file or directory name.")
    
    if "exclude" in data:
        exclude_paths:dict = data["exclude"]
        if not isinstance(exclude_paths, dict):
            raise ValueError(f"Expected 'exclude' to be a dict, but found {type(exclude_paths).__name__}.")
        
        for keys in exclude_paths:
            if not isinstance(keys, str):
                raise ValueError(f"Invalid type in 'exclude' list: {keys} is not a string.")
            if keys not in paths:
                raise ValueError(f"Path '{keys}' in 'exclude' does not match any part of the directory path in {directory_path}.")
    return True



def check_lecture_validity(dir_path: str, filename="lecture.json") -> bool:
    if "." not in filename:
        filename += ".json"
    lecture_path = os.path.join(dir_path, filename)

    if not os.path.isfile(lecture_path):
        raise ValueError(f"Expected a file at {lecture_path}, but found a directory or invalid file type.")
    
    try:
        with open(lecture_path, 'r') as file:
            data:dict = json.load(file)
            if not isinstance(data, dict):
                raise ValueError(f"JSON file {lecture_path} does not contain a valid JSON object.")
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in {lecture_path}: {e}")

    for key in data:
        if not isinstance(key, str):
            raise ValueError(f"Invalid type in JSON keys: {key} is not a string.")
        if not isinstance(data[key], dict):
            raise ValueError(f"Expected value for key '{key}' to be a dict, but found {type(data[key]).__name__}.")
        
        if "type" not in data[key]:
            raise ValueError(f"Key '{key}' in {lecture_path} does not contain the required 'type' key.")

        if data[key]["type"] not in ["list", "include", "important", "string"]:
            raise ValueError(f"Invalid type '{data[key]['type']}' for key '{key}' in {lecture_path}. Expected 'list', 'file', or 'directory'.")
        
        if "extension" not in data[key]:
            raise ValueError(f"Key '{key}' in {lecture_path} does not contain the required 'extension' key.")
        if not isinstance(data[key]["extension"], str):
            raise ValueError(f"Expected 'extension' for key '{key}' to be a string, but found {type(data[key]['extension']).__name__} in {lecture_path}.")
        
        extensions:list[str] = data[key]["extension"].split("|")
        for ext in extensions:
            if ext != ext.strip():
                print(f"Extension '{ext}' in key '{key}' of {lecture_path} contains leading or trailing whitespace.")
    
    return True



if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    value = check_directory_validity(current_dir)
    value2 = check_lecture_validity(current_dir)
    if value:
        print("This file is valid and has no issues.")