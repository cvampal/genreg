# genreg
generate regular graphs and calculate isoperimertic constant.
There are python modules topkl and tocsv. 
>topkl generate random regular graphs and compute the eigenvalues of adjecency matrix then save the graph as pickle object. 

>tocsv read the pickeled graph and compute cheeger constant (isoperimetric constant) using multiprocessing and save it to csv file. 

## Usages:
- **Optional** 
 To make a python enviroment run `./env.sh` It will download miniconda and install all required dependencies. 
 or if you have python already run ` pip install -r requirements.txt` only.
 
- run ` python main.py n k filename ` where n is size of graph (no of vertex) k is sample size (for each regularity of n) 
it will generate about (nk) unique graphs if n is even else (nk/2).
