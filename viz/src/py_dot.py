from graphviz import Digraph


if __name__ == "__main__":
    dot = Digraph(comment="simple graph")
    dot.node('A', "Life")
    dot.node('B', "Family")
    dot.node('C', "Peace")
    dot.node('D', "Health")
    dot.node('E', "Friends")
    dot.edges(['AB', 'AC', 'AD', 'AE'])

    print(dot.source)
    dot.render('graph.pdf', view=True,)
