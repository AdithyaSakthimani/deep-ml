import numpy as np 
def calculate_brightness(img):
	if len(img) == 0 :
		return -1 
	R , C = len(img) , len(img[0])
	if R != C : 
		return -1 
	for v in img : 
		if len(v) != C : 
			return -1 
	nimg = np.array(img)
	m , n = nimg.shape 
	den = m * n 
	res = 0 
	for i in range ( m ) : 
		for j in range ( n ) : 
			res += img[i][j]
	return res / den
