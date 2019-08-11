"""You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B."""

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A = list(A)
        # hash_ = []
        # for i in range(len(A)):
        #     hash_.append(0)
        sum_ = 0
        for i in range(len(A)):
            sum_ += A[i]
        for i in range(len(A)):
            A[abs(A[i]) - 1] = A[abs(A[i]) - 1] * (-1)
        dup = []
        for i in range(len(A)):
            if A[i] > 0:
                dup.append(i + 1)
        for i in range(0,len(A)):
            if dup[0] == abs(A[i]):
                return dup[0], dup[1]
            elif dup[1] == abs(A[i]):
                return dup[1], dup[0]
            else:
                continue
        # miss = (len(A) * (len(A) + 1)) / 2 - (sum_ - dup)
        return dup[0], dup[1]
            
