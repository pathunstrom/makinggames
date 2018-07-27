import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+", type=Path)
parser.add_argument("-v", dest="verbosity", action="count", default=0)


def count_words(file_object):
    words = 0
    for line in file_object:
        words += len(line.split())
    return words


def count_files(paths, verbosity=0, dry_run=False):
    if verbosity > 0:
        print("Starting count.")
    words = 0
    for path in paths:
        if verbosity > 0:
            print(f"Counting {str(path)}")
        if not dry_run:
            with open(path) as f:
                count = count_words(f)
            if verbosity > 0:
                print(f"{str(path)} contained {count} words.")
            words += count
    if verbosity > 0:
        print("Ending count.")
    return words


if __name__ == "__main__":
    args = parser.parse_args()
    print(count_files(args.files, args.verbosity))
