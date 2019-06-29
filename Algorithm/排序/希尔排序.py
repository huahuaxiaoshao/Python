class Solution:
    def hill_sort(self,array):
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]
        for gap in gaps:
            i = gap
            while i < len(array):
                temp = array[i]
                j = i
                while j > 0 and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
                i += 1
        return array

a = [3,4,2,6,7,1,9,8,0,5]
print(Solution().hill_sort(a))