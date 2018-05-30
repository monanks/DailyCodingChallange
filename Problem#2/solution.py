def solution(list1):
    """
    time complexity: O(N)
    space complexity: O(N)
    """
    nums = [1 for i in list1]
    temp = 1
    
    for i in range(1,len(list1)):
        nums[i] = nums[i-1] * list1[i-1]

    for i in range(len(list1)-1, 0, -1):
        temp *= list1[i]
        nums[i-1] *= temp 
    
    return nums

l1 = [10, 15, 3, 7]

print(solution(l1))

l1 = [1, 2, 3, 4, 5]

print(solution(l1))

l1 = [2, 5]

print(solution(l1))