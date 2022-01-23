class Solution:
    def getNthUglyNo(self,n):
        nums = [0] * n
        nums[0] = 1
        i2 = i3 = i5 = 0
        i2_num = 2
        i3_num = 3
        i5_num = 5
        for i in range(1, n):
            next_num = min(i2_num, i3_num, i5_num)
            nums[i] = next_num
            if next_num == i2_num:
                i2 += 1
                i2_num = nums[i2] * 2
            if next_num == i3_num:
                i3 += 1
                i3_num = nums[i3] * 3
            if next_num == i5_num:
                i5 += 1
                i5_num = nums[i5] * 5
        return nums[-1]