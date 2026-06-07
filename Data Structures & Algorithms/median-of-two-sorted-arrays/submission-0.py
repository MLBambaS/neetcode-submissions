class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A): 
            A,B = B,A
        total = len(A) + len(B)
        half = total // 2
        l,r = 0, len(A)-1
        while True:
            i = l + (r-l)//2
            j = half-1-(i+1)
            A_left = A[i] if i>=0 else float("-infinity")
            A_right = A[i+1] if i < len(A)-1 else float("infinity")
            B_left = B[j] if j>=0 else float("-infinity")
            B_right = B[j+1] if j<len(B)-1 else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 0:
                    return (min(A_right, B_right)+max(A_left, B_left))/2
                else:
                    return min(A_right, B_right)
            elif A_left > B_right:
                r = i-1
            else:
                l = i+1