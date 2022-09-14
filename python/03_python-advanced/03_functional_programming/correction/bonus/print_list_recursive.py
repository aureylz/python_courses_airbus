def print_list_recursive(my_list):
    if len(my_list) == 0:
        return                     
    else:
        print(my_list[0])       
        return print_list_recursive(my_list[1:])  