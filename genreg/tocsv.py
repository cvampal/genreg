import itertools
import pandas as pd
import networkx as nx
import csv
import sys
import multiprocessing


def findsubsets(S,m):
    return itertools.combinations(S, m)

def boundary_length(G,aSet):
    all_crossing_edges=set([])
    for a in aSet:
        current_targets=nx.all_neighbors(G,a)
        for current_target in current_targets:
            if current_target not in aSet:
                all_crossing_edges.add((a,current_target))
    return len(all_crossing_edges)

def get_Cheeger_pq(G):
    vertices=nx.nodes(G)
    num_vertices=len(vertices)
    currentMin=num_vertices**2
    p,q = 0,0
    for subset_size in range((int)(num_vertices/2)):
        possibleASets=findsubsets(vertices,subset_size+1)
        for aSet in possibleASets:
            p_var = boundary_length(G,aSet)
            q_var = subset_size+1
            currentValue=p_var/float(q_var)
            if (currentValue<currentMin):
                currentMin=currentValue
                p = p_var
                q = q_var
    return (currentMin,p,q)

# ************************ Parallel Computing of Cheeger Constant****************************************

def boundary_length2(T):
    G,aSet = T
    all_crossing_edges=set([])
    for a in aSet:
        current_targets=nx.all_neighbors(G,a)
        for current_target in current_targets:
            if current_target not in aSet:
                all_crossing_edges.add((a,current_target))
    return len(all_crossing_edges)


def get_Cheeger_pq_parallel(G):
    vertices=nx.nodes(G)
    num_vertices=len(vertices)
    currentMin=num_vertices**2
    p,q = 0,0
    for subset_size in range((int)(num_vertices/2)):
            q_var = subset_size+1
            possibleASets=findsubsets(vertices,subset_size+1)
            data = [(G,aSet) for aSet in possibleASets]
            pools = multiprocessing.Pool(7)
            results = pools.map(boundary_length2,data)
            pools.close()
            pools.join()
            for p_var in results:
                      currentValue=p_var/float(q_var)
                      if (currentValue<currentMin):
                         currentMin=currentValue
                         p = p_var
                         q = q_var
    return (currentMin,p,q)

# *****************************************************************
def write_data(filename,data):
    with open(filename,'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def pkl_to_csv(filename,n,out_file,parallel_mode=True):
    df = pd.read_pickle(filename)
    del df['index']
    header = [i for i in range(1,n+1)]+['Cheeger']
    write_data(out_file,header)
    for i in range(len(df)):
        data = df.iloc[i].tolist()
        if parallel_mode:
             ch = get_Cheeger_pq_parallel(data[-1])
        else:
             ch = get_Cheeger_pq(data[-1])
        data[-1] = ch
        write_data(out_file,data)



