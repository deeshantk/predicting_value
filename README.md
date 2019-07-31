# predicting_value
Can predict the value of any given linear data using straight line concept. 

Library used here is matplotlib which is used to draw graphs and graphic analysis.

# How program works-
First the data is provided (value and its answer) which is stored in two seperte list (xs and ys).
Both value and answer list (xs and ys) along with the value for which the answer is to be predicted is given as arguments to the function predicting the answer.
Now, on line 4 describtion of graph is given. You can learn more about it on https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/.

On line 12 and 13, a loop will calculate slope from the list (xs and ys) and store it in a new list (slope).

Line 18 is a loop that will assign m to the slope of most of values of list (xs and ys).

Predicted answer of the value is calculated using y = mx + c (equation of straingt line) and is returned to predicted_value varible and is printed in main() function.



# NOTE- This will only give accurated answer is case of linear data (where slope is equal maximum times) or where the graph is a straight line.
