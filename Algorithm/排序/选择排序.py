class Solution:
    def selection_sort(self,array):
        if array == []:
            return
        for i in range(len(array)):
            min_index = i
            for j in range(i + 1,len(array)):
                if array[min_index] > array[j]:
                    min_index = j
            if i != min_index:
                array[min_index],array[i] = array[i],array[min_index]
        return array

a = [3,4,2,6,7,1,9,8,0,5]
print(Solution().selection_sort(a))
