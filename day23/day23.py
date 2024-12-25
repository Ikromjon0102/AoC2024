from collections import defaultdict

# Input data
# connections = [
#     "kh-tc", "qp-kh", "de-cg", "ka-co", "yn-aq", "qp-ub", "cg-tb",
#     "vc-aq", "tb-ka", "wh-tc", "yn-cg", "kh-ub", "ta-co", "de-co",
#     "tc-td", "tb-wq", "wh-td", "ta-ka", "td-qp", "aq-cg", "wq-ub",
#     "ub-vc", "de-ta", "wq-aq", "wq-vc", "wh-yn", "ka-de", "kh-ta",
#     "co-tc", "wh-qp", "tb-vc", "td-yn"
# ]

connections = [ i.strip('\n') for i in open('input.txt', 'r').readlines() ]

#
# # Parse input into an adjacency list
# network = defaultdict(set)
# for connection in connections:
#     a, b = connection.split('-')
#     network[a].add(b)
#     network[b].add(a)
#
# # Find triangles
# triangles = set()
# for a in network:
#     for b in network[a]:
#         for c in network[b]:
#             if c in network[a] and a < b < c:  # Ensure unique ordering
#                 triangles.add((a, b, c))
#
# # Filter triangles where at least one name starts with 't'
# t_triangles = [triangle for triangle in triangles if any(computer.startswith('t') for computer in triangle)]
#
# # Output the result
# print("Total triangles:", len(triangles))
# print("Triangles with 't':", len(t_triangles))


network = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    network[a].add(b)
    network[b].add(a)

# Recursive function to find cliques
def find_cliques(potential_clique, remaining_nodes, skip_nodes, max_cliques):
    if not remaining_nodes and not skip_nodes:
        # Found a clique
        max_cliques.append(potential_clique)
        return
    while remaining_nodes:
        node = remaining_nodes.pop()
        find_cliques(
            potential_clique + [node],
            remaining_nodes & network[node],
            skip_nodes & network[node],
            max_cliques
        )
        skip_nodes.add(node)

# Find all maximal cliques
max_cliques = []
find_cliques([], set(network.keys()), set(), max_cliques)

# Find the largest clique
largest_clique = max(max_cliques, key=len)

# Generate the password
password = ",".join(sorted(largest_clique))

# Output the result
print("Largest clique:", largest_clique)
print("Password:", password)