def my_reduce_list(list_: List, function, initializer):
    if len(list_) == 1:   
        return  list_[0]                  
    else: 
        result = function(list_[0], my_reduce_list(list_[1:],function,initializer))
        return result
