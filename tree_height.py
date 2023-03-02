# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    max_height = 0
    
    for i,p in enumerate(parents):
        if p == n:
            max_height = max(max_height, compute_height(i, parents) + 1)

    return max_height


def main():
    input_method = input()
    if "F" in input_method:
        filepath = input()
        if 'a' in filepath:
            return
        with open(filepath, 'r', encoding='UTF-8') as file:
            (n, parents_text) = file.read().splitlines()
    elif "I" in input_method:
        n = input()
        parents_text = input()
    else:
        return
    
    parents = list(map(int, parents_text.split()))
    root = -1

    print(compute_height(root, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))