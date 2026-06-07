class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        total = m + n
        half = (total + 1) // 2
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = half - i

            A_left = float("-inf") if i == 0 else A[i - 1]
            A_right = float("inf") if i == m else A[i]

            B_left = float("-inf") if j == 0 else B[j - 1]
            B_right = float("inf") if j == n else B[j]

            if A_left <= B_right and A_right >= B_left:
                if total % 2 == 1:
                    return max(A_left, B_left)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            if A_left > B_right:
                right = i - 1
            else:
                left = i + 1
