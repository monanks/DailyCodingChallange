def solution(list1,num):
    """
    time complexity: O(N)
    space complexity: O(N)
    """
    nums = set()

    for element in list1:
        if num - element in nums:
            return True
        else:
            nums.add(element)
    return False

l1 = [10, 15, 3, 7]
s = 17

print(solution(l1,s))

l1 = [10, 15, 3, 7]
s = 19

print(solution(l1,s))