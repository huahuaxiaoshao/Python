class Solution:
    def radix_sort(self,array):
        RADIX = 10
        placement = 1
        array_max = max(array)
        while placement < array_max:
            buckets = [[] for _ in range(RADIX)]

            for num in array:
                buckets[(num // placement) % RADIX].append(num)

            index = 0
            for i in range(RADIX):
                temp = buckets[i]
                for num in temp:
                    array[index]  = num
                    index += 1

            placement *= RADIX

        return array

a = [3,4,2,6,7,1,9,8,0,5]
print(Solution().radix_sort(a))