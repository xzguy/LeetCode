'''
Leetcode problem 315

In principle, there are two key operations for Binary Indexed Tree (BIT):
    1, i += (i & -i), same as 'i = (i | (i-1)) + 1'
    2, i -= (i & -i), same as 'i = i & (i-1)'
based on these two operations, two kinds of trees can be constructed, where
each operation moves the node to its parent in the corresponding tree.
The following property is kept:
    to get sum from 0 to index 'i' in the array, sum the node 'i' in BIT up
along all its ancestors using second operation, until 'i' equal zero.
    to update a node 'i' in BIT, also update all nodes depending on node 'i',
where all these nodes can be traversed by the first operation until 'i' is too big.

The above implementation is based on one-based index of BIT.
The zero-based index BIT has different operations and implementation.
'''

def getSum(BITree, i):
    '''
    returns sum of array[0 ... index i].
    This function assumes that the array is preprocessed
    and partial sums of array elements are stored in BITree[].
    
    Input:
        i: int, index
    Output:
        s: int, sum of subarray[0, i] (inclusive on both ends)
    '''
    s = 0   # initialize result

    # index in BITree[] is 1 more than the index in array[]
    # because there is a dummy 0 at the beginning of BITree[]
    i += 1

    # traverse ancestors of BITree[i]
    while i > 0:
        # add current element of BITree to sum
        s += BITree[i]

        # move index i to its parent node
        i -= (i & -i)
    return s

def updateBIT(BITree, i, val):
    '''
    updates a node in BITree at given index i.
    The given value 'val' is added to BITree[i]
    and all of its ancestors.
    Input:
        BITree: [int], Binary Indexed Tree
        i: int, index 
        val: int, value to add at index i
    Output:
        None, update BITree in place
    '''
    # length of the original array
    N = len(BITree) - 1

    # index in BITree[] is 1 more than the index in array[]
    # because there is a dummy 0 at the beginning of BITree[]
    i += 1

    # traverse all ancestors and add 'val'
    while i <= N:
        # add 'val' to current node of BITree
        BITree[i] += val

        # update index for next node to add value
        i += (i & -i)

def construct(arr):
    '''
    constructs and returns a Binary Indexed Tree for given array

    Input:
        arr: [int], input array
    Output
        BITree: [int], Binary Indexed Tree
    '''
    n = len(arr)

    BITree = [0] * (n+1)

    # store actual values in BITree[] using update()
    for i in range(n):
        updateBIT(BITree, i, arr[i])

    return BITree

nums = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BITree = construct(nums)

print("BIT values are")
for i in range(1, len(BITree)):
    print(BITree[i], end='\n' if i==len(BITree)-1 else ', ')

print("Sum of elements in arr[0..5] is " + str(getSum(BITree, 5))) 
nums[3] += 6
updateBIT(BITree, 3, 6) 
print("Sum of elements in arr[0..5] after update is " + str(getSum(BITree, 5))) 
