import os
import json

def flat_generator(
        directory: str,
        directoy_filename: str = "directory.json",
        lecture_filename: str = "lecture.json") -> dict:
    if "." not in directoy_filename:
        directoy_filename += ".json"
    directory_path = os.path.join(directory, directoy_filename)
    if '.' not in lecture_filename:
        lecture_filename += ".json"
    lecture_path = os.path.join(directory, lecture_filename)

    if not os.path.isfile(directory_path):
        raise ValueError(f"Expected a file at {directory_path}, but found a directory or invalid file type.")
    if not os.path.isfile(lecture_path):
        raise ValueError(f"Expected a file at {lecture_path}, but found a directory or invalid file type.")
    
    try:
        with open(directory_path, 'r') as file:
            directory_data: dict = json.load(file)
            if not isinstance(directory_data, dict):
                raise ValueError(f"JSON file {directory_path} does not contain a valid JSON object.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in {directory_path}: {e}")
    
    try:
        with open(lecture_path, 'r') as file:
            lecture_data: dict = json.load(file)
            if not isinstance(lecture_data, dict):
                raise ValueError(f"JSON file {lecture_path} does not contain a valid JSON object.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in {lecture_path}: {e}")

    return lecture_data

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    result = flat_generator(current_dir)
    print("Flat generator result:", result)
    print("I am beautiful, I am flat, I am a generator.")