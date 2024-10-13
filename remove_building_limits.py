#!/usr/bin/python3

import sys
import re
import os

pattern1 = "[\r\n\t ]*base_cap_amount[ ]*=[ 0-9]*"
pattern2 = "[\r\n\t ]*empire_limit[ ]*=[ ]*\{[\r\n\t ]*base[ ]*=[ 0-9]*[\r\n\t ]*\}"
pattern3 = "[\r\n\t ]*empire_limit[ ]*=[ 0-9]*"

def files_io(input_path, output_path):
    files = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
    for file in files:
        result = None
        with open(os.path.join(input_path, file), encoding="utf-8") as text:
            result = text_replace(text.read())
        if result:
            with open(os.path.join(output_path, "ub_" + file), 'w', encoding="utf-8") as output_file:
                print(result, file=output_file)

def text_replace(text) -> str:
    if re.search(pattern1, text) or re.search(pattern2, text):
        result = re.sub(pattern1, "", text)
        result = re.sub(pattern2, "", result)
        result = re.sub(pattern3, "", result)
        return result
    else:
        return None

def main(args):
    if len(args) < 2 or args[2] == "-h" or args[2] == "--help":
        print("Usage: python3 remove_building_limits.py <input_path> <output_path>")
    assert(os.path.isdir(args[1]))
    assert(os.path.isdir(args[2]))
    files_io(args[1], args[2])
    print("[>] Processing done successfully.")

if __name__ == "__main__":
    main(sys.argv)