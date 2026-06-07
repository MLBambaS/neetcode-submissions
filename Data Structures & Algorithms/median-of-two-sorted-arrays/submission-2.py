class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A)>len(B):
            A,B = B,A
        total = len(A)+len(B)
        half = total//2
        l, r = 0, len(A)-1
        while True:
            m = (l+r)//2
            A_left = A[m] if m>=0 else float("-infinity")
            A_right = A[m+1] if m<len(A)-1 else float("infinity")
            k = half-1-(m+1)
            B_left = B[k] if k >=0 else float("-infinity")
            B_right = B[k+1] if k<len(B)-1 else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                if total%2==0 : 
                    return (max(A_left, B_left)+min(A_right, B_right))/2
                else:
                    return min (A_right, B_right)
            elif A_left > B_right:
                r = m-1
            else :
                l= m+1
        