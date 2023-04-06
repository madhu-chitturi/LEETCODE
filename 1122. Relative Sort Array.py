class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        for i in range(len(arr2)):
            a=arr1.count(arr2[i])
            for j in range(a):
                arr1.remove(arr2[i])
                res.append(arr2[i])
        return res+sorted(arr1)
