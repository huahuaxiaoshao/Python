class Solution:
    def linear_search(self,array,key):
        if array == []:
            return -1
        for i in range(len(array)):
            if array[i] == key:
                return i
        return -1

a = [1,3,5,7,8,10]
print(Solution().linear_search(a,4))