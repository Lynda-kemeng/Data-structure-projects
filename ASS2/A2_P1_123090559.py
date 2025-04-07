import queue
from collections import Counter
global counts, listA, listN, dic, removed_elements
n = int(input())
listA = list(map(int, input().split()))
listAcopy = listA.copy()
counts = Counter(listA)
listN = list(range(1, n + 1))
dic = {i + 1: element for i, element in enumerate(listA)}
removed_elements = queue.Queue()
setA = set(listAcopy)

def search_next(i):
    element = dic[i]
    if counts[element] == 0:
        removed_elements.put(element)
        kk = dic[element]
        counts[kk] -= 1
        search_next(element)
    else:
        return



for i in listN:
    if i not in setA:
        removed_elements.put(i)
        k = dic[i]
        counts[k] -= 1
        search_next(i)

print(removed_elements.qsize())





