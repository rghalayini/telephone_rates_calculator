## Telephone rates calculator

#### Assumptions
The solutions for this exercise can differ according to the way the user wants to insert operator entries. I have assumed that the user will enter the values manually, and hence my tailored solution according to this assumption.

#### How to use
The solution is wrapped in a function, therefore please call a function called **find_cheapest_operator** with three variables in order to get the result:
* variable 1: a list containing the names of the operators. For example, insert ['operatorA', operatorB']
* variable 2: an array of operators' rates in the same order as the list above. Each rate should be a dictionary having as key the prefix and as value the rate. For example, insert ({1:0.9, 268:5.1, 46:0.17, 4620:0.0, 468:0.15, 4631:0.15, 4673:0.9, 46732:1.1}, {1:0.92, 44:0.5, 46:0.2, 467:1.0, 48:1.2}
* variable 3: the telephone number

*an example entry is shown after the function call*

#### improvements
If the telephone operator list and the telephone number list are very long (thousands of entries), it might be inefficient to conduct loops to compare each entry with the other. Therefore, the code should be improved to make it faster to telephone numbers that match operator entries in case of a large number of values.
