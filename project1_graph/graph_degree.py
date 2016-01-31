__author__ = 'ravi'

"""
Sample directed graphs
"""
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 3: set([0]),
             4: set([1]), 5:set([2]), 6:set([])}

EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 3: set([7]), 4: set([1]),
             5: set([2]), 6: set([]), 7: set([3]), 8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}

GRAPH0 = {0: set([1]),
          1: set([2]),
          2: set([3]),
          3: set([0])}

GRAPH1 = {0: set([]),
          1: set([0]),
          2: set([0]),
          3: set([0]),
          4: set([0])}

GRAPH4 = {"dog": set(["cat"]),
          "cat": set(["dog"]),
          "monkey": set(["banana"]),
          "banana": set([])}


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with
    the specified number of nodes. A complete graph contains all possible edges to the restriction that self-loops are
    not allowed.
    """

    dictionary = {}
    if num_nodes <= 0:
        return dictionary
    else:
        for dictionary_key in range(0, num_nodes):
            items = []
            for dictionary_value in range(0, num_nodes):
                if dictionary_key == dictionary_value:
                    continue
                else:
                    items.append(dictionary_value)
            dictionary[dictionary_key] = set(items)
    return dictionary

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computed the in-degrees for the nodes in the graph,
    The function should return a dictionary with the same set of keys (nodes) as digraph whose corresponding values are
    the number of edges whose head matches a particular node.
    """

    in_degrees = {}
    for dictionary_key in digraph.keys():
        count = 0
        for dictionary_value in digraph.values():
            if dictionary_key == dictionary_value:
                continue
            else:
                if dictionary_key in dictionary_value:
                    count += 1
        in_degrees[dictionary_key] = count
    return in_degrees

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the un-normalized distribution of the
    in-degree of the graph. The function returns a dictionary whose keys correspond to in-degrees of nodes in the graph.
    The value associated with each particular in-degree is the number of nodes with that in-degree. In-degrees with no
    corresponding nodes in the graph are not included in the dictionary.
    """

    degree_distribution = {}
    for dictionary_key in digraph.keys():
        count = 0
        for dictionary_value in digraph.values():
            if dictionary_key == dictionary_value:
                continue
            else:
                if dictionary_key in dictionary_value:
                    count += 1
        if count in degree_distribution:
            degree_distribution[count] += 1
        elif count not in degree_distribution:
            degree_distribution[count] = 1
    return degree_distribution


print(compute_in_degrees(EX_GRAPH0))
#print(in_degree_distribution(GRAPH1))
print(make_complete_graph(3))

print(in_degree_distribution(GRAPH0))