class Solution:
    def bubble_sort(self,array):
        if len(array) <= 1:
            return array
        for i in range(len(array)-1):
            for j in range(i+1,len(array)):
                if array[i] > array[j]:
                    array[i],array[j] = array[j],array[i]
        return array

a = [6,1,2,7,9,3,4,5,10,8]
print(Solution().bubble_sort(a))