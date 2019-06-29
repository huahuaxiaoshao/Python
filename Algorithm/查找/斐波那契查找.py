class Solution:

    def fibonacci(self,size):
        if size == 0:
            return []
        elif size == 1:
            return [1]
        elif size == 2:
            return [1,1]
        else:
            F = [1,1]
            for i in range(size - 2):
                F.append(F[-1] + F[-2])
            return F

    def fibonacci_search(self,array,key,size):
        F = self.fibonacci(size)
        low,high = 0,len(array) - 1
        n = high
        k = 0
        while n > F[k] - 1:
            k += 1
        while low <= high:
            mid = low + F[k - 1] - 1
            if array[mid] > key:
                high = mid - 1
                k -= 1
            elif array[mid] < key:
                low = mid + 1
                k -= 2
            else:
                if mid <= n:
                    return mid
                else:
                    return n
        return -1


a = [0,1,16,24,35,47,59,62,73,88,99]
print(Solution().fibonacci_search(a,59,10))