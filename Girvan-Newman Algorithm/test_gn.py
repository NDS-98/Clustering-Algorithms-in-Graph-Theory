import networkx as nx
import matplotlib.pyplot as plt


def edge_to_remove(G):
    dict1 = nx.edge_betweenness_centrality(G)
    print(dict1)
    print()
    list_of_tuples = dict1.items()
    list_of_tuples = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
    print(list(list_of_tuples))
    print()
    print(list(list_of_tuples)[0])
    print(list(list_of_tuples)[0][0])
    print()
    return list(list_of_tuples)[0][0]


def girvan(G):
    c = nx.connected_component_subgraphs(G)
    l = len(list(c))
    print('The number of connected components are ', l)

    while(l==1):
        G.remove_edge(*edge_to_remove(G))
        c = nx.connected_component_subgraphs(G)
        l = len(list(c))
        print('The number of connected components are ', l)

    return c


# G = nx.barbell_graph(5,2)
# G = nx.karate_club_graph()
G = nx.barbell_graph(10,5)

nx.draw_networkx(G)
plt.show()
c = girvan(G)


for i in c:
    print(i)
    print(i.nodes())
    print('...................')

nx.draw_networkx(G)
plt.show()

