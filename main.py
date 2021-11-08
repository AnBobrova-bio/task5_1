def medians(nums1, nums2):
    nums3new = nums1 + [el2 for el2 in nums2 if el2 not in nums1]
    nums3new.sort()
    if len(nums3new) % 2 == 1:
        pr = float(nums3new[len(nums3new) // 2])
        print(format(pr, '.3f'))
    else:
        k = (len(nums3new) // 2)
        pr = float(nums3new[k - 1] + nums3new[k] / 2)
        print(format(pr, '.3f'))

nums1 = input().split()
nums2 = input().split()
medians(nums1, nums2)