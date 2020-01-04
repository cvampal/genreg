# GenReg
GenReg is a package to generate [regular graphs](https://en.wikipedia.org/wiki/Regular_graph) and compute its isoperimertic constant ([Cheeger Constant](https://en.wikipedia.org/wiki/Cheeger_constant_(graph_theory))).
### 
In ``genreg/``
- ``topkl.py`` generate random regular graphs and compute the eigenvalues of adjecency matrix then save the graph as pickle object. 

- ``tocsv.py`` read the pickeled graph and compute cheeger constant using *multiprocessing* and save it to csv file. 

## Usages:
- **Optional** : To create *[miniconda](https://docs.conda.io/en/latest/miniconda.html)* ``python3`` enviroment with all dependencies installed.
> `` chmod +x env.sh  && ./env.sh ``

> `` source ~/miniconda3/bin/activate``

> `` pip install -r requirements.txt``

 - `` python main.py argv[1] argv[2] argv[3]``
 
     ``argv[1]`` : size of graph (number of vertices)
 
     ``argv[2]`` : random graphs will be generated for each regularity and repeated graphs will be removed. 
 
     ``argv[3]``: filename. 

- **Output** : 2 files

     ``filename.pkl``: graphs objects in pickeled format.

     ``filename.csv``: Eigenvalues of graph and cheeger constant.
 

