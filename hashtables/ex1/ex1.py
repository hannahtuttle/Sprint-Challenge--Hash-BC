#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for idx in range(length):
        hash_table_insert(ht, weights[idx], idx)
        # print('weight:', weights[idx], 'index',idx)
    # print('testing index check',ht.storage[4].key)
    ind = 0
    find = None
    while ind is not length:
        num = limit - weights[ind]
        find = hash_table_retrieve(ht,num)
        # print(weights[ind])
        # print(num)
        if find is not None:
            # print('find', find)
            print(ind, find)
            return (find,ind)
        ind += 1
    if find is None:
        return None
   
    

# inputs = [ 4, 6, 10, 15, 16 ]
# length = 5 
# limit = 21
# get_indices_of_item_weights(inputs, length, limit)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
