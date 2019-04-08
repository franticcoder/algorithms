# Leetcode : 15. 3Sum
#
# Author: Chungmin Kim
# Date: Apr 7, 2019
# https://leetcode.com/problems/3sum/?fbclid=IwAR3qon3L3vd4F3a4gTlCMSjZxaua5bn4yswKNOieZu7VNdm_1nOnzPmYW8g

class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        result = []

        if len(nums) < 3:
            return []

        # sort the given list
        nums = sorted(nums)

        # The main idea is that while looping the given list from 0 to length,
        # we find other 2 numbers that the sum of three numbers are zero.
        for i in range(0, len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                st = i+1
                end = len(nums)-1

                while (st < end):

                    # when the sum is zero, add the list to outer list
                    # and increase or decrease indexs(st,end)
                    if( nums[i] + nums[st] + nums[end] == 0 ):
                        result.append([nums[i], nums[st], nums[end]])
                        st += 1
                        end -= 1

                        while( nums[st] == nums[st-1] and st < end ):
                            st += 1

                        while( nums[end] == nums[end+1] and st < end ):
                            end -= 1

                    # if less than zero, increase index(st)
                    elif( nums[i] + nums[st] + nums[end] < 0):
                        st += 1
                    # if grater than zero, decrease index(end)
                    else:
                        end -= 1

        return result


sol = Solution()

inArr = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(inArr))

