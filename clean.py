import sys
import csv
import json

csv_path = sys.argv[1]
write_path = sys.argv[2]
try:
    output_every = int(sys.argv[3])
except:
    output_every = 1000

float_cols = ['select_coef', 'p1_freq', 'p2_freq', 'migr_rate', 'mut_rate', 'recomb_rate']
int_cols = ['position', 'fitness_width', 'n', 'origin_gen', 'output_gen', 'rep']

mapped_keys = {'m': 'migr_rate', 'mu': 'mut_rate', 'r': 'recomb_rate', 'sigsqr': 'fitness_width'}

shared_cols =  ['position', 'select_coef', 'm', 'mu', 'r', 'sigsqr', 'n', 'origin_gen', 'output_gen']
p1_cols = shared_cols + ['p1_freq']
p2_cols = shared_cols + ['p2_freq']

def make_json(csv_path, write_path):

    data = []
    print(output_every)
    with open(csv_path, encoding = 'utf-8') as csvfile:
        csvReader = csv.DictReader(csvfile, delimiter = ' ')
    

        for row in csvReader:
            if row['rep'] == '0':
                row['origin_gen'] = int(row['origin_gen'])
                float_items = { key: float(row[key]) for key in float_cols }
                int_items = { key: int(row[key]) for key in int_cols }
                row.update(float_items)
                row.update(int_items)

                if row['output_gen'] % output_every == 0:
                
                    row['p1_effect'] = row['select_coef'] * row['p1_freq']
                    row['p2_effect'] = row['select_coef'] * row['p2_freq']
                    row['effect_size_freq_diff'] = row['p1_effect'] - row['p2_effect']


                    for key, value in mapped_keys.items():
                        row[key] = row.pop(value)


                    p1_row = { key: row[key] for key in p1_cols }
                    p2_row = { key: row[key] for key in p2_cols }

                    p1_row['effect_size_freq'] = row['p1_effect']
                    p2_row['effect_size_freq'] = row['p2_effect']

                    p1_row['effect_size_freq_diff'] = row['p1_effect'] - row['p2_effect']
                    p2_row['effect_size_freq_diff'] = row['p2_effect'] - row['p1_effect']

                    p1_row['pop'] = 1
                    p2_row['pop'] = 2

                    data.append(p1_row)
                    data.append(p2_row)

                # row['p1_effect'] = row['select_coef'] * row['p1_freq']
                # row['p2_effect'] = row['select_coef'] * row['p2_freq']
                # row['effect_size_freq_diff'] = row['p1_effect'] - row['p2_effect']

                # data.append(row)

        with open(write_path, 'w', encoding = 'utf-8') as jsonfile:
            jsonfile.write(json.dumps(data))

if __name__ == "__main__":  
    make_json(csv_path, write_path)