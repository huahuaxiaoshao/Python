class Solution:
    def merge_sort(self,array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        return self.merge(self.merge_sort(array[0:mid]),self.merge_sort(array[mid:]))

    def merge(self,left,right):
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        return result + left + right


a = [3,4,2,6,7,1,9,8,0,5]
print(Solution().merge_sort(a))
