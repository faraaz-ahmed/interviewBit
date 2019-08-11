class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        s = ''
        for i in range(len(A)):
            s = s + str(A[i])
        return list(str(int(s) + 1))