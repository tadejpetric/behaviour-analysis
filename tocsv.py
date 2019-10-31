import glob_vars
import sys


def csv_filename(filename):
    newfilename = ""
    for char in filename:
        if char != ".":
            newfilename += char
        else:
            break
    return newfilename + ".csv"


def dispatch(filename):
    newfilename = csv_filename(filename)
    with open(filename, "r") as fread, open(newfilename, "w") as fwrite:
        for line in fread:


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Priloži datoteko za pretvorbo v csv")
        sys.exit()
    dispatch(filename)
