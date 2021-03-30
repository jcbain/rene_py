import argparse
import csv
import json

default_output_file = "/tmp/output_cleaned.json"

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', required=True, action="store", type=str)
    parser.add_argument('-r', '--remove', required=True, action="store", type=str)
    parser.add_argument('-o', '--output', action="store", type=str, default=default_output_file)
    results = parser.parse_args()

    infile = results.input
    to_remove = results.remove
    write_path = results.output
    # print(results)
    with open(infile, encoding='utf-8') as jsonfile:
        data_list = json.load(jsonfile)

        removal_keys = [v for v in dict.keys(data_list) if to_remove in v]

        for key in removal_keys:
            del data_list[key]

    with open(write_path, 'w', encoding = 'utf-8') as jsonfile:
        jsonfile.write(json.dumps(data_list))

        

        

if __name__ == "__main__":
    main()