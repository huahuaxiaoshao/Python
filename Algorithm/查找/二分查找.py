class Solution:
    def binary_search(self,array,key):
        if array == []:
            return -1
        low,high = 0,len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            if array[mid] == key:
                return mid
            elif array[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return -1


a = [1,3,5,7,8,10]
print(Solution().binary_search(a,10))