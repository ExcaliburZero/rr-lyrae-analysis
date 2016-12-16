"""
Batch script creator for Period04.

Based on a script made by Dylan Richmond.
"""
from __future__ import print_function
import os
import sys


def main():
    # Make sure that sufficient cli arguments have been given
    if not len(sys.argv) == 3:
        error("Invalid arguments, proper arguments are:")
        error("\tpython period04batchscriptor.py INPUT_FILES_DIRECTORY OUTPUT_FILE\n")
        error("Example:")
        error("\tpython period04batchscriptor.py ~/Downloads/one period04freqs.per")
        sys.exit(1)

    # Get the input and outputs from the cli arguments
    input_dir = sys.argv[1]
    output_file = sys.argv[2]

    # Create the batch file and print it out
    batch_file = create_batch_file(input_dir, output_file)
    print(batch_file)


def create_batch_file(input_dir, output_file):
    path = os.path.abspath(input_dir)
    fourier = 'fourier 0 20 o n'

    batch_file = ""
    for file in sorted(os.listdir(path)):
        is_dat = file[-4:] == ".dat"
        if is_dat:
            file_path = os.path.join(path, file)
            batch_file += 'import tou %s' % file_path + "\n"
            batch_file += fourier + "\n"

    batch_file += "savefreqs %s" % output_file + "\n"
    batch_file += "exit" + "\n"

    return batch_file


def error(message):
    print(message, file=sys.stderr)

# Run the main method of the script
if __name__ == '__main__':
    main()
