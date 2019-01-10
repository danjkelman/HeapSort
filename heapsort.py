#incomplete will come back to soon but step one is out of the way
heap=[]
seq=[[1,3],[1,4],[2,5],[2,6],[0,1],[0,2]]

for i in range(7):
    heap.append(int(input("input interger: ")))
print(heap)
for i in range(len(seq)):
    seq2=seq[i]
    if heap[seq2[0]]<heap[seq2[1]]:
        heap[seq2[0]], heap[seq2[1]] = heap[seq2[1]], heap[seq2[0]]
        print(heap)
print("done",heap)
