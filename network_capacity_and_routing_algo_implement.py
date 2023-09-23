

class Heap():

	def __init__(self):
		self.arr = []
		self.size = 0
		self.rank = []

	def newMinHeapNode(self, j, data):
		minHeapNode = [j, data]
		return minHeapNode

	# A utility function to swap two nodes
	# of min heap. Needed for min heapify
	def change(self, a, b):
		t = self.arr[a]
		self.arr[a] = self.arr[b]
		self.arr[b] = t

	# A standard function to heapify at given idx
	# This function also updates rankition of nodes
	# when they are swapped.rankition is needed
	# for update()
	def minHeapify(self, idx):
		smallest = idx
		left = 2*idx + 1
		right = 2*idx + 2

		if (left < self.size and
		self.arr[left][1]
			< self.arr[smallest][1]):
			smallest = left

		if (right < self.size and
		self.arr[right][1]
			< self.arr[smallest][1]):
			smallest = right

		# The nodes to be swapped in min
		# heap if idx is not smallest
		if smallest != idx:

			# Swap rankitions
			self.rank[self.arr[smallest][0]] = idx
			self.rank[self.arr[idx][0]] = smallest

			# Swap nodes
			self.change(smallest, idx)

			self.minHeapify(smallest)

	# Standard function to extract minimum
	# node from heap
	def extractMin(self):

		# Return NULL wif heap is empty
		if self.isEmpty() == True:
			return

		# Store the root node
		root = self.arr[0]

		# Replace root node with last node
		lastNode = self.arr[self.size - 1]
		self.arr[0] = lastNode

		# Update rankition of last node
		self.rank[lastNode[0]] = 0
		self.rank[root[0]] = self.size - 1

		# Reduce heap size and heapify root
		self.size -= 1
		self.minHeapify(0)

		return root

	def isEmpty(self):
		return True if self.size == 0 else False

	def update(self, v, dist):

		# Get the index of v in heap arr

		i = self.rank[v]

		# Get the node and update its dist value
		self.arr[i][1] = dist

		# Travel up while the complete tree is
		# not heapified. This is a O(Logn) loop
		while (i > 0 and self.arr[i][1] <
				self.arr[(i - 1) // 2][1]):

			# Swap this node with its parent
			self.rank[ self.arr[i][0] ] = (i-1)//2
			self.rank[ self.arr[(i-1)//2][0] ] = i
			self.change(i, (i - 1)//2 )

			# move to parent index
			i = (i - 1) // 2;

	# A utility function to check if a given
	# vertex 'v' is in min heap or not
	def ispresent(self, v):

		if self.rank[v] < self.size:
			return True
		return False




def findMaxCapacity(n,a,src,dest):
    minHeap=Heap()
    minHeap.size=n
    graph=[[] for i in range(n)]
    d={}
    for i,j,k in a:
        if d.get((i,j))==None and d.get((j,i))==None:
            d[(i,j)]=k
        elif d.get((i,j))!=None:
            d.update({(i,j):max(d.get((i,j)),k)})
        else:
           d.update({(j,i):max(d.get((j,i)),k)})

    for i,j in d.keys():
        k=d[(i,j)]
        graph[i].append([j,-1*k])
        graph[j].append([i,-1*k])
    data=[]
    parent=[None]*n
    # print(graph)
    for i in range(n):
        data.append(float('inf'))
        minHeap.arr.append(minHeap.newMinHeapNode(i, data[i]))
        minHeap.rank.append(i)
    data[src]*=-1
    minHeap.rank[src]=src
    minHeap.update(src, data[src])

    while not minHeap.isEmpty():
        newHeapNode = minHeap.extractMin()
        i = newHeapNode[0]
        for w in graph[i]:
            j=w[0]
            if minHeap.ispresent(j) and data[i]!=float('inf') and max(w[1],data[i])<data[j]:
                data[j]=max(w[1],data[i])
                parent[j]=i
                minHeap.update(j, data[j])
    t=dest
    b=[]
    # print(parent)
    while t!=None:
        b.append(t)
        t=parent[t]

    for i in range(n):
        data[i]*=-1
	# print(graph[0])
    return data[dest],b[::-1]

print(findMaxCapacity(7,[(0,1,2),(0,2,5),(1,3,4), (2,3,4),(3,4,6),(3,5,4),(2,6,1),(6,5,2)],0,5))
print(findMaxCapacity(5,[(0,1,3),(1,2,5),(2,3,2),(3,4,3),(4,0,8),(0,3,7),(1,3,4)],0,2))
print(findMaxCapacity(170,[(29, 23, 15), (23, 45, 23), (45, 11, 69), (11, 4, 129), (4, 34, 68), (34, 47, 93), (47, 14, 9), (14, 16, 35), (16, 19, 48), (19, 24, 2), (24, 26, 16), (26, 13, 38), (13, 46, 57), (46, 28, 13), (28, 9, 118), (9, 22, 37), (22, 20, 101), (20, 30, 102), (30, 0, 79), (0, 12, 48), (12, 43, 49), (43, 21, 12), (21, 18, 19), (18, 48, 33), (48, 44, 97), (44, 39, 106), (39, 42, 24), (42, 40, 104), (40, 49, 21), (49, 1, 51), (1, 50, 42), (50, 36, 41), (36, 17, 30), (17, 15, 50), (15, 10, 80), (10, 3, 29), (3, 31, 96), (31, 8, 108), (8, 33, 34), (33, 27, 84), (27, 25, 45), (25, 7, 3), (7, 41, 29), (41, 37, 33), (37, 38, 39), (38, 2, 65), (2, 32, 32), (32, 5, 82), (5, 35, 81), (35, 6, 25), (31, 21, 11), (18, 15, 7), (26, 0, 116), (36, 0, 2), (49, 15, 62), (19, 6, 116), (49, 32, 97), (12, 16, 12), (30, 1, 122), (21, 47, 86), (42, 49, 60), (33, 34, 20), (33, 3, 97), (1, 30, 95), (37, 9, 87), (31, 39, 2), (19, 4, 105), (2, 31, 32), (31, 1, 56), (4, 18, 100), (23, 40, 116), (28, 22, 27), (47, 19, 66), (39, 48, 62), (13, 12, 9), (18, 30, 117), (11, 25, 88), (14, 6, 50), (33, 25, 130), (3, 36, 122), (43, 47, 75), (41, 43, 50), (9, 3, 64), (47, 32, 28), (49, 48, 19), (17, 44, 90), (39, 16, 66), (37, 39, 45), (23, 19, 121), (28, 22, 36), (11, 33, 72), (8, 14, 68), (5, 2, 40), (23, 35, 85), (20, 6, 18), (31, 39, 113), (42, 1, 100), (46, 6, 124), (43, 19, 80), (44, 22, 42), (26, 22, 8), (31, 49, 94), (31, 18, 7), (49, 8, 19), (43, 31, 57), (10, 45, 87), (8, 42, 94), (24, 20, 56), (23, 37, 81), (15, 39, 28), (43, 10, 63), (34, 50, 117), (46, 6, 51), (19, 40, 12), (34, 33, 115), (35, 29, 84), (48, 46, 5), (25, 13, 70), (17, 27, 121), (34, 10, 128), (31, 2, 16), (39, 5, 66), (44, 41, 87), (42, 28, 107), (27, 46, 66), (39, 1, 20), (15, 9, 9), (24, 35, 34), (31, 21, 46), (14, 36, 58), (42, 27, 66), (14, 47, 110), (27, 49, 91), (26, 15, 46), (12, 47, 75), (33, 41, 127), (35, 26, 119), (43, 12, 54), (10, 45, 127), (27, 41, 119), (38, 2, 43), (24, 44, 122), (41, 33, 112), (24, 8, 91), (44, 31, 125), (17, 50, 54), (20, 48, 96), (17, 36, 7), (9, 26, 18), (12, 8, 48), (42, 50, 15), (38, 0, 21), (41, 39, 74), (26, 30, 87), (13, 9, 130), (38, 45, 87), (1, 25, 113), (19, 3, 11), (50, 48, 4), (0, 19, 97), (14, 17, 107), (16, 12, 23), (14, 8, 105), (7, 49, 84), (29, 17, 56), (34, 38, 102), (47, 33, 52), (37, 38, 95), (43, 22, 123), (21, 36, 24)],46,31))




