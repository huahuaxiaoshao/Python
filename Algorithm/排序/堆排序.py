class Solution:
    def heap_sort(self,array):
        n = len(array)
        if n <= 1:
            return array
        for i in range(n // 2 - 1,-1,-1):
            self.heapify(array,i,n)
        for i in range(n - 1,-1,-1):
            array[0],array[i] = array[i],array[0]
            self.heapify(array,0,i)
        return array


    def heapify(self,unsorted,index,heap_size):
        index_max = index
        left_index = 2 * index + 1
        right_index = 2 * index +2
        if left_index < heap_size and unsorted[left_index] > unsorted[index_max]:
            index_max = left_index
        if right_index < heap_size and unsorted[right_index] > unsorted[index_max]:
            index_max = right_index
        if index_max != index:
            unsorted[index_max],unsorted[index] = unsorted[index],unsorted[index_max]
            self.heapify(unsorted,index_max,heap_size)


a = [3,4,2,6,7,1,9,8,0,5]
print(Solution().heap_sort(a))