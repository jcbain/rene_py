import argparse
import json

default_output_file = "/tmp/output.json"

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--files', nargs='+', required=True, action='store', type=str)
    parser.add_argument('-o', '--output', action="store", type=str, default=default_output_file)

    results = parser.parse_args()
    files = results.files
    output = results.output

    final = []
    for f in files:
        with open(f, encoding='utf-8') as jsonfile:
            j = json.load(jsonfile)
            final.extend(j)
    
    with open(output, 'w', encoding = 'utf-8') as jsonfile:
        jsonfile.write(json.dumps(final))

if __name__ == "__main__":
    main()