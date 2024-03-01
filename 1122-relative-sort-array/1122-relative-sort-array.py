class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        nums1 = []
        nums2 = []
        for a in arr1:
            if a in set(arr2):
                nums1.append(a)
            else:
                nums2.append(a)
        counter = Counter(nums1)
        ans = []

        for i in arr2:
            ans += [i] * counter[i]

        return ans + sorted(nums2)