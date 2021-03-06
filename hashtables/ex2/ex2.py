#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for idx in range(length):
        # print('source',tickets[idx].source)
        # print('destination',tickets[idx].destination)
        hash_table_insert(hashtable, tickets[idx].source, tickets[idx].destination)
    
    current = hash_table_retrieve(hashtable, "NONE")
    # prev = None
    count = 0
    while count is not length:
        route[count] = current
        current = hash_table_retrieve(hashtable, current)
        count += 1

    print('route',route)
    return route


# ticks = [
#   Ticket("PIT", "ORD" ),
#   Ticket("XNA", "CID" ),
#   Ticket("SFO", "BHM" ),
#   Ticket("FLG", "XNA" ),
#   Ticket("NONE", "LAX"),
#   Ticket("LAX", "SFO" ),
#   Ticket("CID", "SLC" ),
#   Ticket("ORD", "NONE"),
#   Ticket("SLC", "PIT" ),
#   Ticket("BHM", "FLG" )
# ]
# legs = len(ticks)

# reconstruct_trip(ticks, legs)