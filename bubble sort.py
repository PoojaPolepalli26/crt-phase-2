def performbubblesort(nums):
    n=len(nums)
    fixthisindex =n-1
    while fixthisindex >0:
        for index in range(fixthisindex):
            if nums[index]>nums[index +1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
        fixthisindex -=1
nums=[10,8,2,14,12,7]
print("before sorting",nums)
performbubblesort(nums)
print("after sorting:",nums)

