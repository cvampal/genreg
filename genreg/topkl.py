import sys
import networkx as nx
import numpy as np
import pandas as pd
from scipy import linalg as LA



def get_eigen_val(mat):
    eigen,_ = LA.eig(mat)
    return eigen.real


def get_regular_graph2(n,k):
    graphs = []
    graph_append = graphs.append
    for i in range(1,n):
        j = 0
        if (i*n) % 2 == 0:
            while j != k:
                g = nx.generators.random_graphs.random_regular_graph(i,n)
                if nx.is_connected(g):
                    graph_append(g)
                j+=1
    return graphs



def generate_reg_graph2(n,k,output_filename):
    g = get_regular_graph2(n,k)
    print(f'{len(g)} random regular graph found.')
    clm = [i for i in range(1,n+1)]
    clm.append('graph')
    df = pd.DataFrame(columns=clm)
    for i in range(len(g)):
        matrix = nx.adjacency_matrix(g[i]).toarray()    
        eig = np.round(get_eigen_val(matrix),3)
        eig[::-1].sort()
        eig = eig.tolist()
        df.loc[i] = eig + [g[i]]
    new = df.drop_duplicates(subset=list(df)[:-2])
    print(f'{new.shape[0]} unique graph generated.')
    new.reset_index(inplace=True)
    new.to_pickle(output_filename)


