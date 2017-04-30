# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:18:36 2017

@author: nbui151 

"""

# loading data 
import numpy as np
import pandas as pd
import operator # for sorting commmand  

X =pd.read_csv('products.csv', sep=',', header=0)

# print the names of the products 
print(X.columns) 

'''Let's calculate the Probability that a customer will buy a product (eg. apples)
and store the result in a dictionary called support_item, whereby support["apple"] = Pr(customer buys apple) 
and Pr(customer buys apple) = (Total number of customers who bought apples)/(Total number of customers)
'''

# count the number of times each product was bought 
count_item = np.zeros(X.shape[1])
for i in range(X.shape[1]): 
    count_item[i] = (X[X.columns[i]]==1).sum()

# calculate Pr(customer buys X) 
support_item = count_item/(X.shape[0]) 

# store the product name and probability in a dictionary 
support_item_dict = {}
for i in range(X.shape[1]):
    support_item_dict[X.columns[i]] = support_item[i]

# calculate the support for two products Pr(customer buys X and Y) 
name_pairwise = pd.DataFrame(np.zeros([X.shape[1],X.shape[1]]))
support_pairwise = pd.DataFrame(np.zeros([X.shape[1],X.shape[1]]))

for col in range(X.shape[1]):
    item1 = str(X.columns[col])
    for col2 in range(X.shape[1]):
        item2 = str(X.columns[col2])
        if item1 is not item2: 
            num_pair = 0
            for row in range(X.shape[0]):     
                if X.iloc[row, col] == 1 and X.iloc[row, col2] == 1:
                    num_pair += 1
            name_pairwise.iloc[col, col2] = str("Pr(Buy " + item1 + " and " + item2 + ")") 
            support_pairwise.iloc[col, col2] = round(num_pair/X.shape[0], 3)

# store product pair name and probabilities in a dictionary 
# format of dictionary is: support_dict["Pr(Buy apple and orange)"] = number 

support_dict = {}
for m in range(name_pairwise.shape[1]):
    for n in range(name_pairwise.shape[1]):
        if support_pairwise.iloc[m,n] > 0: 
            support_dict[name_pairwise.iloc[m,n]] = support_pairwise.iloc[m,n]
sorted_support = sorted(support_dict.items(), key=operator.itemgetter(1), reverse=True)


## Calculate the confidence which is Pr(customer will buy X | he/she bought Y)  
confidence_pairwise = pd.DataFrame(np.zeros([X.shape[1],X.shape[1]]))
name_pairwise_conf = pd.DataFrame(np.zeros([X.shape[1],X.shape[1]]))

for col in range(X.shape[1]):
    item1 = str(X.columns[col])
    for col2 in range(X.shape[1]):
        item2 = str(X.columns[col2])
        if item1 is not item2: 
            name_pairwise_conf.iloc[col, col2] = str("Pr(Buy " + item1 + " | " + item2 + ")") 
            confidence_pairwise.iloc[col, col2] = support_pairwise.iloc[col, col2]/support_item[col2] 

# store the names and probabilities in dictionary 
# format of dictionary is: confidence_dict["Pr(Buy apple | orange)"] = number 

confidence_dict = {}
for m in range(name_pairwise_conf.shape[1]):
    for n in range(name_pairwise_conf.shape[1]):
        if confidence_pairwise.iloc[m,n] > 0: 
            confidence_dict[name_pairwise_conf.iloc[m,n]] = confidence_pairwise.iloc[m,n]
sorted_conf = sorted(confidence_dict.items(), key=operator.itemgetter(1), reverse=True)
       
# write a function to help us pull out the probabilities if certain keywords are contained in the key 

def dictsearch(search_string, dictionary):
    mini_dict = {}
    for key, v in dictionary.items():
        if str(search_string) in key:
            key = key 
            value = round(v, 4)
            mini_dict[key] = value
    mini_dict_sorted = sorted(mini_dict.items(), key=operator.itemgetter(1), reverse=True)
    return mini_dict_sorted        

