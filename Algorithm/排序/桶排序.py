class Solution:
    def bucket_sort(self,array,bucket_size):
        if array == []:
            return
        min_value = min(array)
        max_value = max(array)
        bucket_count = (max_value - min_value) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]

        for i in range(len(array)):
            buckets[(array[i] - min_value) // bucket_size].append(array[i])

        return sorted([buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i]))])

print(Solution().bucket_sort([3,4,2,6,7,1,9,8,0,5],5))