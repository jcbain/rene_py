import argparse
import json

default_output_dir = "/tmp"
default_uniq_params = ['m', 'mu', 'r', 'sigsqr', 'n', 'pop', 'alpha']

def unique(list1):
 
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--files', nargs='+', required=True, action='store', type=str)
    parser.add_argument('-o', '--output', action="store", type=str, default=default_output_dir)
    parser.add_argument('-d', '--dict', action="store", nargs='?', type=str2bool, default='t')
    
    results = parser.parse_args()
    files = results.files
    output_dir = results.output
    save_as_object = results.dict


    if output_dir.endswith('/'):
        output = '{}output_data.json'.format(output_dir)
    else: 
        output = '{}/output_data.json'.format(output_dir)

    
    if(save_as_object):
        final = {}
        for f in files:
            with open(f, encoding='utf-8') as jsonfile:
                data_list = json.load(jsonfile)
                uniq_params = unique([{key: i[key] for key in default_uniq_params if key in i} for i in data_list])  

                data_obj = {}  
                for p_set in uniq_params: 
                    data_param_set = [i for i in data_list if {key: i[key] for key in p_set} == p_set]
                    set_key = "_".join(['{}{:.11f}'.format(k, p_set[k]).rstrip('0').rstrip('.') for k in p_set])
                    data_obj[set_key] = data_param_set
                
            final.update(data_obj)
    else:
        final = []

        for f in files:
            with open(f, encoding='utf-8') as jsonfile:
                data_list = json.load(jsonfile)

            final.extend(data_list)
    
    with open(output, 'w', encoding = 'utf-8') as jsonfile:
        jsonfile.write(json.dumps(final))


if __name__ == "__main__":
    main()