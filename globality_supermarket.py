import csv
import pyfpgrowth
import argparse 

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
    transactions = file_to_list('/Users/jashvora/Downloads/retail_25k.dat')

    #get an optimized list of transactions with use of helper function
    opt_transactions = less_than_three(transactions)
    patterns = pyfpgrowth.find_frequent_patterns(opt_transactions, sigma)
    three_or_more_set = dict()
    for key, val in patterns.items():
        if len(key) >=3:
            three_or_more_set[key] = val

    write_to_file(sigma, three_or_more_set)


# first optimization: get rid of transactions that have less than 3 items.
def less_than_three(lst): #works
    new_lst = []
    for i in lst:
        if len(i)>=3:
            new_lst.append(i)
    return new_lst

# this function does the final bit of work and writes results to a file
def write_to_file(sig, my_dict):
    with open('supermarket_optimization.txt', 'w') as f:
        f.write('Item Set Size, co-occurrence frequency, item numbers \n')
        for item, freq in my_dict.items():
            f.write(str(len(item))+', '+str(freq)+', '+str(item)+'\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    parser.add_argument('integers', type=int)
    args = parser.parse_args()
    file = args.file
    sig = args.integers
    sigma = sig

    supermarket_optimization(sigma, file)
