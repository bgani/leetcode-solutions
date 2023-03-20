class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

        
    # Merge in-place
    def merge(self, arr, s, m, e):
        # Copy the sorted left & right to temp arrays
        L = arr[s: m + 1] # leftSubarray
        R = arr[m + 1: e + 1] # rightSubarray

        i = 0 # index for leftSubarray
        j = 0 # index for righSubarray
        k = s # index for arr, keeps track of where next element in arr needs to be placed

        # Merge the two sorted halves int the original array (Two Pointer i and j)
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1 

        # One of the halves will have elements remaning
        # Add remaining elements to arr
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while k < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, arr, s, e): 
        # base case, if elements count in Sub Array is <= 1 then return arr
        if e - s + 1 <= 1:
            return arr
        
        # The middle index of array 
        m = (s + e) // 2
        # Sort the left half
        self.mergeSort(arr, s, m)
        # Sort the right half
        self.mergeSort(arr, m + 1, e)
        # Merge sorted halves
        self.merge(arr, s, m, e)
        return arr