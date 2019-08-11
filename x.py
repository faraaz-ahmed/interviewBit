"""
Flip
Asked in:  
VMWare
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

Notes:

Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
For example,

S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
"""

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        A = list(map(int,A))
        dex = []
        recent_bit, recent_count = 0, 0
        for i in range(len(A)):
            # print('bit and count',recent_bit,recent_count)
            if i == 0 and A[i] == 0:
                recent_bit = 0
                recent_count += 1
            elif i == 0 and A[i] == 1:
                recent_bit = 1
                recent_count += 1
            else:
                if A[i] == 1 and recent_bit == 1:
                    recent_count += 1
                elif A[i] == 1 and recent_bit == 0:
                    dex.append(recent_count)
                    # print('one')
                    recent_count, recent_bit = 1, 1
                elif A[i] == 0 and recent_bit == 0:
                    recent_count += 1
                elif A[i] == 0 and recent_bit == 1:
                    dex.append(recent_count)
                    # print(2)
                    recent_count, recent_bit = 1, 0
        if i == len(A) - 1:
            dex.append(recent_count)
            # print(3)
        # print('dex = ', dex)
        # print(A[0], len(dex))
        # if A[0] == 1 and len(dex) == 1:
            # print('ok')
        if A[0] == 0:
            for i in range(len(dex)):
                if not i % 2 == 0:
                    dex[i] = dex[i] * (-1)
        else:
            for i in range(len(dex)):
                if i % 2 == 0:
                    dex[i] = dex[i] * (-1)
        # print(dex, "dex")
        max_sum_so_far, current_sum = 0, 0
        start, s, end = 0, 0, 0
        for i in range(len(dex)):
            current_sum += dex[i]
            if current_sum < 0:
                current_sum = 0
                s = i + 1
            elif current_sum > max_sum_so_far:
                max_sum_so_far = current_sum
                start = s
                end = i
                # s = i + 1
                
        current_sum, ms = 0, 0
        index = []
        for i in range(len(dex)):
            current_sum += dex[i]
            if current_sum == max_sum_so_far:
                index.append(i)
            if current_sum < 0:
                current_sum = 0
            elif current_sum > ms:
                ms = current_sum
        if len(index) > 0:
            end = index[0]
        # print(index, "index")
        # print(start, end, 'start and end')
        sum1, sum2 = 0, 0
        for i in range(len(dex)):
            if i < start:
                sum1 += abs(dex[i])
            # if i == start:
            #     sum2 = sum1
            if i <= end:
                sum2 += abs(dex[i])
        # if start == end and start == 0:
        #     sum1, sum2 = 0, 0
        #     for i in range(len(dex)):
        #         if i < start:
        #             sum1 += abs(dex[i])
        #         # if i == start:
        #         #     sum2 = sum1
        #         if i < end + 1:
        #             sum2 += abs(dex[i])
            
        # print('meow')
        sum_ = 0
        for i in range(len(A)):
            sum_ = sum_ + int(A[i])
        if sum_ == len(A):
            return []
        else:
            # print('whyyyy', A[0], len(dex))
            return [sum1 + 1, sum2]
                
                    
                    
            