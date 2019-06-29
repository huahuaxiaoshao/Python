class Solution:
    def quick_sort(self,left,right,array):
        if left > right:
            return
        i = left
        j = right
        while i < j:
            while array[j] >= array[left] and i < j:
                j -= 1
            while array[i] <= array[left] and i < j:
                i += 1
            if i < j:
                array[i],array[j] = array[j],array[i]
        array[left],array[i] = array[i],array[left]
        self.quick_sort(left,i-1,array)
        self.quick_sort(i+1,right,array)
        return array

a = [6,1,2,7,9,3,4,5,10,8]
print(Solution().quick_sort(0,len(a)-1,a))