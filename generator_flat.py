import os
import json
import check_validity as ch

def flat_generator(
        directory: str,
        directory_filename: str = "directory.json",
        lecture_filename: str = "lecture.json") -> list:
    """    Generate a flat list of files and directories based on the provided directory and lecture JSON files.
    Args:
        directory (str): The path to the directory containing the JSON files.
        directory_filename (str): The name of the directory JSON file. Defaults to "directory.json".
        lecture_filename (str): The name of the lecture JSON file. Defaults to "lecture.json".
    Returns:
        list: A flat list of dictionaries containing the directory structure and files.
    Raises:
        ValueError: If the directory or lecture JSON files are not found, are not valid JSON objects, or do not contain the required keys.
    """
    if "." not in directory_filename:
        directory_filename += ".json"
    directory_path = os.path.join(directory, directory_filename)
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
    
    if not ch.check_directory_validity(directory, directory_filename):
        raise ValueError(f"Directory validity check failed for {directory_path}.")
    if not ch.check_lecture_validity(directory, lecture_filename):
        raise ValueError(f"Lecture validity check failed for {lecture_path}.")
    
    dir:str = directory_data['directory']
    dir_depth = len(dir.split('/'))-1
    if dir_depth == 0:
        raise ValueError(f"Directory depth is zero for {directory_path}. Please check the directory structure.")
    
    flat = []

    if dir.split('/')[-1] == "":
        print("case empty directory")
        correct_dir:list[str] = listingSubDir(directory, directory_data, dir_depth)
            
        corrected_dir = [d[len(directory)+1:] for d in correct_dir if d.startswith(directory)]

        if len(corrected_dir) == 0 or len(corrected_dir) != len(correct_dir):
            raise ValueError(f"Directory structure is not valid for {directory}. Please check the directory structure.")
        print(corrected_dir)
        for direc in corrected_dir:
            if not os.path.isdir(os.path.join(directory, direc)):
                raise ValueError(f"Directory {direc} does not exist in {directory}.")

            files = filesExclude(os.path.join(directory, direc), directory_data)
            new_flat: dict[str, list[str]|str] = {}
            for index in range(min(len(dir.split('/'))-1, len(direc.split('\\')))):
                new_flat[dir.split('/')[index]] = direc.split('\\')[index]
            
            for keys in lecture_data.keys():

                if lecture_data[keys]['type'] == 'include':
                    for ext in lecture_data[keys]['extension'].split('|'):
                        ext = ext.strip()
                        if ext:
                            new_flat[keys] = [f for f in files if f.endswith(ext)]
                elif lecture_data[keys]['type'] == 'list':
                    for ext in lecture_data[keys]['extension'].split('|'):
                        ext = ext.strip()
                        if ext:
                            new_flat[keys] = [f for f in files if f.endswith(keys+'.'+ext)]
                elif lecture_data[keys]['type'] == 'string':
                    filename = [f for f in files if f.endswith(keys+'.'+lecture_data[keys]['extension'])]
                    if filename:
                        new_flat[keys] = filename[0]
                    else:
                        new_flat[keys] = ""
                elif lecture_data[keys]['type'] == 'important':
                    for ext in lecture_data[keys]['extension'].split('|'):
                        ext = ext.strip()
                        if ext:
                            # Implementation can change for the list of files
                            new_flat["all_" + keys] = [f for f in files if f.endswith(keys+'.'+ext) and f!=keys+'.'+ext and not f.endswith('__'+keys+'.'+ext)]
                            filename = [f for f in files if f.endswith(keys+'.'+ext) and (f==keys+'.'+ext or  f.endswith('__'+keys+'.'+ext))]
                            if filename:
                                new_flat["validate_" + keys] = filename[0]
                            else:
                                new_flat["validate_" + keys] = ""
                    

            flat.append(new_flat)

    elif dir.split('/')[-1] == "file":
        print("case file directory")
        correct_dir:list[str] = listingSubDir(directory, directory_data, dir_depth)

        corrected_dir = [d[len(directory)+1:] for d in correct_dir if d.startswith(directory)]

        if len(corrected_dir) == 0 or len(corrected_dir) != len(correct_dir):
            raise ValueError(f"Directory structure is not valid for {directory}. Please check the directory structure.")
            
        for direc in corrected_dir:
            if not os.path.isdir(os.path.join(directory, direc)):
                raise ValueError(f"Directory {direc} does not exist in {directory}.")
            files = filesExclude(os.path.join(directory, direc), directory_data)
            only_files = [f for f in files if os.path.isfile(os.path.join(directory, direc, f))]
            for only_file in only_files:
                new_flat: dict[str, list[str]|str] = {}
                for index in range(min(len(dir.split('/'))-1, len(direc.split('\\')))):
                    new_flat[dir.split('/')[index]] = direc.split('\\')[index]
                new_flat['file'] = only_file
                flat.append(new_flat)

    elif dir.split('/')[-1] == "files":
        print("case files directory")
        correct_dir:list[str] = listingSubDir(directory, directory_data, dir_depth, False)

        corrected_dir = [d[len(directory)+1:] for d in correct_dir if d.startswith(directory)]

        if len(corrected_dir) == 0 or len(corrected_dir) != len(correct_dir):
            raise ValueError(f"Directory structure is not valid for {directory}. Please check the directory structure.")
            
        for direc in corrected_dir:
            if not os.path.isdir(os.path.join(directory, direc)):
                raise ValueError(f"Directory {direc} does not exist in {directory}.")
            
            files = filesExclude(os.path.join(directory, direc), directory_data)
            only_files = [f for f in files if os.path.isfile(os.path.join(directory, direc, f))]
            for only_file in only_files:
                new_flat: dict[str, list[str]|str] = {}
                for index in range(min(len(dir.split('/'))-1, len(direc.split('\\')))):
                    new_flat[dir.split('/')[index]] = direc.split('\\')[index]
                new_flat['file'] = only_file
                flat.append(new_flat)
        
    
    return flat


def listingSubDir(
    directory:str,
    directory_json:dict={},
    depth: int = 0,
    lastOnly:bool = True
) -> list[str]:
    """
    List all subdirectories in a given directory up to a specified depth.

    Args:
        directory (str): The path to the directory to list.
        directory_json (dict): The JSON data containing the directory structure and exclusions.
        depth (int): The depth to which subdirectories should be listed. Defaults to 0
        lastOnly (bool): If True, only return the directories at the last depth. Defaults to True.

    Returns:
        list[str]: A list of subdirectories at the specified depth, or all subdirectories if `lastOnly` is False.
    """
    exclude: dict = directory_json.get("exclude", {})

    current_list_directory:list[str] = [directory]
    all_directories:list[str] = []
    list_directory:list[str] = []

    count = 0
    while depth > 0:
        name = directory_json["directory"].split("/")[count]
        list_exclude:list[str] = []
        list_start_exclude:list[str] = []
        if name in exclude:
            list_exclude = [n for n in exclude[name] if n.endswith('/') or n.endswith('\\')]
            list_start_exclude = [n for n in exclude[name] if n.endswith('*')]

        new_list_directory = []
        print(list_exclude, list_start_exclude)
        for current_directory in current_list_directory:
            new_directory = os.listdir(current_directory)
            new_list_directory.extend([os.path.join(current_directory, d) for d in new_directory
                                       if os.path.isdir(os.path.join(current_directory, d))
                                       and d not in list_exclude
                                       and not any(d.startswith(start_exclude[:-2]) for start_exclude in list_start_exclude)])


        all_directories.extend(new_list_directory)
        if depth == 1: # if we are at the last depth, we want all directories
            list_directory.extend(new_list_directory)

        current_list_directory = new_list_directory.copy()
        depth -= 1
        count += 1
    if lastOnly:
        return list_directory
    else:
        return all_directories

def filesExclude(directory: str, directory_json: dict) -> list[str]:
    """
    Exclude files from a directory based on the exclude dictionary.
    
    Args:
        directory (str): The path to the directory to list files from.
        directory_json (dict): The JSON data containing the directory structure and exclusions.
    
    Returns:
        list[str]: A list of files in the directory that are not excluded.
    """
    files = os.listdir(directory)
    exclude: dict = directory_json.get("exclude", {})
    excluded_files = []
    
    for key, patterns in exclude.items():
        for pattern in patterns:
            if pattern.endswith('*'):
                pattern = pattern[:-1]  # Remove the trailing '*'
                excluded_files.extend([f for f in files if f.startswith(pattern)])
            else:
                excluded_files.extend([f for f in files if f == pattern])
    
    return [f for f in files if f not in excluded_files]

def export_json(data: list, path: str) -> None:
    """
    Export data to a JSON file.
    Args:
        data (list): The data to export.
        path (str): The path where the JSON file will be saved.
    Returns:
        None
    """
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
        

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    result = flat_generator(current_dir)
    print("Flat generator result:", result)
    print("I am beautiful, I am flat, I am a generator.")