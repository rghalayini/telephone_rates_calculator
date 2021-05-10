def find_cheapest_operator(operators_list, rates, telephone):
    #transforming the telephone number to a string in order to make it simpler to loop through
    tel_num=str(telephone)
    
    #let's initiate a new empty dictionary to put the highest matching prefixes of each operator in
    highest_prefix_per_operator={}
    
    index=0


    #First: looping through the list of operators to analyse each operator alone
    for single_operator in rates:
        prefix_list=[]
        
        #copy the prefixes alone to another list
        for prefix in single_operator:
            prefix_list.append(str(prefix))

        matching_numbers=[]
        
        #checking if there are matching prefixes with the telephone number and copying them to another list
        for i in prefix_list:
            if tel_num.startswith(i):
                matching_numbers.append(i)

        #choosing the longest matching prefix if there is matching prefix
        if len(matching_numbers)>0:
            longest_match=int(max(matching_numbers, key=len))
    
            #copying both the longest matching prefix per operator and its rate to dictionary we created above
            for key in single_operator:
                if key==longest_match:
                    highest_prefix_per_operator[operators_list[index]] = {"prefix":key, "rate":single_operator[key]}
                
        index = index+1
        
    #once we repeat the for loop for each operator, we will end up with a nested dictionary having one longest 
    #matching prefix per operator and its rate. Therefore, we will simply choose the cheapest rate and return the 
    #respective operator
    if len(highest_prefix_per_operator)>0:
        key = min(highest_prefix_per_operator, key=lambda x: highest_prefix_per_operator[x]["rate"])
        return "The cheapest operator is: " + key 
    
    #if there is no match between all the prefixes and the phone number, we return the following
    else:
        return "no operator has a rate for this phone number"


op_A={1:0.9, 268:5.1, 46:0.17, 4620:0.0, 468:0.15, 4631:0.15, 4673:0.9, 46732:1.1}
op_B={1:0.92, 44:0.5, 46:0.2, 467:1.0, 48:1.2}
tel=1209824324

solution=find_cheapest_operator(["operatorA", "operatorB"], (op_A, op_B), tel)
print(solution)

