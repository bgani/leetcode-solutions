class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if(len(nums) == 1):
            return nums

        return self.quickSort(nums, 0, len(nums) - 1)

    # DID NOT PASS LEETCODE TESTCASES ON SUBMISSION FOR VERY BIG ARRAY: TIME LIMIT EXCEEDED
    def quickSort(self, arr, s, e):
        # base case
        if e - s + 1 <= 1:
            return
        
        pivot = arr[e] # we start pivot from last element
        left_pointer = s # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(s, e):
            if(arr[i] < pivot):
                tmp = arr[left_pointer]
                arr[left_pointer] = arr[i]
                arr[i] = tmp
                left_pointer += 1

        # Move pivot in-between left & right sides
        arr[e] = arr[left_pointer]
        arr[left_pointer] = pivot

        # quick sort for left side, don't include pivot
        self.quickSort(arr, s, left_pointer - 1)

        # quick sort for right side, don't include pivot
        self.quickSort(arr, left_pointer + 1, e)

        return arr


        