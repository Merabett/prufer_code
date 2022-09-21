def prufer_to_tree(prufer_code):
    '''
    :param prufer_code: array containing elements of the prufer code
    :return: tree generated from prufer code
    '''
    tree_labels = [i for i in range(1, len(prufer_code) + 3)]
    deg = [1]*(len(tree_labels) + 1)

    for i in prufer_code:
        deg[i] += 1
    edges = []
    for i in prufer_code:
        for j in tree_labels:
            if deg[j] == 1:
                edges.append((i,j))
                deg[i] -= 1
                deg[j] -= 1
                break

    last = [x for x in tree_labels if deg[x] == 1]
    edges.append((last[0], last[1]))

    return edges



def tree_to_prufer(edges):
    '''
    :param edges: array containing all edges of the tree, represented as tuples
    :return: prufer code associated to the introduced tree
    '''
    prufer_list = []
    tree_labels = [i for i in range(len(edges) + 2)]
    deg = [0]*(len(tree_labels))

    for ele in edges:
        deg[ele[0]] += 1
        deg[ele[1]] += 1

    m = 0
    while m != len(deg)-3:
        vertex = 0
        smallest_leaf = None
        del_edge = None
        for deg_of_vertex in deg:
            if deg_of_vertex == 1:
                smallest_leaf = vertex
                break
            vertex += 1
        i = 0
        for e in edges:
           if e[0]==smallest_leaf or e[1]==smallest_leaf:
                if e[0] == smallest_leaf:
                    prufer_list.append(e[1])
                if e[1] == smallest_leaf:
                    prufer_list.append(e[0])
                deg[e[0]] -= 1
                deg[e[1]] -= 1
                del_edge = i
                break

           i += 1

        edges.pop(del_edge)
        m += 1

    prufer_sequence = ''
    for i in prufer_list:   prufer_sequence += str(i)
    return prufer_sequence
