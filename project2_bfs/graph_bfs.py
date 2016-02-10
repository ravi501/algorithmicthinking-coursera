__author__ = 'ravi'

from collections import deque

def bfs_visited(ugraph, start_node):
    queue = deque()
    visited=set()

    visited.add(start_node)
    queue.add(start_node)

    while queue:
        node = queue.popleft()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

def cc_visited(ugraph):
    remaining_nodes = set(ugraph.keys())
    connected_components = []

    while remaining_nodes:
        node = remaining_nodes.pop()
        visited = bfs_visited(ugraph, node)
        remaining_nodes -= visited
        connected_components.append(visited)

    return connected_components

def largest_cc_size(ugraph):
    connected_components = cc_visited(ugraph)
    if connected_components:
        return max(map(len, connected_components))
    else:
        return 0

def compute_resilience(ugraph, attack_order):
    resilience = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph.pop(node)
        for edge in ugraph:
            if node in ugraph[edge]:
                ugraph[edge].remove(node)
        resilience.append(largest_cc_size(ugraph))

    return resilience




