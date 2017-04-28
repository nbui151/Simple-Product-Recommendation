# Simple-Product-Recommendation

Explanation: 
This code takes as input a csv file. Each column corresponds to a product and each row corresponds to a customer. 
For example, if the entries of the first row are [1, 1, 0, 0], this means a customer bought the first 
two products in the basket, but not the third and fourth product. The entries are binary, 1 meaning that at least one item 
from a product was bought, 0 meaning none was bought. This product recommendation code calculates the Probability that 
the customer will purchase item X if he/she has purchased item Y, based on past customers' recorded behavior.
The support of a product is defined as Pr(customer buys X) 
The support of two products is defined as Pr(customer buys both X and Y) 
The confidence is defined as Probability(customer buys X | he/she bought Y) 
The confidence is the measure we are interested in and is calculated as Confidence = Pr(customer buys both X and Y)/Pr(customer buys Y) 
To use the code, load your file.
support_item stores Pr(customer buys X) for each product X, Y, Z, etc... 
support_dict stores Pr(customer buys X and Y) for pairs of products X and Y, Y and Z, X and Z, etc. 
confidence_dict stores Pr(customer buys X | he/she bought Y) for pairs of products. 
sorted_support: sorts support_dict by the highest probabilities
sorted_confidence: sorts confidence_dict by the highest probabilities 

Usage: 
Say the file of past purchase data you loaded has 4 products: apple, orange, bread and butter (like in my example file), 
the function dictsearch("your product name", support_dict) would print out all the product pair support 
for the product, sorted by highest probability first, you will see which other products are frequently purchased together 
with that product. 
On the other hand, the function dictsearch("| your product name", confidence_dict) prints out the probability that 
a customer will buy a certain product, given that he/she bought your product, sorted by the highest probabilities. 
If you want to recommend another product to your customer, pick those displayed first by the function. 

Eg. dictsearch("apple", support_dict) prints out Pr(Buy apple and orange), Pr(Buy apple and bread), etc..., sorted high to low 
dictsearch("| apple", confidence_dict) prints out Pr(Buy orange | apple), Pr(Buy bread | apple), etc..., sorted high to low 
dictsearch("apple |", confidence_dict) would print out Pr(Buy apple | orange), Pr(Buy apple | bread), etc..., you might use this 
to decide when to recommend apple. 


