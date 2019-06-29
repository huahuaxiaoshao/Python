class Solution:
    def insertion_sort(self,array):
        if array == []:
            return
        for i in range(len(array)):
            pre_index = i - 1
            current = array[i]
            while pre_index >= 0 and current < array[pre_index]:
                array[pre_index + 1] = array[pre_index]
                pre_index -= 1
            array[pre_index + 1] = current
        return array

a = [3,4,2,6,7,1,9,8,0,5]
print(Solution().insertion_sort(a))
