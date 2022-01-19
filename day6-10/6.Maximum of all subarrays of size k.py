class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        q = []
        l = r = 0
        ans = []
        while r < len(arr):
            while q and arr[q[-1]] < arr[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.pop(0)
            
            if r + 1 >= k:
                ans.append(arr[q[0]])
                l += 1
            r += 1
        return ans