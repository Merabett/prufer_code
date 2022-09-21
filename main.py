import Tree as T
import functions as f

if __name__ == "__main__":
    print('LOADING...')
    print("          PRÜFER CODE PROGRAM")
    print("          ===================")
    print("Options:")
    print("     1. Generate the Prüfer code for a given labeled tree")
    print("     2. Generate the tree associated to a given Prüfer code")
    print("     3. Exit the program")

    option = 0

    while option != "3":

        option = input("Please chose one option between 1 and 3: ")

        if option == "1":
            print("GENERATING THE PRÜFER CODE FOR A GIVEN TREE")
            print("*"*41)
            print("Reading the tree")
            print("================")
            num_edges = int(input("Please, enter the number of edges in the tree: "))
            edges = []

            for i in range(1, num_edges + 1):
                print("Reading the edge ", str(i))
                father_vertex = int(input("Please, enter the father vertex: "))
                child_vertex = int(input("Please, enter the child vertex: "))
                edges.append((father_vertex, child_vertex))
            prufer_code = f.tree_to_prufer(edges)
            print("The generated tree in preorder is: ", str(edges))
            print("The Prüfer code associated to the tree is: ", str(prufer_code))
            print()

        elif option == "2":
            print("GENERATING THE TREE FROM A PRÜFER CODE")
            print("*"*36)

            prufer_code = input("Please enter a sequence of integer numbers without spaces: ")
            input_prufer = []
            for i in prufer_code:
                input_prufer.append(int(i))  #converts string of prufer sequence to list of elements

            resulting_tree = f.prufer_to_tree(input_prufer) #returns edges of the thee
            #create tree from resulting edges:

            vertex = []
            for e in resulting_tree:
                if e[0] not in vertex:  vertex.append(e[0])
                if e[1] not in vertex:  vertex.append(e[1])

            nodes = [None] * (1 + len(vertex))

            for e in resulting_tree:
                parent = e[0]
                child = e[1]

                if nodes[parent] is None:   nodes[parent] = T.Tree(parent)
                if nodes[child] is None:    nodes[child] = T.Tree(child)
                nodes[parent].append_child(nodes[child])

            v = 1
            while not nodes[v].is_root():   v += 1
            final_result = nodes[v]

            print(final_result)
            print("The entered Prüfer code is: ", str(input_prufer))
            print("The generated tree in preorder is: ", str(final_result))
            print()

        elif option == "3":
            print('EXITING...')
            break
        else:
            print("Error. Please try again.")
