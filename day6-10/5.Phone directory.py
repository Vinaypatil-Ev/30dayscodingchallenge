#User function Template for python3
import collections
class TRIE():
    def __init__(self):
        # self.chld = collections.OrderedDict({chr(i): None for i in range(97, 97 + 26)} )
        self.chld = collections.OrderedDict()
        for i in range(97, 97 + 26):
            self.chld[chr(i)] = None
        self.end = False
    def insert(self, word):
        curr = self
        for i in word:
            if not curr.chld[i]:
            # if i not in curr.chld:
                curr.chld[i] = TRIE()
            curr = curr.chld[i]
        curr.end = True
    def find(self, prefix):
        ans = []
        def dfs(curr, word, is_):
            if curr.end:
                if is_:
                    ans.append(word)
                
            for w, trie in curr.chld.items():
                if trie:
                    dfs(trie, word + w, is_ or ((word + w) == prefix))
        dfs(self, "", False)
        return ans
class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        t = TRIE()
        for word in contact:
            t.insert(word)
        # print(t.chld["s"].chld)
        ans = []
        for i in range(1, len(s) + 1):
            res = t.find(s[:i])
            if res:
                ans.append(res)
            else:
                ans.append([0])
        # print(ans)
        return ans
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends