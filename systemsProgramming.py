import argparse
#input is a mount point
#output is the JSON list of all files + disk usage

def getDiskUsage(mount):
    #TODO from mount find all files, recursively
    #TODO for each file get size in bytes
    #TODO format in JSON
    print("OK")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mount', help= "Mount point")
    args = parser.parse_args()

    #TODO check if mount exists


    if args.mount is not None:
        return(getDiskUsage(args.mount))