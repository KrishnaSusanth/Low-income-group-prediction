# Simple python code computing values of the sequence defined as follows
# A(1) = 0 and A(n) = A(n-1) + 3/(n*(n-1)) for n>1
#
# 1. Find and fix the two mistakes in computeValue (if you do not fix
# them the code will give you an execution error)
#
# 2. Afterwards, look at the output. Does it help you in finding a
# non-recursive definition of A(n)? Does it help you in guessing the
# limit?
#
# 3*. computeValue can be simplified into a very simple
# computation. How does this alternative version look like?

# A(1) = 0 and A(n) = A(n-1) + 3/(n*(n-1)) for n>1
def computeValue(N):
    if N==1:
        return 0
    else:
        return computeValue(N-1) + 3/(N*(N - 1))


def printValue(N):
    if N < 1 or not isinstance(N, int):
        print("This sequence starts from 1 and N has to be a natural number!\n")
    elif N == 1:
        print('A(1) = 0\n')
    else:
        value = computeValue(N)
        print('A({0}) = A({1}) + 3/{2} = {3}\n'.format(N, N-1, N*(N-1), value))



for i in range(91,101):
    printValue(i)
