import argparse
import os


def printhelp():
    print("interface for running csv parser and preparation on batches")
    print("Usage:")
    print("Use `help` to display this message")
    print("Use `prepare` to call the preparation parser")
    print("\t\tpython interface.py prepare --inputs <input_dir> --outputs <output_dir>")
    print("Use `csv` to call the conversion to csv")
    print("\t\tpython interface.py csv --inputs <input_dir> --outputs <output_dir>")


def prepare(iny, outy):
    import prepare_file
    for x in os.listdir(iny):
        prepare_file.dispatch(os.path.join(iny, x), os.path.join(outy, x))


def prep_csv(iny, outy):
    import tocsv
    for x in os.listdir(iny):
        if x[-4:] == ".txt":
            xout = x[:-4] + ".csv"
            tocsv.dispatch(os.path.join(iny, x), os.path.join(outy, xout))


if __name__ == '__main__':
    parser_m = argparse.ArgumentParser()
    parser_m.add_argument("operation", help="The action to perform")
    parser_m.add_argument("--inputs", help="the directory where we are reading from")
    parser_m.add_argument("--outputs", help="the directory we are writing to")
    args = parser_m.parse_args()
    if args.operation in ["help", "?"]:
        printhelp()
    elif args.operation == "prepare":
        prepare(args.inputs, args.outputs)
    elif args.operation == "csv":
        prep_csv(args.inputs, args.outputs)
