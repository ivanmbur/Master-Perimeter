import sympy as sp
import numpy as np
import numba

N=4


m=sp.Matrix([[ 2,  3,  4,  5,  6,  4,  2,  3],
 [ 3,  6,  8, 10, 12,  8,  4,  6],
 [ 4,  8, 12, 15, 18, 12,  6,  9],
 [ 5, 10, 15, 20, 24, 16,  8, 12],
 [ 6, 12, 18, 24, 30, 20, 10, 15],
 [ 4,  8, 12, 16, 20, 14,  7, 10],
 [ 2,  4,  6,  8, 10,  7,  4,  5],
 [ 3,  6,  9, 12, 15, 10,  5,  8]])

#@numba.jit
def getElements(N):
	
	arr = np.array([],dtype=np.int)	

	for e1 in range(N):
		if(2 * e1>N):
			break
		for e2 in range(N):
			if((2*e1+3*e2)>N):
				break
			for e3 in range(N):
				if((2*e1+3*e2 + 4*e3)>N):
					break
				for e4 in range(N):
					if((2*e1+3*e2 + 4*e3+5*e4)>N):
						break
					for e5 in range(N):
						if((2*e1+3*e2 + 4*e3+5*e4+6*e5)>N):
							break
						for e6 in range(N):
							if((2*e1+3*e2 + 4*e3+5*e4+6*e5+ 4*e6)>N):
								break
							for e7 in range(N):
								if((2*e1+3*e2 + 4*e3+5*e4+6*e5+ 4*e6+2*e7)>N):
									break
								for e8 in range(N):
									if((2*e1+3*e2 + 4*e3+5*e4+6*e5+ 4*e6+2*e7 + 3*e8)>N):
										break
									vec = [e1,e2,e3,e4,e5,e6,e7,e8]
									if vec !=[0,0,0,0,0,0,0,0]:
										arr = np.append(arr,np.array(vec))
	
	L = int(np.shape(arr)[0]/8)
	arr = np.reshape(arr,(L,8))
	return sp.Matrix(arr)/N

def check(N,elem):
    length = np.shape(elem)[0]
    for t in range(length):
            t = elem[t,:]
            value = t*(m * t.transpose())/2
            if(np.floor(N*value)!=np.array(N*value)):
                print("For the element "+str(t) + ", we get "+str(value[0,0]) + "\t Anomaly!!")
            else:
                print("For the element "+str(t) + ", we get "+str(value[0,0] ))

elem = getElements(N)
check(N,elem)

