import argparse
import json
from pathlib import Path
import os
#input is a mount point
#output is the JSON list of all files + disk usage

def getDiskUsage(path):
    # from mount find all files, recursively
    # for each file get size in bytes
    # format in JSON
    files = []
    for fileName in path.rglob("*.*"):
        if not fileName.is_dir():    
            print(fileName)
            fileSize = Path(fileName).stat().st_size
            #fileSize = os.path(fileName).getsize()
            files.append("{0},{1}".format(fileName, fileSize))
    data = {"files": files}
    return json.dumps(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mount', help= "Mount point")
    args = parser.parse_args()
    
    path = Path(args.mount)
    if not path.is_dir():
        print("{0} is not a directory".format(args.mount))
    else:
        print(getDiskUsage(path))