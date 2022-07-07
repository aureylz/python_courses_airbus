def print_list_recursive(list_of_something: List[Any]):
    if len(list_of_something) == 0:
        return                     
    else:
        print(list_of_something[0])       
        return print_list_recursive(list_of_something[1:])  
