class Solution:
    def counting_sort(self,array):
        if array == []:
            return []
        array_len = len(array)
        array_min = min(array)
        array_max = max(array)

        counting_array_len = array_max - array_min + 1
        counting_array = [0] * counting_array_len

        for num in array:
            counting_array[num - array_min] += 1

        for i in range(1,len(counting_array)):
            counting_array[i] += counting_array[i - 1]

        result = [0] * array_len

        for num in array:
            result[counting_array[num - array_min] - 1] = num
            counting_array[num - array_min] -= 1
        return result

a = [3,4,2,6,7,1,9,8,0,5]
print(Solution().counting_sort(a))