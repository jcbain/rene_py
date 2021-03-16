import argparse
import json

default_output_file = "/tmp/output_template.json"

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--numloci', required=True, action='store', type=int)
    parser.add_argument('-o', '--output', type=str, default=default_output_file)

    results = parser.parse_args()
    n = results.numloci
    write_path = results.output

    data = []

    for i in range(n):
        row = {'genome_scaffold': 'g1', 'position': i + 1, 'gene': i}
        data.append(row)
    
    with open(write_path, 'w', encoding = 'utf-8') as jsonfile:
        jsonfile.write(json.dumps(data))

if __name__ == "__main__":
    main()