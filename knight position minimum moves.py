
class cell:

	def __init__(self, x=0, y=0, dist=0):
		self.x = x
		self.y = y
		self.dist = dist

# checks whether given position is
# inside the board


def isInside(x, y, N):
	if (x >= 1 and x <= N and
			y >= 1 and y <= N):
		return True
	return False

# Method returns minimum step to reach
# target position


def minStepToReachTarget(knightpos,targetpos, N):

	dx = [2, 2, -2, -2, 1, 1, -1, -1]
	dy = [1, -1, 1, -1, 2, -2, 2, -2]

	queue = []

	queue.append(cell(knightpos[0], knightpos[1], 0))

	visited = [[False for i in range(N + 1)]
			for j in range(N + 1)]

	visited[knightpos[0]][knightpos[1]] = True

	while(len(queue) > 0):

		t = queue[0]
		queue.pop(0)

		if(t.x == targetpos[0] and
		t.y == targetpos[1]):
			return t.dist

		for i in range(8):

			x = t.x + dx[i]
			y = t.y + dy[i]

			if(isInside(x, y, N) and not visited[x][y]):
				visited[x][y] = True
				queue.append(cell(x, y, t.dist + 1))



knightpos = [0,0]
targetpos = list(map(int,input().split()))
print(minStepToReachTarget(knightpos,targetpos, 30))
