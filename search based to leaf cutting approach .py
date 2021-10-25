# OBJECTIVE
# Find the central node of a tree that has the shortest maximum distance to all the leafs of the tree and return that shortest distance

# INPUT
# N - Number of links
# Next N lines are 2 space separated ints specifying a link between 2 nodes.

# OUTPUT
# Single int representing the minimal amount of steps required to proagate to every node on the graph

# NOTES
# No cyclic links e.g. a => b => c => a
# A propagation step is counted as traversing to a new depth in the tree and not a step for each link (i.e. propagation is concurrent)
# Graphs can be big (up to 150,000 nodes)
# Looking at the test data the nodes are not always numbered from zero or contiguously
# The value of x and y < 200,000 (so we can use an array rather than a dict)

# TO CONSIDER
# We should always take the max distance from our epicentre to the tips as the answer as this will represent the minimum time required
# Do we calculate the max distance for each node and track the shortest or is there an algorithm that will allow us to pinpoint the epicentre node immediately?
# The blurb for the problem specifies memoization which prob means that a straightforward search approach will be too slow and we need to cache the max dists. No mention as to what the time limit is - forum posts suggests that timeout is ~5000ms
# We don't have to search the whole tree everytime we just have to search until we exceed the current max
# We could always thread the search and calculate node distances in parallel
# Is there a heuristic that will give us the best node to start with that will give us more early outs during traversal? The one surrounded by the most nodes?

# UPDATE
# After implementing a search solution with min-max it was too slow, even with the early out added. Looking on the forum it seems most people were using the leaf cutting approach. Trying this proved to be much quicker. However it does
# feel that it goes against the spirit of the challenge which specifically mentioned searching and memoization

import sys
from collections import defaultdict

# Logging to stdout is reserved for returning the answer. To debug log
# we must log to stderr
#
def debug_log(msg):
	sys.stderr.write(str(msg) + '\n')

# Iterate through the nodes and find any that have an adjacency list with only a single link. 
# This means that the node is a leaf node. We then prune that node and update the links of
# any linked nodes
# 
# Note: We defer pruning so that we don't create more leaf nodes as we iterate
# 
def trim_all_leaves(links):
	to_remove = []
	for node,linked_nodes in links.items():
		if len(linked_nodes) == 1:
			# This is a leaf node mark it for pruning
			to_remove.append(node)

	for node in to_remove:
		linked_nodes = links[node]
		for ln in linked_nodes:
				links[ln].remove(node)
		del links[node]

# Links are adjacency lists where each node key of the dictionary contains the other linked node indices
# We use a leaf pruning algorithm that essentially allows us to measure the radius of the graph by counting the
# number of steps to reach the central node
# 
def run(links, expected_output = None):
	num_steps = 0
	while len(links) > 1:
		trim_all_leaves(links)
		num_steps = num_steps + 1

	if expected_output != None:
		print("SUCCESS" if num_steps == expected_output else str.format("FAIL expected {} got {}", expected_output, num_steps))

	# Output the answer to CodinGame
	print(num_steps)

# Used by the tests to convert lines of linked nodes into adjacency lists
# 
def parse_links(unparsed_links):
	links = defaultdict(list)
	for nodes in unparsed_links:
		n1, n2 = [int(node) for node in nodes.split()]
		links[n1].append(n2)
		links[n2].append(n1)

	return links

# Used when running in CodinGame to read input from stdinput
#
if __name__ == "__main__":
	num_links = int(raw_input())

	links = defaultdict(list)
	for i in xrange(num_links):
		n1, n2 = [int(j) for j in raw_input().split()]
		links[n1].append(n2)
		links[n2].append(n1)

	run(links)