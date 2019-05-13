import random
import sys
from collections import Counter
from itertools import chain
from main import read_distances, neighbor_joining 

MAXWEIGHT = 10
NLEAVES = 4

def generate(filename):
	distance_matrix = get_empty_matrix(NLEAVES)
	vertices, parents, children = gen_rand_tree()
	print(children)
	get_distances(2*NLEAVES-2, children, distance_matrix)

	for i in range(NLEAVES):
		distance_matrix[i][i] = 0

	with open(filename, 'w') as f:
		for i in range(NLEAVES):
			for j in range(NLEAVES):
				f.write("%d " % distance_matrix[i][j])
			f.write("\n")
	print(distance_matrix)

def check(filename):
	NLEAVES, correct_matrix = read_distances(filename)
	nj_matrix = get_empty_matrix(NLEAVES)
	for i in range(NLEAVES):
		for j in range(NLEAVES):
			nj_matrix[i][j] = correct_matrix[i][j]
	children = neighbor_joining(NLEAVES, nj_matrix)
	distance_matrix = get_empty_matrix(NLEAVES)
	get_distances(2 * NLEAVES - 2, children, distance_matrix)

	correct = Counter(chain.from_iterable(correct_matrix))
	solution = Counter(chain.from_iterable(distance_matrix))
	diff = (solution - correct) + (correct - solution)
	if len(diff) > 0:
		print(correct_matrix)
		print(distance_matrix)
		return 1

	for i in range(NLEAVES):
		for j in range(NLEAVES):
			if correct_matrix[i][j] != distance_matrix[i][j]:
				print("differ at (%d, %d): expected %d, got %d" % (i, j, correct_matrix[i][j], distance_matrix[i][j]))
				return 2
	
	print("correct")
	return 0


def get_empty_matrix(n):
	distance_matrix = []

	for i in range(n):
		row= []
	
		for j in range(n):
			row += [0]
		
		distance_matrix += [ row ]
    
	return distance_matrix


def get_distances(root,children, distance_matrix):
	if root < NLEAVES:
		return [root]
	else:
		left = get_distances(children[root][0][0], children, distance_matrix)
		right = get_distances(children[root][1][0], children, distance_matrix)
		weight_left = children[root][0][1]
		weight_right= children[root][1][1]
		
		for child in left:
			distance_matrix[child][child] += weight_left

		for child in right:
			distance_matrix[child][child] += weight_right

		for left_child in left:
			for right_child in right:
				distance_matrix[left_child][right_child] = distance_matrix[left_child][left_child] + distance_matrix[right_child][right_child]
				distance_matrix[right_child][left_child] = distance_matrix[left_child][right_child]

		if root == 2 * NLEAVES - 2:
			for i in range(NLEAVES):
				distance_matrix[i][i] = 0
		return left + right

def gen_rand_tree():
    vertices = list(range(NLEAVES))
    active_vertices = list(range(NLEAVES))
    parents = {}
    children = {}

    for i in range(NLEAVES - 1):
        new_vertex = NLEAVES + i
        a, b = random.sample(active_vertices, 2)

        a_weight = random.randint(0, MAXWEIGHT)
        parents[a] = (new_vertex, a_weight)

        b_weight = random.randint(0, MAXWEIGHT)
        parents[b] = (new_vertex, b_weight)

        children[new_vertex] = ((a, a_weight), (b, b_weight))

        active_vertices.remove(a)
        active_vertices.remove(b)
        active_vertices += [new_vertex]

    return vertices, parents, children

if __name__ == '__main__':
	command = sys.argv[1] if len(sys.argv) > 1 else 'help' 
	filename = sys.argv[2] if len(sys.argv) > 2 else 'tmp.txt'
	NLEAVES = int(sys.argv[3]) if len(sys.argv) > 3 else NLEAVES
	MAXWEIGHT = int(sys.argv[4]) if len(sys.argv) > 4 else MAXWEIGHT

	if command == 'gen':
		generate(filename)
	elif command == 'check':
		ret = check(filename)
		sys.exit(ret)
	else:
		print("Usage: python test.py <command> <filename> <#leaves> <max_weight>")
		print("<command>: run, check")
