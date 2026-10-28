import numpy as np
def solve_jacobi(a: np.ndarray, b: np.ndarray, n: int) -> list:
	# a is ( b , N ) , x is ( b , 1 )
	# b is ( b , 1 ) 
	m , N = a.shape 
	X = np.zeros(m)
	# def sumV () : 
	# 	total = 0 
	# 	for i in range ( m ) : 
	# 		for j in range ( N ) : 
	# 			if j != i :
	# 				total += (a[i][j] * X[j])
	# 	return total
	for k in range ( n ) : 
		X_new = np.zeros(m)
		for i in range ( m ) : 
			total = 0 
			for j in range ( N ) : 
				if i != j : 
					total += ( a[i][j] * X[j])
			X_new[i] =( 1 / a[i][i] ) * (b[i] - total)
		X = X_new
	return X 