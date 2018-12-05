import numpy as np

def pageRankIter(transitionMatrix, PRMatrix, beta, epsilon, maxIter):
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
		if np.sum(np.absolute(newPRMatrix - PRMatrix)) < epsilon:
			return newPRMatrix
		PRMatrix = newPRMatrix
	return PRMatrix

if __name__ == '__main__':
	from build_trans_mat import build_trans_mat
	from PageRank_matrix import pr_matrix
	transitionMatrix = build_trans_mat()
	PRMaxtrix = np.ones((transitionMatrix.shape[0], 1))
	res = pageRankIter(transitionMatrix, PRMaxtrix, 0.2, 0.0001, 100000)
	print(res)
	np.savetxt('PageRank_result.txt', res)
