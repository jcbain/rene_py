import os
import argparse
from cleaners import cleaners

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--directory', required=True, action="store", type=str)
    parser.add_argument('-n', '--newdirectory', action="store", type=str, default='images')

    results = parser.parse_args()

    directory = results.directory
    string_directory = results.newdirectory
    files = os.listdir(directory)

    all_output_strings = [cleaners.create_latex_string(img, string_directory) for img in files]
    output_string = "\n\n".join(all_output_strings)

    print(output_string)


if __name__ == "__main__":
    main()