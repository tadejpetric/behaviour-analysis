import sys


def dispatch(in_name, out_name):
    with open(in_name, 'r') as inf, open(out_name, 'w') as outf:
        working_string = ""
        peoplecount = 0
        for line in inf:
            try:
                keyword, rest = line.split(' ', 1)
            except ValueError:
                # Happens on unfortunate interrupts
                continue
            if keyword == "Warning:":
                continue
            elif keyword == "people":
                peoplecount = int(rest.strip())
            working_string += line
            if line == "--- 1\n":
                if peoplecount == 2:
                    outf.write(working_string)
                working_string = ""


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Prilozi datoteko za pretvorbo v csv")
        print("Uporaba: python prepare_file.py <input_file> <output_file>")
        sys.exit()
    dispatch(sys.argv[1], sys.argv[2])
