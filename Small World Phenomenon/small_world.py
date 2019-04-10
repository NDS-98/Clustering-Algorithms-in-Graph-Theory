import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def add_edges(G):
    list_nodes = []
    for i in G.nodes():
        list_nodes.append(i)
    n = G.number_of_nodes()
    # print(list_nodes)

    for i in range(0, len(list_nodes)):
        G.add_edge(list_nodes[i], list_nodes[i-1])
        G.add_edge(list_nodes[i], list_nodes[i-2])
        target = i+1
        if(target>n-1):
            target = target-n
            G.add_edge(list_nodes[i], target)
        else:
            G.add_edge(list_nodes[i], target)

        target = i+2
        if (target>n-1):
            target = target-n
            G.add_edge(list_nodes[i], target)
        else:
            G.add_edge(list_nodes[i], target)


def add_long_link(G):
    v1 = random.choice(np.array(G.nodes()))
    v2 = random.choice(np.array(G.nodes()))
    while(v1==v2):
        v1 = random.choice(np.array(G.nodes()))
        v2 = random.choice(np.array(G.nodes()))
    G.add_edge(v1,v2)

def find_best_neighbour(G,c,v):
    dis = G.number_of_nodes()
    for each in G.neighbors(c):
        dis1 = len(nx.shortest_path(H,source=each,target=v))
        if(dis1<dis):
            dis=dis1
            choice=each
    return choice


def myopic_search(G,u,v):
    path = [u]
    current = u
    while(1):
        w = find_best_neighbour(G, current, v)
        path.append(w)
        current = w
        if(current==v):
            break
    return path


def set_path_colors(G,p,p1):
    c=[]
    for each in G.nodes():
        if(each==p1[0]):
            c.append("red")
            print(each)
        elif(each==p1[len(p1)-1]):
            c.append("red")
            print(each)
        elif(each in p and each in p1 and each!=p1[0] and each!=p1[len(p1)-1]):
            c.append("yellow")
        elif(each in p and each not in p1):

            c.append("blue")
        elif(each in p1 and each not in p):
            c.append("green")
        elif(each not in p1 and each not in p):
            c.append("black")

    return c

x1=[]
y1=[]

# for num in [100,200,300,400,500,600,700,800,900,1000]:
# for num in [100,200,300,400,500]:
for num in [100]:
    G = nx.Graph()
    G.add_nodes_from(range(0,num))

    # Add ties based on Homophily
    add_edges(G)
    # for each in G.nodes():
    #     print(each, ':', end=' ')
    #     for each1 in G.neighbors(each):
    #         print(each1, end=' ')
    #     print('\n')

    # Add weak ties
    # add_long_link(G)

    H = G.copy()

    x = [0]
    y = [nx.diameter(G)]
    t=0

    # 10% of number of nodes
    while(t<=G.number_of_nodes()/10):
        add_long_link(G)
        t=t+1
        x.append(t)
        y.append(nx.diameter(G))
    plt.title("For "+str(num)+" Nodes")
    plt.xlabel("Number of weak ties added")
    plt.ylabel("Diameter")
    plt.plot(x,y)
    plt.show()

    m=[]
    o=[]
    x=[]
    t=0

    # diametrically opposite points
    for u in range(0,(int)(G.number_of_nodes()/2)-1):
        v=u+G.number_of_nodes()/2
        p = myopic_search(G,u,v)
        p1 = nx.shortest_path(G,source=u,target=v)
        m.append(len(p))
        o.append(len(p1))
        x.append(t)
        t=t+1
    print(G.number_of_nodes(), np.average(m))
    y1.append(np.average(m))
    x1.append(G.number_of_nodes())
    plt.plot(x, m, 'r')
    plt.plot(x, o, 'b')
    plt.xlabel('Node')
    plt.ylabel('Path Length')
    plt.gca().legend(('myopic', 'optimal'))
    plt.show()

    colors = set_path_colors(G, p, p1)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,pos=pos,node_color=colors)
    plt.show()

plt.plot(x1,y1)
plt.xlabel('Number of nodes')
plt.ylabel('Average myopic path length')
plt.show()




print(p1)
print(p)


print(colors[0],colors[40])





