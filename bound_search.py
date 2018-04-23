# Bound search for Matrix Spencer

import numpy as np
import random
from numpy import linalg as LA
from scipy.stats import ortho_group

def min_search(N):

	#Matrix Generation
	matrix = []

	while len(matrix) < N:

		#Generate random orthogonal matrix:
		b = ortho_group.rvs(N)

		#generate random diagonal matriix with eigner vals (Spectral norm decomposition)
		vec = []
		for j in range (N):
			#temp = random.uniform(0,1)
			temp = random.choice([1])
			vec.append(temp)
		d=np.diag(vec)

		#Genrating the final matrix
		b_symm = b.dot(d.dot(b.T))

		#Spectral norm of the matrix
		norm = LA.norm(b_symm, 2)

		if norm <= 1:
			matrix.append(b_symm)

	#Test for norm condition satisfiability
	#for m in matrix:
		#print(LA.norm(m, 2))
		#w, v = LA.eig(m)
		#print(w)

	#generation of +1 and -1 of all combination
	sigma_list = []
	def sigma_val(sigma, n):
		sigma1 = sigma.copy()
		if n == 1:
			sigma.append(1)
			sigma1.append(-1)
			sigma_list.append(sigma)
			sigma_list.append(sigma1)
			return()
		else:
			#add 1 to N'th position
			sigma.append(1)
			sigma_val(sigma, n-1)
			#add -1 to Nth position
			sigma1.append(-1)
			sigma_val(sigma1, n-1)

	sigma_empty = []
	sigma_val(sigma_empty, N)

	#Use sigma_list and matrix

	norm_val = []
	for i in sigma_list:
		temp = np.zeros((N,N))
		for pos in range(len(i)):
			temp = temp + i[pos]*matrix[pos]
		norm_val.append(LA.norm(temp, 2))

	return(min(norm_val))

N =12
global_min = 0
for i in range(10000):
	random_min = min_search(N)
	#searching largest among the minimum
	if random_min > global_min:
		global_min = random_min

print(global_min)











