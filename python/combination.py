class Solution:
    def combinationSum(self, candidates, target):
        res = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])  # can reuse same element
                path.pop()
        
        backtrack(0, [], target)
        return res
        
