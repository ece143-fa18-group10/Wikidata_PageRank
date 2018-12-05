import numpy as np

nodes = []
links = []
ranks = np.loadtxt('../PageRank_result.txt')
sortedRanks = np.sort(ranks)
numberOfNodes = 200

with open('../input.txt') as fh:
	for i, line in enumerate(fh):
		row = line.split()
		if row[0] == 'n':
			url = row[2]
			if url[-1] == '/' or url[-1] == '\\':
				url = url[: -1]
			nodes.append((ranks[i], url, row[1]))
		elif row[0] == 'e':
			links.append((row[1], row[2]))

minrank = sortedRanks[-numberOfNodes]
maxrank = sortedRanks[-1]

with open('data.js', 'w') as fh:
	fh.write('data = {"nodes":[\n')

	count = 0
	idMap = {}
	for row in nodes:
		rank = row[0]
		if rank >= sortedRanks[-numberOfNodes]:
			if count > 0: fh.write(',\n')
			rank = 19 * ((rank - minrank) / (maxrank - minrank))
			fh.write('{' + '"rank":' + str(rank) + ', "url":"' + row[1] + '"}')
			idMap[row[2]] = count
			count += 1
	fh.write('],\n')

	fh.write('"links":[\n')
	count = 0
	for row in links:
		if row[0] not in idMap or row[1] not in idMap : continue
		if count > 0: fh.write(',\n')
		fh.write('{"source":' + str(idMap[row[0]]) + ',"target":' + str(idMap[row[1]]) + '}')
		count += 1
	fh.write(']};')
