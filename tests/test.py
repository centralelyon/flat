import sys
import os
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from generator_flat import flat_generator, export_json  # noqa: E402

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    result = flat_generator(current_dir, lecture_filename="lecture.json")
    #result2 = flat_generator(current_dir, lecture_filename="lecture2.json")
    #result3 = flat_generator(current_dir, lecture_filename="lecture2.json", directory_filename="directory2.json")
    #result4 = flat_generator(current_dir, lecture_filename="lecture.json", directory_filename="directory3.json")
    #result5 = flat_generator(current_dir, lecture_filename="lecture2.json", directory_filename="directory3.json")
    #result6 = flat_generator(current_dir, lecture_filename="lecture3.json", directory_filename="directory3.json")
    print("Flat generator result:", result)
    export_json(result, current_dir+"/flat.json")
    #print("Flat generator result:", result2)
    #print("Flat generator result:", result3)
    #print("Flat generator result:", result4)
    #print("Flat generator result:", result5)
    #print("Flat generator result:", result6)