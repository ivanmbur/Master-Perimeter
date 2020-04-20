import numpy as np

#Define the length of an axis  of the lattice.

l=2

#Create an array with all of the vertices.

vertices = np.array([[n,m] for n in range(l) for m in range(l)])

#Create an array with all of the edges.

edges = np.concatenate((np.array([[p,p+[1,0]] for p in vertices]),np.array([[p,p+[1,0]] for p in vertices])), axis=0)

#Create all possible diagrams. A 0 corresponds to a dashed line while a 1 to a bold line.

state = 
