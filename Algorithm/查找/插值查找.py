class Solution:
    def interpolation_search(self,array,key):
        if array == []:
            return -1
        low,high = 0,len(array) - 1
        while low <= high:
            mid = low + (key - array[low]) * (high - low) // (array[high] - array[low])
            if array[mid] == key:
                return mid
            elif array[mid] < key:
                high = mid - 1
            else:
                low = mid + 1
        return -1

a = [1,3,5,7,8,10]
print(Solution().interpolation_search(a,5))


