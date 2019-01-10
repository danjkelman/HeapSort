#my goal would be to at some point make it so that you can introduce any number of intergers
heap=[]
seq=[[2,6],[2,5],[1,4],[1,3],[0,2],[0,1]]
finalList=[]

for i in range(7):
    heap.append(int(input("input interger: ")))

while len(seq)>0:
    for x in range(len(heap)):
        for i in range(len(seq)):
            seq2=seq[i]
            if heap[seq2[0]]>heap[seq2[1]]:
                heap[seq2[0]], heap[seq2[1]] = heap[seq2[1]], heap[seq2[0]]
    finalList.append(heap[0])
    del heap[0]
    test = 1
    test = test + 1
    if test%2==0:
        del seq[0]
finalList.append(heap[0])
    
print("done",finalList)
