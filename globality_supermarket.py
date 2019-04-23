import csv
import sys
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
    #use helper function to convert dat file to an easy-to-traverse list without whitespaces
    retail_list = file_to_list(file)

    #put sets of three into dictionary and set the value to the frequency of those sets appearing in retail_list together
    my_dict = dict()
    row_length = len(retail_list)
    for i in range(row_length):
        for j in range(len(retail_list[i])-2):
            first = retail_list[i][j]
            second = retail_list[i][j+1]
            third = retail_list[i][j+2]
            if first+','+second+','+third not in my_dict:
                my_dict[first+','+second+','+third]=0
            else:
                my_dict[first+','+second+','+third] = my_dict[first+','+second+','+third] +1

    #use helper function to return file with values that meets the sigma value criteria for frequency
    frequent_items(sigma, my_dict)


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
