import csv
import argparse
import itertools

def file_to_list(file):
    retail_list = []
    with open(file) as f:
        reader = csv.reader(f, skipinitialspace=False,delimiter=' ', quoting=csv.QUOTE_NONE)
        for row in reader:
            retail_list.append(row)

    for i in retail_list:
        i.remove('')
    return retail_list

def supermarket_optimization(sigma, file):
    comb_freq_dict = dict()

    #this just converts the file into a list of lists and removes unnecessary whitespaces
    retail_list = file_to_list(file)

    #first optimization
    new_retail_list = less_than_three(retail_list)

    #second optimization
    sorted_retail_list = sorted(new_retail_list, key=len)

    for x in range(len(sorted_retail_list)):
        comb_list = list(itertools.combinations(sorted_retail_list[x], 3))
        for i in comb_list:
            if i not in comb_freq_dict:
                comb_freq_dict[i] = 1
            else:
                comb_freq_dict[i] = comb_freq_dict[i] +1

    frequent_items(sigma, comb_freq_dict)


# first optimization: get rid of transactions that have less than 3 items.
def less_than_three(lst): #works
    new_lst = []
    for i in lst:
        if len(i)>=3:
            new_lst.append(i)
    return new_lst

# this function does the final bit of work and writes results to a file
def frequent_items(sig, my_dict):
    with open('supermarket_optimization.txt', 'w') as f:
        f.write('Item Set Size, co-occurrence frequency, item numbers \n')
        for item, freq in my_dict.items():
            if freq >= sig:
                f.write('3, '+str(freq)+', '+str(item)+'\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    parser.add_argument('integers', type=int)
    args = parser.parse_args()
    file = args.file
    sig = args.integers
    sigma = sig

    supermarket_optimization(sigma, file)
