import sys
from genreg import tocsv,topkl

nodes = int(sys.argv[1])
sample_size = int(sys.argv[2])
filename = 'data/'+ sys.argv[3] + '.pkl'
outfilename = 'data/reg'+sys.argv[1]+'.csv'
topkl.generate_reg_graph2(nodes,sample_size,filename)
tocsv.pkl_to_csv(filename,nodes,outfilename)
