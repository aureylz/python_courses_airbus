def my_reduce_list(list_, function, initializer):
    if len(list_)==0:
        return initializer
    if len(list_)==1:
        if initializer is None:
            return None
        else:
            return function(initializer, list_[0])
    if initializer is None:
        return my_reduce_list(list_[2:], function, function(list_[0], list_[1]))
    else:
        return my_reduce_list(list_[1:], function, function(initializer, list_[0]))
