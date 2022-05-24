class Solution: 
    def solve(self,A): 
        if len(A)==len(set(A)): 
            return -1 
        for i in range(len(A)): 
            if A.count(A[i])>1: 
                return A[i]
