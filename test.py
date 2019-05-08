import random

MAXWEIGHT = 10
NLEAVES = 4

def main():
    vertices, parents, children = gen_rand_tree()
    get_distances(children[2*NLEAVES-2], children)

def get_distances(children):
    

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
    main()
