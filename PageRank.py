import numpy as np

def pageRankIter(transitionMatrix, PRMaxtrix, beta, epsilon, maxIter):
	'''
	:type transitionMatrix: ndarray
	:type PRMatrix: ndarray
	:type beta: float
	:type epsilon: float
	:type maxIter: int
	:rtype: ndarray
	'''
	for _ in range(maxIter):
		newPRMatrix = (1 - beta) * transitionMatrix.dot(PRMatrix) + beta * PRMatrix
		if np.sum(np.absolute(newPRMatrix - PRMaxtrix)) < epsilon:
			return newPRMatrix
		PRMaxtrix = newPRMatrix
	return PRMaxtrix
