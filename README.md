#Supermarket-Optimization 

Description: This program generates all of the item sets (set size 3 or more) that occur in transactions at least sigma-amount of times. The sigma value is a parameter passed into the program. This algorithm utilizes FP Growth to accompolish the problem statement. I was debating between two algorithms: Apriori and FP Growth. I ended up choosing the latter for a couple reasons. The apriori algorithm takes a support value and confidence value as parameters. In our problem, we are only given a support value which is sigma. Secondly, the apriori algorithm does not work well with large datasets like the one provided. The FP Growth algorithm efficiently is able to determine frequencies for each pattern using a tree. It also filters many of the undesireable results prior to constructing the tree. This is why I decided to go with the FP Growth algorithm. 

In order to run this program, do the following:
 • Clone or download the repository
 • Be sure to 'pip3 install pyfpgrowth' 
 • The globality_supermarket.py file is the file you want to execute from terminal • Go to terminal, and run "python3 globality_supermarket.py -f <dat file path> <sigma value> " - For example, "python globality_supermarket.py -f /Users/bob/Downloads/retail_25k.dat 4" - The sigma value is 4 and the file path is /Users/bob/Downloads/retail_25k.dat. 
 • Upon executing, a textfile called "supermarket_optimization.txt" will appear in the same directory you executed the script in. 
 • The textfile will have a header and below it will be all of the desired data 
